from github import Github
import datetime
import json

def send_last_modification_date_to_file(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def get_artifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def get_last_modification_date(repository_name):
    
    # Inicializa a instância do Github
    g = Github("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", timeout=30)

    # Obtém o repositório desejado
    repo = g.get_repo(repository_name)

     # Obtém os últimos 5 (ou os últimos disponíveis) commits do repositório
    print("Qtde de commits:", len(list(repo.get_commits())))
    if len(list(repo.get_commits())) >= 5:
        commits = list(repo.get_commits()[:5])
    else:
        commits = list(repo.get_commits())

    dates_string = ""

    for i, commit in enumerate(commits, start=1):
        creation_commit_formatted = commit.commit.author.date.strftime('%d-%m-%Y %H:%M:%S')
        
        if i == len(commits):
            dates_string += creation_commit_formatted
        else:
            dates_string += creation_commit_formatted + ";"

    print("dates_string: ", dates_string)
    print("\n")
    return dates_string

def get_repository_name():
    artifacts = get_artifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        print("Repository name:", repository_name)
        last_dates = get_last_modification_date(repository_name)
        send_last_modification_date_to_file("lastModificationDate.txt", repository_name, last_dates)

if __name__ == "__main__":
    get_repository_name()