import csv
import json
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('add parameter json file to be converted to csv')
    file_path = sys.argv[1]
    print(f'converting json file {file_path}...')

    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

        abs_file_path = os.path.abspath(file_path)
        directory = os.path.dirname(abs_file_path)
        filename = os.path.basename(abs_file_path)
        name, _ = os.path.splitext(filename)
        extension = '.csv'

        with open(directory+os.sep+name+extension, 'w', encoding='utf-8', newline='') as csv_f:
            fieldnames = ['nazwisko', 'data_ur', 'info', 'scan_link', 'created_utc']
            writer = csv.DictWriter(csv_f, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(data)
            print(f'converted to file {name+extension}')
