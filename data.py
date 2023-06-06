import json
import csv

# Specify the path to the input JSON file
input_json_file = '/Users/apple/Documents/Projects/News/News_Category_Dataset_v3.json'

# Specify the path to the output CSV file
output_csv_file = 'output.csv'

# Open the input JSON file
with open(input_json_file, 'r') as json_file:
    # Initialize an empty list to store the JSON objects
    json_data = []

    # Read each line in the JSON file
    for line in json_file:
        # Load the JSON data from the line
        json_obj = json.loads(line)
        
        # Append the JSON object to the list
        json_data.append(json_obj)

# Extract the keys from the first JSON object to use as column headers
column_headers = list(json_data[0].keys())

# Open the output CSV file in write mode
with open(output_csv_file, 'w', newline='') as csv_file:
    # Create a CSV writer
    writer = csv.DictWriter(csv_file, fieldnames=column_headers)

    # Write the column headers to the CSV file
    writer.writeheader()

    # Write each JSON object as a row in the CSV file
    writer.writerows(json_data)

print
