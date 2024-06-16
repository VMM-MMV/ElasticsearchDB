import json
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])
with open('laptop/files/categorized_topic.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for doc in data:
    try:
        res = es.index(index="computers", body=doc)
        print(f"Indexed document: {doc['name']}, Result: {res}")
    except Exception as e:
        print(f"Failed to index document {doc['name']}: {e}")