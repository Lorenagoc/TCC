'''
Comments with the tag on stackoverflow
Reference: https://stackapi.readthedocs.io/en/latest/user/complex.html#comments-with-at-least-a-score-of-10-on-ask-ubuntu
'''

from stackapi import StackAPI
from datetime import datetime
import json
import time

def sendCommentsToFile(output_file, keyword, num_found):
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
    print("\n")
    return tags   

def getComments(tag):
   # Crie uma instância da StackAPI
    print("Tag:", tag)
    total_comments = 0
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key)
    questions = so.fetch('questions', tagged=[tag, 'java'], sort='votes')
    page = 3
    print("Total de perguntas com a tag:", len(questions['items']))

    while True:
        print("Página:", page)
        questions = so.fetch('questions', tagged=tag, sort='votes', pagesize=100, page=page, fromdate=datetime(2018,1,1), todate=datetime(2023,8,1))
        page += 1
        for question in questions['items']:
            question_id = question['question_id']
            comments = so.fetch('questions/{}/comments'.format(question_id))
            total_comments += len(comments['items'])
            print("Total de comentários para a pergunta atual", len(comments['items']))
            time.sleep(1)

        if 'has_more' not in questions or not questions['has_more'] or page > 100:
            break
    
    print(f"Total de comentários para tag '{tag}': {total_comments}")
    return total_comments


if __name__ == "__main__":
  tags = getSoTag()
  for tag in tags:
    comments = getComments(tag)
    print("\n")
    sendCommentsToFile("comments.txt", tag, comments)