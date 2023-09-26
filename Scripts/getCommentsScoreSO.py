'''
Comments with at least a score of 10 on stackoverflow
Reference: https://stackapi.readthedocs.io/en/latest/user/complex.html#comments-with-at-least-a-score-of-10-on-ask-ubuntu
'''

from stackapi import StackAPI
import json

def sendCommentsBiggestScoreToFile(output_file, keyword, num_found):
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

def getCommentsScore(tag):
   # Crie uma instância da StackAPI
    print("Tag:", tag)
    total_upvotes = 0
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key)
    questions = so.fetch('questions', tagged=[tag, 'java'], sort='votes')
    print("Total de perguntas com a tag:", len(questions['items']))
    for question in questions['items']:
        question_id = question['question_id']
        comments = so.fetch('questions/{}/comments'.format(question_id))
        print("Total de comentários na pergunta:", len(comments['items']))
        for comment in comments['items']:
            print(comment['score'])
            total_upvotes += comment['score']

    print(f"Total de upvotes nos comentários da tag '{tag}': {total_upvotes}")
    return total_upvotes


if __name__ == "__main__":
  tags = getSoTag()
  for tag in tags:
    biggest_score = getCommentsScore(tag)
    print("\n")
    sendCommentsBiggestScoreToFile("biggest_score.txt", tag, biggest_score)