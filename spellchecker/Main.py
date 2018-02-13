# -*- coding: utf-8 -*-

from spellchecker.Dictionary import Dictionary

#If a word is unknown, ask the user what to do with it
#The user can accept the word, ignore it or replace it
def consultUser(currentWord, mainDict, ignored):
    print("A palavra "+currentWord+" é desconhecida. O que você deseja fazer?")
    print("1 - Adicionar a palavra ao dicionário")
    print("2 - Ignorar a palavra")
    print("3 - Substituir a palavra por outra")
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        mainDict.add(currentWord)
        return currentWord
    if opcao == 2:
        ignored.add(currentWord)
        return currentWord
    if opcao == 3:
        newWord = input("Insira a nova palavra: ")
        return newWord
       
       
#Copy all words and punctuation from the input document to the output document
#but ask the user what to do with any words that are unknown        
def processDocument(mainDict, ignored):
    try:
        inDoc = open('in.txt', 'r')
        outDoc = open('out.txt', 'w')
    except:
        print("Problema ao abrir o arquivo!")
    words = inDoc.readlines()
    for line in words:
        for currentWord in line.split():
            if not mainDict.contains(currentWord.lower()) and not ignored.contains(currentWord.lower()):
                currentWord = consultUser(currentWord.lower(), mainDict, ignored)
            outDoc.write(currentWord+" ")
    inDoc.close()
    outDoc.close()        
    print("Verificação ortográfica finalizada com sucesso!")    
        

#Main function
if __name__ == '__main__':
    mainDict = Dictionary()
    ignored = Dictionary()
    try:
        mainDict.load('main-dict.txt')
        processDocument(mainDict, ignored)
        mainDict.save('main-dict.txt')
    except:
        print("Erro!")
    