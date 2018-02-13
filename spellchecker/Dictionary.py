class Dictionary(object):
    
    #Construct an empty dictionary
    def __init__(self):
        self.dict = []
    
    #Load this dictionary from filename
    def load(self, filename):
        fileDic = open(filename, 'r')
        linhas = fileDic.readlines()
        for wd in linhas:
            self.dict.append(wd)  
        
    #Save this dictionary to filename    
    def save(self, filename):
        self.dict.sort()
        fileDic = open(filename, 'w')
        for wd in self.dict:
            fileDic.write(wd)
            
    #Check if a word wd is in this dictionary        
    def contains(self, wd):
        for line in self.dict:
            if wd in line:
                return True

    #Add a word wd to this dictionary            
    def add(self, wd):
        self.dict.append(wd+"\n")
        
        
