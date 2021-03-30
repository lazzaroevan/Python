import pickle
import os

import requests


def loadDict(filepath):
    file = open(filepath, "rb")
    dictionary = pickle.load(file)
    file.close()
    return dictionary
def imageGrabber(listOfNamesPath,directory):
    listOfNames = []
    file = open(listOfNamesPath,'r',encoding='utf8')
    for i in file:
        listOfNames.append(i.split('#'))
    for i in listOfNames:
        file = open(directory+i,'rb')
        tempList = pickle.load(file)
        print(tempList)
#       urlList =
#       r = requests.get(,stream = True)
#       if r.status_code == 200:
#           r.raw.decode_content = True
#           imageFile = open('images/','wb')

def createLineByLineDict(dictionary,filepath):
    print(len(dictionary.keys()))
    count = 0
    for i in dictionary.keys():
        try:
            key =  i.replace('\"','')
            file = open(filepath+key, 'wb')
            definition = (dictionary[i])
            pickle.dump(definition,file)
            file.close()
        except(OSError):
            print('OSerror')
            count += 1
    print(count)

def creatListofAnimalsFirstName(filepath,newFilepath):
    files = os.walk(filepath)
    file = open(newFilepath,'w',encoding= 'utf8')
    list = []
    for i in files:
        for a in (i[2]):
            list.append(a)
#            file.write(a)
#            file.write('\n')
    file.close()
    print(len(list))

if __name__ == '__main__':
    #createLineByLineDict(loadDict('animalDictionary.txt'),'AnimalFiles/')
    #creatListofAnimalsFirstName('AnimalFiles/','animalNames.txt')
    imageGrabber('animalDatabase.txt','Images/')
