from github import Github
from github import RateLimitExceededException
import calendar
import time
import json

def sendLastButOneModificationDateToFile(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ";" + str(num_found) + "\n")
    output_file.close()

def getArtifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def getLastButOneModificationDate(repository_name):
    while True:
        try:
            # Inicializa a instância do Github
            g = Github("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", timeout=30)

            repo = g.get_repo(repository_name)
            commits = list(repo.get_commits())
            commit = commits[1]
            lastCreationCommitFormatted = commit.commit.author.date.strftime('%d-%m-%Y %H:%M:%S')
            return lastCreationCommitFormatted
        except StopIteration:
            break  # loop end
        except RateLimitExceededException:
            search_rate_limit = g.get_rate_limit().search
            reset_timestamp = calendar.timegm(search_rate_limit.reset.timetuple())
            # add 10 seconds to be sure the rate limit has been reset
            sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 10
            time.sleep(sleep_time)
            continue
        except Exception as e:
            print(f"Erro ao obter dados do repositório {repository_name}: {str(e)}")
            return None

def getRepositoryName():
    artifacts = getArtifacts()
    for artifact in artifacts:
        repository_name = artifact["FullRepoName"]
        print("Repository name:", repository_name)
        lastButOneDate = getLastButOneModificationDate(repository_name)
        sendLastButOneModificationDateToFile("lastButOneModification.txt", repository_name, lastButOneDate)
         # Espere 5 segundos entre as solicitações para evitar exceder os limites de taxa
        time.sleep(5)

if __name__ == "__main__":
    getRepositoryName()