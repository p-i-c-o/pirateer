# ┌──────────────────────────────────┐
# │ This code was created by p-i-c-o │
# │ GitHub:   www.github.com/p-i-c-o │
# │                                  │
# │ No referral is required!         │
# │ This was created for the world.  │
# └──────────────────────────────────┘

# ------------------------- IMPORTS -------------------------

import os
import subprocess
import re
import json
import colorama

from rich.console import Console
from rich.table import Table

from colorama import Fore, Back, Style

# ------------------------ FUNCTIONS ------------------------

console = Console()

def run(command):
  result = subprocess.run(command, shell=True, capture_output=True, text=True)
  return result.stdout

def parse(torrent_data):
    # Split the data into lines
    lines = torrent_data.strip().split('\n')

    # Define the keys for the dictionary
    keys = ["added", "id", "leechers", "name", "seeders", "size", "status", "username"]

    # Initialize an empty list to store dictionaries
    torrent_list = []

    # Iterate through lines and convert each entry to a dictionary
    for line in lines[2:]:
        # Use regular expression to extract values
        values = re.split(r'\s+\|\s+', line)
        # Create a dictionary by zipping keys and values
        torrent_dict = dict(zip(keys, values))
        # Append the dictionary to the list
        torrent_list.append(torrent_dict)

    return torrent_list

def search(term):
  return parse(run(f'piratebay search {term}'))

def DictToTable(data):
    console = Console()

    if not data:
        console.print("No data to display.")
        return

    # Create a table
    table = Table(title="Torrent Information")

    # Define columns for the table based on the keys of the first dictionary
    columns = list(data[0].keys())

    # Add columns to the table
    for column_name in columns:
        table.add_column(column_name.capitalize())  # Capitalize the column names for display

    # Add rows to the table
    for item in data:
        row_data = [str(item[key]).strip() for key in columns]
        table.add_row(*row_data)

    # Print the table
    return table

def remove_keys(data_list, keys_to_remove):
    for data_dict in data_list:
        for key in keys_to_remove:
            data_dict.pop(key, None)
    return data_list

# ------------------------ MAIN CODE ------------------------

output = search('shawshank')

coutput = remove_keys(output, ["added", "leechers"])
output1 = DictToTable(coutput[:5])
console.print(output1)


#print(json.dumps(output, indent=2))
