import json
import os
import sys
import uuid

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('add parameter to folder with json files to merge')
    directory = sys.argv[1]
    print(f'merging json files in directory {directory}...')
    results = []
    for filename in sorted(os.listdir(directory),
                           key=lambda x: os.path.getmtime(directory+os.sep+x)):
        if filename.endswith('.json'):
            with open(directory+os.sep+filename, encoding='utf-8') as f:
                data = json.load(f)
                print(f'processed file {filename} ({len(data)} entities)')
                results.extend(data)

    directory_up = os.path.dirname(directory)
    directory_with_files_to_merge = os.path.basename(os.path.normpath(directory))
    merged_filename = f'{directory_up}{os.sep}merged-' \
                      f'{directory_with_files_to_merge}-{uuid.uuid1()}.json'
    with open(merged_filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        print(f'merged data dumped to file {merged_filename} ({len(results)} entities)')
