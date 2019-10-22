import random, os, shutil
# l = os.listdir('./clothing')
# random.shuffle(l)

# print(len(l))
# for i in range(30000):
    # if (not ("train" in l[i]) and not ("test" in l[i])):
        # shutil.move('./clothing/' + l[i], './clothing/train/' + l[i])

# for i in range(30001, 44444):
    # if (not ("train" in l[i]) and not ("test" in l[i])):
        # shutil.move('./clothing/' + l[i], './clothing/test/' + l[i])

# print(l[0:4])


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

train_cifar = getListOfFiles("./train")
test_cifar = getListOfFiles("./test")

# for x in train_cifar:
    # print('./not_clothing/train/' + x.split("/")[-2] + x.split("/")[-1])
    # shutil.move(x, './not_clothing/train/' + x.split("/")[-2] + x.split("/")[-1])

for x in test_cifar:
    # print('./not_clothing/train/' + x.split("/")[-2] + x.split("/")[-1])
    shutil.move(x, './not_clothing/test/' + x.split("/")[-2] + x.split("/")[-1])

# print(len(train_cifar))
# print(train_cifar[0].split("/"))
