import random

# Thanks Jordan! http://groups.google.com/group/nltk-users/browse_thread/thread/9823a1feeed5f3f2/81e70cb6704dc01e
import curses 
from curses.ascii import isdigit 

import nltk 
from nltk.corpus import cmudict 

d = cmudict.dict() 

def nsyl(word): 
    if word.lower() in d:
        possy = [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]] 
        ### Just one way to deal with the list of numbers that are returned back.
        return max(possy)
    else:
        return 100

fives = []
sevens= [] 

def process():
    for title in ["pride"]: #["sense","pride","zola","flatland"]: #Just Zola seems to provide the most Zen haikus. 
        text = open(title+".txt").read()
        filtered = filter(lambda letter: not letter in ";,'\"\r\n",text)
        sentences=filtered.replace("Mr.","Mr").replace("Mrs.","Mrs").split(".")
        for sentence in sentences:
            words = sentence.split(" ")
            if len(words) <8:
                sylla= sum(map(nsyl,words))
                if sylla==5:
                    fives.append(sentence)
                if sylla==7:
                    sevens.append(sentence)
def newHaiku():
    i = random.randint(0,len(fives)-1)
    j = random.randint(0,len(sevens)-1)
    k = random.randint(0,len(fives)-1)
    while len(fives)>1 and k==i:
        k=random.randint(0,len(fives)-1)
    
    print fives[i]
    print sevens[j]
    print fives[k]

process()
newHaiku()
