from github import Github
import json

def get_artifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def get_frequency_release(repository_name):
    
    # Inicializa a instância do Github
    g = Github("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")

    # Obtém o repositório desejado
    repo = g.get_repo(repository_name)

    releases = repo.get_releases()
    num_releases = releases.totalCount

    if num_releases >= 2:
        # Obtém as duas últimas releases
        releases = repo.get_releases()[:2]  # Obtém as duas últimas releases

        # Itera pelas releases e imprime informações relevantes
        print("Releases do repositório:", repository_name)
        for release in releases:
            # print("Nome:", release.title)
            # print("Tag:", release.tag_name)
            print("Data de lançamento:", release.created_at)
        print("\n")
    elif num_releases == 1:
        print("Última release do repositório:", repository_name)
        release = repo.get_latest_release()
        # print("Nome:", release.title)
        # print("Tag:", release.tag_name)
        print("Data de lançamento:", release.created_at)
        print("\n")
    else:
        last_commits = repo.get_commits()[:2]
        print("Não há releases para o repositório:", repository_name)
        for commit in last_commits:
            commit_created_at = commit.commit.author.date
            print("Data de lançamento do commit:", commit_created_at)
        print("\n")


def get_repository_name():
    artifacts = get_artifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        get_frequency_release(repository_name)

if __name__ == "__main__":
    get_repository_name()