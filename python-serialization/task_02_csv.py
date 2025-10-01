#!/usr/bin/env python3
"""
reading data from one format (CSV) and converting it 
into another format (JSON) using serialization techniques
"""

import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """Convert a CSV file into JSON format and save it as data.json"""
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
