import pickle


def saveDictToFile(filepath):
    file = open(filepath, "rb")
    dictionary = pickle.load(file)
    file.close()
    return dictionary

def createLineByLineDict(dictionary,filepath):
    print(len(dictionary.keys()))
    for i in dictionary.keys():
        try:
            key =  i.replace('\"','')
            file = open(filepath+key, 'w', encoding='utf8')
            definition = str(dictionary[i])
            definition = definition.replace('"','')
            file.write(definition)
            file.close()
        except(OSError):
            print('OSerror')


if __name__ == '__main__':
    createLineByLineDict(saveDictToFile('animalDictionary.txt'),'AnimalFiles/')
