import os


def importFile(path,delimiter):
    animalDatabase = []
    file = open(path, 'r',encoding = 'utf8')
    for i in file:
        animalDatabase = i.split(delimiter)
    file.close()
    return animalDatabase

def importAnimalNames(filepath):
    files = os.walk(filepath)
    animalNames = []
    for i in files:
        animalNames.append(i[2])
    return animalNames[0]

if __name__ == '__main__':
    print(len(importFile('animalDatabase.txt','#')))
    print(len(importAnimalNames('Summaries')))