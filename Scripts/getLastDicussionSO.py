from stackapi import StackAPI
import json

def get_artifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts
   

def getLastDiscussedDates(tag):
   # Crie uma instância da StackAPI
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key, impose_throttling=True)

    questions = so.fetch('questions', tagged=[tag, 'java'], sort='creation', order='desc', limit=5)
    dates_string = ""
    for i in range(0, 10):
        if questions == None or i >= len(questions):
            break
        if i > 0:
            dates_string += ';'
        dates_string += questions[i].creation_date.strftime("%m/%d/%Y, %H:%M:%S") + " UTC"
    print("Datas: ", dates_string)

def get_so_tag():
    artifacts = get_artifacts()
    tags = []
    for artifact in artifacts:
        so_tag = artifact["SOtags"]
        tags.append(so_tag)
    print("\n")
    return tags
        
  

if __name__ == "__main__":
  tags = get_so_tag()
  print ("Tags: ", tags)
  for tag in tags:
    print("Tag: ", tag)
    getLastDiscussedDates(tag)