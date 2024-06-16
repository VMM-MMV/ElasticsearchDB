from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

index_mapping = {
    "mappings": {
        "properties": {
            "name": {"type": "text"},
            "gaming": {"type": "float"},
            "work": {"type": "float"},
            "casual": {"type": "float"},
            "school": {"type": "float"},
            "storage_size": {"type": "float"},
            "battery_life": {"type": "float"},
            "ethernet_port": {"type": "float"},
            "hdmi_port": {"type": "float"},
            "screen_resolution": {"type": "float"},
            "keyboard_backlight": {"type": "float"},
            "weight": {"type": "float"},
            "price": {"type": "integer"},
            "additional_specs": {"type": "object", "enabled": False},  # Additional specifications
            "store_name": {"type": "keyword", "index": False}  # Store name not indexed but retrievable
        }
    }
}
 
# Create the index (if it doesn't exist)
if not es.indices.exists(index='computers'):
    es.indices.create(index='computers', body=index_mapping)