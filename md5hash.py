def md5_convert():
    import hashlib

    file_path = input('Введите адрес файла: \n')
    with open(file_path, 'rt', encoding='UTF-8') as f:
        lines = f.read().split('\n')
        lines1 = (hashlib.md5(line.encode()) for line in lines)
        for line in lines1:
            print(line.hexdigest())
    return


def upload_lines(file_path: str):

    with open(file_path, 'rt', encoding='UTF-8') as f:
        for lines in f.read().split('\n'):
            yield lines


def md5_conv(file_path: str):
    import hashlib
    for lines in upload_lines(file_path):
        line = hashlib.md5(lines.encode())
        print(line.hexdigest())


if __name__ == '__main__':
    md5_conv('wiki_country.txt')
    md5_convert()











