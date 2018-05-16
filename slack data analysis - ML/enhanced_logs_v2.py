import pandas as pn
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import SpaceTokenizer
from nltk.corpus import stopwords
import numpy as np
from nltk.stem import WordNetLemmatizer
from collections import Counter
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

lemmatizer = WordNetLemmatizer()
logs = pn.read_csv("logs_enhanced.csv",encoding='latin-1')

#messages = logs['message_utf8']['num_questions' > 0]

messages = logs.loc[logs['num_questions'] > 0, 'message_utf8'].iloc[0]
message2 = logs.loc[logs['num_questions'] > 0, 'message_utf8'].iloc[1]
messagesx = logs.loc[logs['num_questions'] > 0, 'message_utf8']
print type(messagesx)


for index in messagesx.iteritems():
    print index[1]
#print messages
#print message2
#print messages[0] + '\n' + messages[1]
#ml = len(messages)
#print ml
#34467
itr = 0

tokenized_stopless_messages = []
tokenizer = SpaceTokenizer()
stop_words = set(stopwords.words("english"))
#adding more stop_words based on initial analysis
stop_words.update(['new','use','would','-','using'])
#print stop_words


while(itr<100):
   try:

       if(messages[itr][0:1] == "`"):
          itr += 1
          #print "code found at: " + itr
       else:
           lowercased = messages[itr].lower()
           lemmatized_lowercased = lemmatizer.lemmatize(lowercased)
           tokenized = tokenizer.tokenize(lowercased)
           filtered_sentence = [words for words in tokenized if not words in stop_words]
           tokenized_stopless_messages.append(filtered_sentence)
           #print "filtered_sentence added"

           #tokenized_messages.append(tokenizer.tokenize(messages[itr]))
           itr += 1
           #print itr
   except TypeError:
       #print "Skipped"
       itr += 1
       #print itr

       #print itr
       #error after 1741

#print tokenized_messages[0]
#np_array = np.array(tokenized_stopless_messages)

#flattened_array = np_array.flatten()
flattened_list = sum(tokenized_stopless_messages,[])

#print flattened_list

most_common_words= [word for word, word_count in Counter(flattened_list).most_common(10)]
#print str(most_common_words)
#print tokenized_stopless_messages
#print flattened_array




#eg_string = "This is a sample sentence, showing off the stop words filtration."
#print eg_string[0:2]

#tokenizer = SpaceTokenizer()
#word_tokens = tokenizer.tokenize(eg_string)
#print word_tokens


#filtered_sentence = [words for words in word_tokens if not words in stop_words]

#filtered_sentence2 = [words for words in tokenized_messages[1] if not words in stop_words]

#print filtered_sentence2

#print filtered_sentence + "\n message1: " + filtered_sentence2