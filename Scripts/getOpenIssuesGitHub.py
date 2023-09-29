'''
Get count of repository open issues
Reference: https://pygithub.readthedocs.io/en/stable/index.html
'''

from github import Github
import json

def sendOpenIssuesToFile(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def getArtifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def getOpenIssues(repository_name):
    
    # Inicializa a instância do Github
    g = Github("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", timeout=30)

    # Obtém o repositório desejado
    repo = g.get_repo(repository_name)

    openIssues = repo.get_issues(state='open')
    totalIssues = 0

    for issue in openIssues:
        print("Issue:", issue)
        totalIssues += 1
    print("Qtde de issues:", totalIssues)
    print("\n")
    return totalIssues

def getRepositoryName():
    artifacts = getArtifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        print("Repository name:", repository_name)
        openIssues = getOpenIssues(repository_name)
        sendOpenIssuesToFile("issues.txt", repository_name, openIssues)

if __name__ == "__main__":
    getRepositoryName()