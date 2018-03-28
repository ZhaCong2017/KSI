import hashlib
import argparse
import KSI_make

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="input the number of file", type=int, dest='num')
    parser.add_argument('-p', help="input the path of file", dest='path')
    args = parser.parse_args()
    filePath = args.path
    num = args.num
    num -= 1
    Key_hash = KSI_make.readFile(filePath)
    # print(Key_hash)

    hashlist = []
    file = open('KSI.txt', 'r')
    for line in file:
        hashlist.append(line.split(' ')[: -1])
    file.close()
    # print(hashlist)

    i = 0
    while i < len(hashlist) - 1:
        if num % 2 == 0:
            Key_hash = hashlib.sha256((Key_hash + hashlist[i][num + 1]).encode('utf-8')).hexdigest()
        else:
            Key_hash = hashlib.sha256((hashlist[i][num - 1] + Key_hash).encode('utf-8')).hexdigest()
        i += 1
        num = int(num / 2)

    print(Key_hash)
    if Key_hash == hashlist[len(hashlist) - 1][0]:
        print("True")
    else:
        print("False")

