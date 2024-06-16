import json
from classify import *

# Load JSON data from a file
with open('files/results_all_17.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate over the JSON data
result_all = []
for item in data:
    response = classify(name=item['name'][:-1], price=item['price'], additional_specs=item['additional_specs'])
    if response:
        result = {"name": item['name'][:-1], "price": item["price"], "gaming": response["gaming"], "work": response["work"], "casual": response["casual"], "school": response["school"], "storage_size": response["storage size"], "battery_life": response["battery life"], "ethernet_port": response["ethernet port"], "hdmi_port": response["hdmi port"], "screen_resolution": response["screen resolution"], "keyboard_backlight": response["keyboard backlight"], "weight": response["weight"], "store_name": item["store_name"], "additional_specs": item["additional_specs"]}
        print(result)
        result_all.append(result)

with open(f'files/categorized_topic.json', 'w', encoding='utf-8') as f:
    json.dump(result_all, f, ensure_ascii=False, indent=4)