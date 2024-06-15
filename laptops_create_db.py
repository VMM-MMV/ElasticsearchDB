from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Define the index mapping
index_mapping = {
  "mappings": {
    "properties": {
      "name": {"type": "text"},
      "lightweight": {"type": "float"},
      "portable": {"type": "float"},
      "gaming_power": {"type": "float"}
    }
  }
}

# Create the index  
es.indices.create(index='computers', body=index_mapping)