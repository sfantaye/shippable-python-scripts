# tests/test_convert_csv_to_json.py
#This test:
#Creates a temp CSV file with sample data.
#Converts it to JSON using your script.
#Loads the JSON and checks the data is as expected.
#Cleans up temporary files after testing.

import os
import json
import tempfile
import csv
import pytest
from scripts.general.convert_csv_to_json import convert_csv_to_json

@pytest.fixture
def sample_csv_data():
    data = [
        {"name": "Alice", "age": "30"},
        {"name": "Bob", "age": "25"}
    ]
    with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)
        f.seek(0)
        yield f.name
    os.remove(f.name)

def test_convert_csv_to_json(sample_csv_data):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        output_json_path = f.name

    try:
        convert_csv_to_json(sample_csv_data, output_json_path)

        with open(output_json_path, 'r') as f:
            json_data = json.load(f)

        assert isinstance(json_data, list)
        assert json_data[0]["name"] == "Alice"
        assert json_data[1]["age"] == "25"
    finally:
        os.remove(output_json_path)
