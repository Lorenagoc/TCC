'''
Get count of repository stars
Reference: https://pygithub.readthedocs.io/en/stable/index.html
'''

from github import Github
import json

def sendStartsToFile(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def getArtifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def getStarts(repository_name):
    
    # Inicializa a instância do Github
    g = Github("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", timeout=30)

    # Obtém o repositório desejado
    repo = g.get_repo(repository_name)

     # Obtém a qtde de estrelas o repositorio possui
    print("Qtde de starts:", repo.stargazers_count)
    if repo.stargazers_count:
        return repo.stargazers_count
    else:
        return 0

def getRepositoryName():
    artifacts = getArtifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        print("Repository name:", repository_name)
        starts = getStarts(repository_name)
        sendStartsToFile("starts.txt", repository_name, starts)

if __name__ == "__main__":
    getRepositoryName()