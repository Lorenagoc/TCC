'''
Get number of upvotes of stackoverflow comments
Reference: https://stackapi.readthedocs.io/en/latest/user/complex.html#comments-with-at-least-a-score-of-10-on-ask-ubuntu
'''

from stackapi import StackAPI
from datetime import datetime
import json
import time

def sendUpvotesToFile(output_file, keyword, num_found):
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

def getUpvotes(tag):
   # Crie uma instância da StackAPI
    print("Tag:", tag)
    total_upvotes = 0
    page = 1
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key)
    questions = so.fetch('questions', tagged=[tag, 'java'], sort='votes')
    print("Total de perguntas com a tag:", len(questions['items']))


    while True:
        print("Página:", page)
        questions = so.fetch('questions', tagged=tag, sort='votes', pagesize=100, page=page, fromdate=datetime(2018,1,1), todate=datetime(2023,8,1))
        page += 1
        for question in questions['items']:
            question_id = question['question_id']
            comments = so.fetch('questions/{}/comments'.format(question_id))
            print("Total de comentários para a pergunta atual", len(comments['items']))
            time.sleep(1)
            for comment in comments['items']:
                print("Upvotes -> ", comment['score'])
                total_upvotes += comment['score']
                time.sleep(1)

        if 'has_more' not in questions or not questions['has_more'] or page > 100:
            break

    print(f"Total de upvotes nos comentários da tag '{tag}': {total_upvotes}")
    return total_upvotes


if __name__ == "__main__":
  tags = getSoTag()
  for tag in tags:
    upvotes = getUpvotes(tag)
    print("\n")
    sendUpvotesToFile("upvotes.txt", tag, upvotes)