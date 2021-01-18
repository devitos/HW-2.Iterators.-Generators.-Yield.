def md_5conv(path):
    import hashlib
    with open(path) as file:
        for lines in file:
            line = hashlib.md5(lines.encode())
            yield line.hexdigest()


if __name__ == '__main__':

    for item in md_5conv('wiki_country.txt'):
        print(item)
