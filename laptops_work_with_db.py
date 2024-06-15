from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])
# docs = [
#     {
#         "name": "IdeaPad 1i",
#         "gaming": 0.4,
#         "work": 0.7,
#         "casual": 0.8,
#         "school": 0.9,
#         "storage_size": 0.6,
#         "battery_life": 0.5,
#         "ethernet_port": 1,
#         "hdmi_port": 1,
#         "screen_resolution": 0.4,
#         "keyboard_backlight": 0,
#         "weight": 0.7,
#         "price": 600,
#         "additional_specs": {
#             "cpu": "Intel Core i5",
#             "ram": "8 GB DDR4",
#             "storage": "256 GB SSD",
#             "gpu": "Integrated Intel UHD Graphics",
#             "OS": "Windows 10 Home"
#         },
#         "store_name": "Best Buy"
#     },
#     {
#         "name": "Gaming Beast 2000",
#         "gaming": 0.9,
#         "work": 0.3,
#         "casual": 0.4,
#         "school": 0.2,
#         "storage_size": 0.8,
#         "battery_life": 0.6,
#         "ethernet_port": 1,
#         "hdmi_port": 1,
#         "screen_resolution": 0.9,
#         "keyboard_backlight": 1,
#         "weight": 0.5,
#         "price": 1200,
#         "additional_specs": {
#             "cpu": "AMD Ryzen 7",
#             "ram": "16 GB DDR4",
#             "storage": "512 GB SSD + 1 TB HDD",
#             "gpu": "NVIDIA GeForce RTX 3060",
#             "OS": "Windows 10 Pro"
#         },
#         "store_name": "Amazon"
#     },
#     {
#         "name": "UltraPortable X",
#         "gaming": 0.3,
#         "work": 0.8,
#         "casual": 0.9,
#         "school": 0.9,
#         "storage_size": 0.5,
#         "battery_life": 0.7,
#         "ethernet_port": 0,
#         "hdmi_port": 0,
#         "screen_resolution": 0.7,
#         "keyboard_backlight": 0,
#         "weight": 0.9,
#         "price": 800,
#         "additional_specs": {
#             "cpu": "Intel Core i3",
#             "ram": "4 GB DDR4",
#             "storage": "128 GB SSD",
#             "gpu": "Integrated Intel UHD Graphics",
#             "OS": "Windows 11 Home"
#         },
#         "store_name": "Newegg"
#     }
# ]

# Bulk index documents
# for doc in docs:
#     try:
#         res = es.index(index="computers", body=doc)
#         print(f"Indexed document: {doc['name']}, Result: {res}")
#     except Exception as e:
#         print(f"Failed to index document {doc['name']}: {e}")

# Query for the best match for multiple criteria and sort by price
query = {
    "query": {
        "function_score": {
            "query": {"match_all": {}},
            "functions": [
                # {"field_value_factor": {"field": "gaming", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "work", "factor": 1, "modifier": "none"}},
                {"field_value_factor": {"field": "casual", "factor": 1, "modifier": "none"}},
                {"field_value_factor": {"field": "school", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "storage_size", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "battery_life", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "ethernet_port", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "hdmi_port", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "screen_resolution", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "keyboard_backlight", "factor": 1, "modifier": "none"}},
                # {"field_value_factor": {"field": "weight", "factor": 1, "modifier": "none"}}
            ],
            "score_mode": "avg",
            "boost_mode": "replace"
        }
    },
    "sort": [
        {"price": {"order": "asc", "unmapped_type": "integer"}}  # Sort by price in ascending order
    ]
}

# Define the search query with function score and filter for store_name "Best Buy"
# query = {
#     "query": {
#         "function_score": {
#             "query": {
#                 "bool": {
#                     "must": [
#                         {"match_all": {}}
#                     ],
#                     "filter": [
#                         {"term": {"store_name": "Best Buy"}}
#                     ]
#                 }
#             },
#             "functions": [
#                 {"field_value_factor": {"field": "casual", "factor": 1, "modifier": "none"}},
#                 {"field_value_factor": {"field": "school", "factor": 1, "modifier": "none"}}
#             ],
#             "score_mode": "sum",  # Optional: Adjust scoring mode as needed
#             "boost_mode": "replace"  # Optional: Adjust boost mode as needed
#         }
#     },
#     "sort": [
#         {"_score": {"order": "desc"}},  # Sort by score descending
#         {"price": {"order": "asc"}}     # Then by price ascending
#     ]
# }

# Search the index
response = es.search(index='computers', body=query)

# Print search results
print("Search Results:")
for hit in response['hits']['hits']:
    print(f"Name: {hit['_source']['name']}, Price: {hit['_source']['price']}")
    # Access additional specifications if needed
    additional_specs = hit['_source'].get('additional_specs', {})
    if additional_specs:
        print("Additional Specifications:")
        for key, value in additional_specs.items():
            print(f"{key}: {value}")
    # Access store name
    store_name = hit['_source'].get('store_name', '')
    if store_name:
        print(f"Store: {store_name}")
    print()