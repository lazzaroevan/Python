from mediawiki import MediaWiki
from mediawiki import DisambiguationError
import threading
import pickle
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
def getData(checkForReptile,animalDict,breakout,threadIncrement):
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
                    animalDict[firstWord] = [(tempTitle,childPage.summary,childPage.images)]
                else:
                    animalDict[firstWord].append((tempTitle,childPage.summary,childPage.images))
        except(DisambiguationError):
            print('Disambiguation Error')

        if threadIncrement == 0:
            break
        else:
            threadIncrement -= 1
        currentSize += 1
        if(currentSize%100 == 0):
            print(currentSize,'/',threadIncrement,sep='')

if __name__ == '__main__':
    #getListOfAnimals('Animals','animalDatabase.txt','#')
    animalDatabase = importFile('animalDatabase.txt','#')
    arrayOfThreads =[]
    animalDict = {}
    threadIncrement = len(animalDatabase)//10
    for i in range(10):
        thread = threading.Thread(target=getData, args=(animalDatabase,animalDict,i*threadIncrement,threadIncrement))
        arrayOfThreads.append(thread)
        thread.start()
    for i in arrayOfThreads:
        i.join()
    count = 0
    for i in animalDict.keys():
        count += len(animalDict[i])
    print(count)
    saveDictToFile(animalDict,"animalDictionary.txt")