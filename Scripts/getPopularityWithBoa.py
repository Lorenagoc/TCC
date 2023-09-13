"""
- Script para buscar a popularidade de bibliotecas através de uma query na API do Boa.
- O script busca pelos imports das bibliotecas em projetos Java do GitHub.
- Query Boa fonececido por: Eduardo Cunha Campos (Orientador)
- Referência: https://github.com/ualberta-smr/LibraryMetricScripts
"""

import getpass
import json
import time
import re

from boaapi.boa_client import BoaClient, BOA_API_ENDPOINT
from boaapi.status import CompilerStatus, ExecutionStatus


def send_totals_to_file(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()


def get_artifact_names():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts


def boa_search(artifact_id):
    # Username: lorenacabral
    # Password: Lo090899@

    client = BoaClient(endpoint=BOA_API_ENDPOINT)
    client.login("lorenacabral", "Lo090899@")

    # Login com credenciais
    # user = input("Username [%s]: " % getpass.getuser())
    # if not user:
    #   user = getpass.getuser()
    # client.login(user, getpass.getpass())
    # print("successfully logged in to Boa API")

    query = f"""
projectsCount: output sum of int;

awt := false;

visit(input, visitor {{
    after node: Project ->
        if (awt)
            projectsCount << 1;
	# only look at the latest snapshot of Java files
	before n: CodeRepository -> {{
		snapshot := getsnapshot(n, "SOURCE_JAVA_JLS");
		foreach (i: int; def(snapshot[i]))
			visit(snapshot[i]);
		stop;
	}}
	before node: ASTRoot ->
	    exists(j: int; match("{artifact_id}", node.imports[j])) {{
			awt = true;
			stop;
	    }}
	before node: Type ->
	    if (match("{artifact_id}", node.name)) {{
			awt = true;
			stop;
	    }}
}});
 """

    artifact_popularity = 0
    # query using a specific dataset
    job = client.query(query, client.get_dataset("2019 October/GitHub"))
    print("query submitted")

    while job.is_running():
        job.refresh()
        print("job " + str(job.id) + " still running, waiting 10s...")
        time.sleep(10)

    if job.compiler_status is CompilerStatus.ERROR:
        print("job " + str(job.id) + " had compile error")
    elif job.exec_status is ExecutionStatus.ERROR:
        print("job " + str(job.id) + " had exec error")
    else:
        try:
            artifact_popularity = re.search(r"\d+", job.output()).group()
        except:
            pass

    client.close()
    print("client closed")
    return artifact_popularity


def main():
    artifact_names = get_artifact_names()
    for artifact_name in artifact_names:
        print(
            "Searching for cleaartifact: "
            + str(artifact_name["LibraryName"])
            + "..."
            + "\n"
        )
        artifact_popularity = boa_search(artifact_name["LibraryName"].replace("-", "."))
        send_totals_to_file(
            "popularity.txt", artifact_name["LibraryName"], artifact_popularity
        )


if __name__ == "__main__":
    main()
