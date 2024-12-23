from lab6.utils import  *


import os , sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def phone_book(data):
    book = {}
    results = []

    for command in data:
        if command[0] == "add":
            number, name = command[1], command[2]
            book[number] = name
        elif command[0] == "del":
            number = command[1]
            book.pop(number, None)
        elif command[0] == "find":
            number = command[1]
            results.append(book.get(number, "not found"))
    return results


def main():
    write(end='')
    array = read(type_convert=str)
    result = phone_book(array)
    for line in result:
        write(line, to_end=True)


if __name__ == '__main__':
    main()
