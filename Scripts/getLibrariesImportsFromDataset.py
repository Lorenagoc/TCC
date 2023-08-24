import json

with open("dataset-info.json") as json_file:
    data = json.load(json_file)
    
with open("artifacts_out.txt", "w") as txt_file:
    for key in data.keys():
        txt_file.write(str(data[key]["artifactId"]).replace("-", ".") + "\n")