import json
with open(r"file.json", "r") as data:
        Text=json.load(data)
obj={
        "name":"siddhi",
        "department" : "IT"
        }
Text.append(obj)
print(Text)

with open(r"file.json", "w") as d:
        json.dump(Text,d)
