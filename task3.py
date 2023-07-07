def open_read_files():
    name_list = ['1.txt', '2.txt', '3.txt']
    common_dict = {}
    for i in name_list:
        with open(i) as f:
            file = f.readlines()
            common_dict[str(len(file))] = i
    return sorted(common_dict.items())

def write_file(dict):
    with open('result.txt', 'w') as f:
        for d in dict:
            with open(d[1]) as file:

                f.write(f'{d[1]}\n')
                f.write(f'{d[0]}\n')
                f.write(f'{file.read()}\n')


open_read_files()
write_file(open_read_files())
