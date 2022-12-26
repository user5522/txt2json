import argparse
import json
import os

def read_text_lines(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()

def write_json_lines(data, file):
    with open(file, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='the input text file')
    parser.add_argument('output_file', help='the output JSON file')
    parser.add_argument('--key1', required=True, help='the first key to use for the dictionaries in the output data')
    parser.add_argument('--key2', help='the second key to use for the dictionaries in the output data')
    parser.add_argument('--value2', default=None, help='the value for the second key in the dictionaries in the output data')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: input file {args.input_file} not found')
        exit(1)

    if os.path.exists(args.output_file):
        response = input(f'Output file {args.output_file} already exists. Overwrite it? (y/n) ')
        if response.lower() != 'y':
            print('Aborting')
            exit(1)

    data = []
    for line in read_text_lines(args.input_file):
        item = {
            args.key1: line
        }
        if args.key2 is not None:
            item[args.key2] = args.value2
        data.append(item)

    with open(args.output_file, 'w') as f:
        json.dump(data, f, indent=2)
