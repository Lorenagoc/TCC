import getpass
import json
import time
import requests
import re

from boaapi.boa_client import BoaClient, BOA_API_ENDPOINT
from boaapi.status import CompilerStatus, ExecutionStatus

# def get_artifact_names(start, rows):
#     url = f"https://search.maven.org/solrsearch/select?q=*:*&rows={rows}&start={start}&wt=json"
#     response = requests.get(url)
#     data = response.json()

#     artifacts = []
#     docs = data["response"]["docs"]
#     for doc in docs:
#         artifact_id = doc["a"]
#         if artifact_id not in artifacts :
#             artifact_id = artifact_id.replace("-", '.')
#             boa_search(artifact_id)
#             artifacts.append(artifact_id)
#         else : continue
#     return artifacts

def get_artifact_names():    
    with open("artifacts_out.txt", "r") as txt_file:
        artifacts = txt_file.read().splitlines()
    return artifacts

def boa_search(artifact_id):

    # Username: lorenacabral
    # Password: Lo090899@

    client = BoaClient(endpoint=BOA_API_ENDPOINT)
    client.login("lorenacabral", "Lo090899@")
    
    # user = input("Username [%s]: " % getpass.getuser())
    # if not user:
    #     user = getpass.getuser()
    # client.login(user, getpass.getpass())
    # print("successfully logged in to Boa API")

    # artifact_id = "org.junit"

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

    # print(query)

    # query using a specific dataset
    # job = client.query(query, client.get_dataset("2019 October/GitHub"))
    job = client.query(query, client.get_dataset("2019 October/GitHub (medium)"))
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
            print("output: ")
            print(re.search(r'\d+', job.output()).group())
            # with open("popularidade.txt", "w") as txt_file:
            #     for projectCount in job.output().find("projectsCount"):
            #         txt_file.write(projectCount + "\n")
            # txt_file.close()
        except:
            pass

    client.close()
    print("client closed")

def main():
    artifact_names = get_artifact_names()
    for artifact_name in artifact_names:
        print("Searching for artifact: " + artifact_name + "..." + "\n")
        boa_search(artifact_name)

if __name__ == "__main__":
    main()
        
