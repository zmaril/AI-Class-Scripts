import random
import curses 
from curses.ascii import isdigit 
import nltk 
from nltk.corpus import cmudict 

d = cmudict.dict() 
fives = []
sevens= [] 

def numberOfSyllables(word): 
    if word.lower() in d:
        return max([len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]])
    else:return 100

def process():
    for title  in ["pride"]: 
        text = open(title+".txt").read()
        filtered = filter(lambda letter: not letter in ";,'\"\r\n",text)
        sentences=filtered.replace("Mr.","Mr").replace("Mrs.","Mrs").split(".")
        for sentence in sentences:
            words = sentence.split(" ")
            if len(words) <8:
                sylla= sum(map(numberOfSyllables,words))
                if sylla==5:
                    fives.append(sentence)
                if sylla==7:
                    sevens.append(sentence)
def newHaiku():
    i,j,k = random.randint(0,len(fives)-1),random.randint(0,len(sevens)-1),random.randint(0,len(fives)-1)
    while len(fives)>1 and k==i: k=random.randint(0,len(fives)-1)
    print fives[i]
    print sevens[j]
    print fives[k]

process()
newHaiku()


#Nana was frigid
#He took her hand and soothed her
#Go said she simply
