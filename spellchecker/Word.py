class Word(object):
    
    #Each Word object is a single word.
    
    def __init__(self):
        self.word = ""
        
    def getWord(self, inDoc):
        words = inDoc.readlines()
        for line in words:
            for self.word in line.split():
                return self.word
    
    def putWord(self, outDoc, wd):
        outDoc.write(wd+" ")
        