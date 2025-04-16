import csv
import json
import argparse

def convert_csv_to_json(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('--input', required=True, help='Path to input CSV')
    parser.add_argument('--output', required=True, help='Path to output JSON')
    args = parser.parse_args()
    convert_csv_to_json(args.input, args.output)
