import pandas as pn
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import SpaceTokenizer
from nltk.corpus import stopwords
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

logs = pn.read_csv("logs_enhanced.csv",encoding='latin-1')

messages = logs['message_utf8']

print messages[0] + '\n' + messages[1]
ml = len(messages)
print ml
#34467
itr = 0

tokenized_messages = []
tokenizer = SpaceTokenizer()

while(itr<10):
   try:

       if(messages[itr][0:1] == "`"):
          itr += 1
          print "code found"
       else:
           tokenized_messages.append(tokenizer.tokenize(messages[itr]))
           itr += 1
           print itr
   except TypeError:
       print "Skipped"
       itr += 1
       print itr

       #print itr
       #error after 1741

print tokenized_messages[0]

eg_string = "This is a sample sentence, showing off the stop words filtration."
print eg_string[0:2]

#tokenizer = SpaceTokenizer()
word_tokens = tokenizer.tokenize(eg_string)
#print word_tokens

stop_words = set(stopwords.words("english"))

filtered_sentence = [words for words in word_tokens if not words in stop_words]

filtered_sentence2 = [words for words in tokenized_messages[1] if not words in stop_words]

print filtered_sentence2

#print filtered_sentence + "\n message1: " + filtered_sentence2