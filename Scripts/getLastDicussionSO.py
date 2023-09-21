from stackapi import StackAPI
import datetime
import json

def send_last_discussions_to_file(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def get_artifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def get_so_tag():
    artifacts = get_artifacts()
    tags = []
    for artifact in artifacts:
        so_tag = artifact["SOtags"]
        tags.append(so_tag)
    print("\n")
    return tags   

def getLastDiscussedDates(tag):
   # Crie uma instância da StackAPI
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key, impose_throttling=True)

    # Obtem as cinco perguntas mais recentes com a tag
    questions = so.fetch('questions', tagged=[tag, 'java'], sort='creation', order='desc', limit=5)
    dates_string = ""

    if questions['items']:
        for i, question in enumerate(questions['items'], start=1):
            creation_date_formatted = datetime.datetime.fromtimestamp(question['creation_date']) .strftime('%d-%m-%Y %H:%M:%S')

            if i >= len(questions):
                dates_string += creation_date_formatted
                break
            elif i > 0:
                dates_string += creation_date_formatted + ";"
    else:
        dates_string = None
    return dates_string

if __name__ == "__main__":
  tags = get_so_tag()
  for tag in tags:
    print("Tag:", tag)
    last_discussions = getLastDiscussedDates(tag)
    print("Últimas discussões:", last_discussions)
    print("\n")
    send_last_discussions_to_file("last_discussions.txt", tag, last_discussions)