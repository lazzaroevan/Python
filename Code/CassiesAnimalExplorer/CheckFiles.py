import os
from PIL import Image, UnidentifiedImageError


#Use this file to check the number of names in animalDatabase.txt vs the number of files in the summaries folder



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

def removeUnsupportedPictures():
    numberOfImagesDeleted = 0
    numberOfImagesGoneThrough = 0
    for b in importAnimalNames('Summaries'):
        imageDirectoryPath = os.getcwd()+'/'+"Images/"+b
        for i in os.walk(imageDirectoryPath):
            for a in i[2]:
                try:
                    try:
                        imagePath = imageDirectoryPath +'/'+a
                        if('Red_Pencil_Icon.png' not in a):
                            #note, resizing the images takes up alot of time and memory, causes long load times
                            imageToResize = Image.open(imagePath)
                            imageToResize = imageToResize.resize((round(imageToResize.size[0] * (.5)), (round(imageToResize.size[1] * (.5)))))
                        else:
                            os.remove(imagePath)
                            numberOfImagesDeleted +=1
                    except(UnidentifiedImageError,OSError):
                        os.remove(imagePath)
                        numberOfImagesDeleted += 1
                except(Exception):
                        print('Exception')
                numberOfImagesGoneThrough += 1
        if(numberOfImagesGoneThrough%1000 == 0):print("Images Deleted:",numberOfImagesDeleted,'   Images Gone Through:',numberOfImagesGoneThrough)

if __name__ == '__main__':
    #print(len(importFile('animalDatabase.txt','#')))
    #print(len(importAnimalNames('Summaries')))
    removeUnsupportedPictures()