import os
files = [i for i in os.listdir() if i.endswith('.txt')]
files.sort()
len_strings = []
dct = {}
with open(r'all_files.txt','wt') as f:
    for file in files:
        strings = open(file, encoding='utf-8').readlines()
        dct[len(strings)] = file
        len_strings.append(len(strings))
        len_strings.sort()
    for len_ in len_strings:
        files_sorted = dct.setdefault(len_)
        file_sorted_strings = open(files_sorted, encoding='utf-8').read()
        f.write(f'{files_sorted}\n{len_}\n')
        f.write(file_sorted_strings)
        f.write('\n')