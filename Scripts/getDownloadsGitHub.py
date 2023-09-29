'''
Get number of clones for the last year
Reference: https://pygithub.readthedocs.io/en/stable/index.html
'''

from github import Github
import json

def sendDownloadsToFile(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def getArtifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def getDownloads(repository_name):
    
    # Inicializa a instância do Github
    g = Github("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", timeout=30)
    downloads = 0
    # Obtém o repositório desejado
    repo = g.get_repo(repository_name)
    releases = repo.get_releases()
    for release in releases:
        assets = release.get_assets()
        for asset in assets:
            downloads += asset.download_count
            print("Downloads:", downloads)
    return downloads

def getRepositoryName():
    artifacts = getArtifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        print("Repository name:", repository_name)
        downloads = getDownloads(repository_name)
        sendDownloadsToFile("downloads.txt", repository_name, downloads)

if __name__ == "__main__":
    getRepositoryName()