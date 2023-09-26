'''
Questions with the tag on stackoverflow
Reference: https://stackapi.readthedocs.io/en/latest/user/complex.html#comments-with-at-least-a-score-of-10-on-ask-ubuntu
'''

from stackapi import StackAPI
from datetime import datetime
import json

def sendQuestionsToFile(output_file, keyword, num_found):
    output_file = open(output_file, "a")
    output_file.write(keyword + ":" + str(num_found) + "\n")
    output_file.close()

def getArtifacts():
    artifacts = {}
    with open("Dataset.json", "r") as myfile:
        artifacts = json.loads(myfile.read(), strict=False)
    return artifacts

def getSoTag():
    artifacts = getArtifacts()
    tags = []
    for artifact in artifacts:
        so_tag = artifact["SOtags"]
        tags.append(so_tag)
    return tags   

def getQuestions(tag):
   # Crie uma instância da StackAPI
    total_questions = 0
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key)
    page = 1
    total_questions = 0

    while True:
        print("Página:", page)
        questions = so.fetch('questions', tagged=tag, sort='votes', pagesize=100, page=page, fromdate=datetime(2018,1,1), todate=datetime(2023,8,1))
        total_questions += len(questions['items'])
        page += 1

        if 'has_more' not in questions or not questions['has_more'] or page > 100:
            break
    return total_questions


if __name__ == "__main__":
  tags = getSoTag()
  for tag in tags:
    questions = getQuestions(tag)
    print("Tag:", tag)
    print("Total de perguntas com a tag:", questions)
    print("\n")
    sendQuestionsToFile("questions.txt", tag, questions)