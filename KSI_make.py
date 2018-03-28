import hashlib
import os


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    hashlist = []
    hashlist.append([])
    for allDir in pathDir:
        child = os.path.join('%s\\\\%s' % (filepath, allDir))
        # print(child)
        hashlist[0].append(readFile(child))

    KSIBuild(hashlist)
    return hashlist


def readFile(filename):
    f = open(filename, 'rb')

    hash = hashlib.sha256()
    hash.update(f.read())
    return hash.hexdigest()


def KSIBuild(hashlist):
    # print(hashlist)
    le = len(hashlist)
    if len(hashlist[le - 1]) == 1:
        return
    if len(hashlist[le - 1]) % 2 != 0:
        hashlist[le - 1].append("123")
    hashlist.append([])

    i = 0
    while i < len(hashlist[le - 1]):
        hash = hashlib.sha256((hashlist[le - 1][i] + hashlist[le - 1][i + 1]).encode('utf-8')).hexdigest()
        hashlist[le].append(hash)
        i += 2

    KSIBuild(hashlist)


if __name__ == "__main__":
    filePath = "C:\\Users\\79499\\Desktop\\python\\KSI\\test"
    hashlist = eachFile(filePath)
    file = open('KSI.txt', 'w')
    for x in hashlist:
        for y in x:
            file.write(str(y) + ' ')
        file.write('\n')
    file.close()
    print("KSI has been build")
