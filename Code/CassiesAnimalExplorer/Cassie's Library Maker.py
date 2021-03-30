import shutil

import requests
from mediawiki import MediaWiki
from mediawiki import DisambiguationError
import threading
import pickle
import os
wikipedia = MediaWiki()

def getListOfAnimals(title,path,delimiter):
    p = wikipedia.page(title)
    checkForReptile = p.backlinks
    file = open(path,'w',encoding = 'utf8')
    try:
        for i in checkForReptile:
            file.write(i)
            file.write(delimiter)
    except(UnicodeDecodeError):
        print('continue')
    file.close()

def importFile(path,delimiter):
    animalDatabase = []
    file = open(path, 'r',encoding = 'utf8')
    for i in file:
        animalDatabase = i.split(delimiter)
        print(len(animalDatabase))
    file.close()
    return animalDatabase
def saveDictToFile(dict,filepath):
    file = open(filepath, "wb")
    pickle.dump(dict, file)
    file.close()
def getData(checkForReptile,animalDict,breakout,threadIncrement,errors):
    finalSize = len(checkForReptile)
    currentSize = 0
    for i in checkForReptile[breakout:breakout+threadIncrement]:
        try:
            childPage = wikipedia.page(i)
            if(childPage != None):
                tempTitle = childPage.title
                if ' ' in tempTitle:
                    firstWord = tempTitle[0:tempTitle.find(' ')]
                else:
                    firstWord = tempTitle
                if firstWord not in animalDict:
                    animalDict[firstWord] = [tempTitle]
                else:
                    animalDict[firstWord].append(tempTitle)
                os.mkdir(os.getcwd()+'/Images/' + tempTitle)
                file = open('Summaries/'+ tempTitle,'w',encoding='utf8')
                file.write(childPage.summary)
                file.close()
                for i in childPage.images:
                    filename = i.split("/")[-1]
                    r = requests.get(i, stream=True)
                    if r.status_code == 200:
                        r.raw.decode_content = True
                        with open(os.getcwd()+'/Images/' + tempTitle+ '/' + filename, 'wb') as f:
                            shutil.copyfileobj(r.raw, f)
                    else:
                       errors[0] += 1
        except(DisambiguationError,FileExistsError):
            errors[0] += 1
        if threadIncrement == 0:
            break
        else:
            threadIncrement -= 1
        currentSize += 1
        if(currentSize%100 == 0):
            print(currentSize,'/',threadIncrement,sep='',end='')
            print('Errors:',errors[0])

if __name__ == '__main__':
    #getListOfAnimals('Animals','animalDatabase.txt','#')
    animalDatabase = importFile('animalDatabase.txt','#')
    arrayOfThreads =[]
    animalDict = {}
    threadIncrement = len(animalDatabase)//13
    errors = [0]
    for i in range(13):
        thread = threading.Thread(target=getData, args=(animalDatabase,animalDict,i*threadIncrement,threadIncrement,errors))
        arrayOfThreads.append(thread)
        thread.start()
    for i in arrayOfThreads:
        i.join()
    count = 0
    for i in animalDict.keys():
        count += len(animalDict[i])
    print(count)
    saveDictToFile(animalDict,"animalDictionary.txt")