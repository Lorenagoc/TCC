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
    print("Tag:", tag)
    user_api_key = 'hDxbIGl*XQDx7qfyHHi9QA(('
    so = StackAPI('stackoverflow', key=user_api_key)
    
    total_comments = 0
    
    # Parâmetros para a pesquisa de perguntas
    params = {
        'tagged': tag,
        'sort': 'votes',
        'pagesize': 100,
        'fromdate': datetime(2018, 1, 1),
        'todate': datetime(2023, 8, 1),
        'page': 1
    }
    
    max_queries = 10  # Defina o número máximo de consultas que deseja fazer
    queries = 0
    
    while queries < max_queries:
        questions = so.fetch('questions', **params)
        for question in questions['items']:
            question_id = question['question_id']
            comments = so.fetch('questions/{}/comments'.format(question_id))
            total_comments += len(comments['items'])
        
        print("Total de comentários para a tag '{}': {}".format(tag, total_comments))
        
        if 'has_more' not in questions or not questions['has_more']:
            break
        
        # Aumente o tempo de espera para não exceder os limites de taxa
        time.sleep(5)  # Espere 5 segundos entre as consultas
        
        # Avance para a próxima página
        params['page'] += 1
        queries += 1  # Acompanhe o número de consultas feitas

    return total_comments


if __name__ == "__main__":
  tags = getSoTag()
  for tag in tags:
    comments = getComments(tag)
    print("\n")
    sendCommentsToFile("comments.txt", tag, comments)