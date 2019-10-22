import random, os, shutil
# l = os.listdir('./clothing')
# random.shuffle(l)

# print(len(l))
# for i in range(35000):
    # if (not ("train" in l[i]) and not ("test" in l[i])):
        # shutil.move('./clothing/' + l[i], './train/clothing/' + l[i])

# for i in range(35001, 44442):
    # if (not ("train" in l[i]) and not ("test" in l[i])):
        # shutil.move('./clothing/' + l[i], './test/clothing/' + l[i])


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

# train_cifar = getListOfFiles("./train_cf")
test_cifar = getListOfFiles("./test_cf")

# for x in train_cifar:
    # shutil.move(x, './train/other/' + x.split("/")[-2] + x.split("/")[-1])

for x in test_cifar:
    shutil.move(x, './test/other/' + x.split("/")[-2] + x.split("/")[-1])

