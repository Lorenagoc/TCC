from github import Github
import json

def sendLastButOneModificationDateToFile(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def getArtifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def getLastButOneModificationDate(repository_name):
    
    # Inicializa a instância do Github
    g = Github("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", timeout=30)

    # Obtém o repositório desejado
    repo = g.get_repo(repository_name)

    # Obtém o penúltimo commit do repositório
    print("Qtde de commits:", len(list(repo.get_commits())))
    commit = repo.get_commits()[1]
    lastCreationCommitFormatted = commit.commit.author.date.strftime('%d-%m-%Y %H:%M:%S')
    return lastCreationCommitFormatted

def getRepositoryName():
    artifacts = getArtifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        print("Repository name:", repository_name)
        lastButOneDate = getLastButOneModificationDate(repository_name)
        sendLastButOneModificationDateToFile("lastButOneModification.txt", repository_name, lastButOneDate)

if __name__ == "__main__":
    getRepositoryName()