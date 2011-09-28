#class book(Id,ASIN,title,group,salesrank):
import re    
rawdata = open("amazon-meta.txt")
rawbooks = rawdata.read()
#books = rawbooks.split("\r\n\r\n")
#bookdata= []

clean = rawbooks[0:100000].replace("\r"," ").replace("\n"," ").replace("|"," ").replace(":"," ")
words = clean
for reg in ["\d{4}-\d{1,2}-\d{1,2}","[A-Z1-9]{3,}","\d+","\[","\]"]: #Regexp are a pain in the butt
            words = re.sub(reg,"",words)
words = words.split(" ")


freqWords = {}
# #for word in words:
#     if word in freqWords:
#         freqWords[word] = freqWords[word]+1
#     else:
#         freqWords[word]=1

def checkDict(wordDict,word):
    if word in wordDict:
        wordDict[word]+=1
    else:
        wordDict[word]=1
    return wordDict
    
newFreq= reduce(checkDict,words,{})

wordTuples = [(newFreq[key],key) for key in newFreq.keys()] 
wordTuples.sort()
reversed = [ (x,y) for (y,x) in wordTuples]
exist = filter(lambda x: len(x[0]) > 0, reversed)





