class WordSet(object):
    
    #Construct an empty set of words
    def __init__(self):
        self.words = []
    
    #Make wd a member of this set of words
    def add(self, wd):
        self.words.append(wd)
    
    #Return true if and only if wd is a member of this set of words
    def contains(self, wd):
        return self.words.__contains__(wd) 