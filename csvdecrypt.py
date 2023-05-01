import csv
import json

output_format = input("Choose output format (1 for text, 2 for JSON): ")

# Open the CSV file
with open('passwords.csv') as csv_file:
    # Read the CSV file into a dictionary
    reader = csv.DictReader(csv_file)
    # Convert the dictionary into a list of dictionaries
    data = [row for row in reader]

# Write the data to a file in the chosen format
if output_format == '1':
    # Write the data to a text file
    with open('passwords.txt', 'w') as txt_file:
        for row in data:
            txt_file.write(f"{row['username']}: {row['password']}\n")
    print("Data written to passwords.txt")
elif output_format == '2':
    # Write the data to a JSON file
    with open('passwords.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data written to passwords.json")
else:
    print("Invalid output format. Choose 1 for text or 2 for JSON.")
