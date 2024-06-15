from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# docs = [
#   {"name": "IdeaPad 1i", "lightweight": 0.9, "portable": 0.8, "gaming_power": 0.2},
#   {"name": "Gaming Beast 2000", "lightweight": 0.2, "portable": 0.3, "gaming_power": 0.9},
#   {"name": "UltraPortable X", "lightweight": 0.95, "portable": 0.95, "gaming_power": 0.1}
# ]

# for i, doc in enumerate(docs, 1):
#   es.index(index='computers', id=i, document=doc)

# Query for the best match for lightweight and portable
query = {
  "query": {
    "function_score": {
      "query": {
        "match_all": {}
      },
      "functions": [
        {
          "field_value_factor": {
            "field": "lightweight",
            "factor": 1,
            "modifier": "none"
          }
        },
        {
          "field_value_factor": {
            "field": "portable",
            "factor": 1,
            "modifier": "none"
          }
        }
      ],
      "score_mode": "avg",
      "boost_mode": "replace"
    }
  }
}

# Search the index
response = es.search(index='computers', body=query)
print(response)