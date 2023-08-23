#!/usr/bin/env python3
import argparse

def open_file(file_name):
    with open(file_name,'r') as file:
        file_contents = file.readlines()
        return file_contents

def remove_duplicates_from_list(lines_list):
    unique_list = []
    for line in lines_list:
        if line not in unique_list:
            unique_list.append(line)
    return unique_list

def combine_files(file_list):
    all_lines = []
    for file_name in file_list:
        all_lines.extend(open_file(file_name))
    return all_lines

def save_to_file(new_list, output_file_name):
    with open(output_file_name, 'w') as file:
        for line in new_list:
            file.write(line)

def main():
    parser = argparse.ArgumentParser(description="Remove linhas duplicadas de um ou mais arquivos e salva em um novo arquivo.")
    parser.add_argument('files', metavar='F', type=str, nargs='+', help='uma lista de arquivos para processar')
    parser.add_argument('-o', '--output', help='caminho e nome do arquivo de saída', required=True)

    args = parser.parse_args()

    all_lines = combine_files(args.files)
    unique_lines = remove_duplicates_from_list(all_lines)

    save_to_file(unique_lines, args.output)
    print(f"Lista sem duplicatas salva em {args.output}!")

if __name__ == '__main__':
    main()
