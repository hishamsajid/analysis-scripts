import pandas as pn
from nltk import word_tokenize
from nltk import pos_tag 
from nltk import ne_chunk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
import csv
import sys
import string

reload(sys)
sys.setdefaultencoding('latin-1')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
stop_words.update(['@','>','<','.',',','-','=','(',')','[',']','/','\\','?','_',
'Hey','How','Does','AND','Has','`','Can','Could','First','Would'])

#logs = pn.read_csv('logs_enhanced.csv',encoding='latin-1')
#logs2 = pn.read_csv("logs.csv",encoding ='latin-1')

logs_filtered = pn.read_csv('logs_filtered.csv', encoding = 'latin-1', engine='python')

#questions in adobe-analytics
#vector = logs.loc[(logs['num_questions'] > 0) & (logs['channel'] == 'adobe-analytics (C03AFUKHC)'), 'message_utf8']
#print len(vector)
#messages in adobe-analytics
#vector = logs.loc[(logs['channel'] == 'adobe-analytics (C03AFUKHC)'), 'message_utf8']

#questions in google-analytics
#vector = logs.loc[(logs['num_questions'] > 0) & (logs['channel'] == 'google-analytics (C03AE85U5)'), 'message_utf8']
#print len(vector)
#vector = logs.loc[(logs['num_questions'] > 0) & (logs['channel'] == 'measure (C031USB3Z)'), 'users']

#vector = logs.loc[(logs['num_questions'] > 0) & (logs['channel'] == 'adobe-dtm (C2PN1PYA2)'), 'users']

#vector = logs.loc[(logs['num_questions'] > 0) & (logs['channel'] == 'lobby-bar (C031USB41)'), 'message_utf8']

#messages in measure
#vector = logs.loc[(logs['channel'] == 'measure (C031USB3Z)'), 'message_utf8']

#messages in women-in-analytics (C20HQRV9V)
#vector = logs.loc[logs['channel'] == 'women-in-analytics (C20HQRV9V)','message_utf8']

#messages in conferences channel
#vector = logs.loc[logs['channel'] == 'conferences (C03A92FM6)','message_utf8']

#questions w.r.t channel




#print vector

#all messages
#vector = logs['message_utf8']

#all filtered messages
vector = logs_filtered['message_utf8']

#messages in which questions were asked
#vector = logs.loc[(logs['num_questions'] > 0), 'message_utf8']




tg_list = []
itr = 0
for item in vector.iteritems():
    #when .loc and iloc used
    #tokenized_item = word_tokenize(item[1])
    #print type(item)
    #print type(item[1])
    print itr
    try:
        tokenized_item = word_tokenize(item[1])
    except TypeError:
        pass
    #tokenized_item = word_tokenize(item[1])
    stemmed_lemmatized_list = []
    for word in tokenized_item:
        lemmatized_item = lemmatizer.lemmatize(word)
        #UNCOMMENT IF STEMMING IS TO BE APPLIED
        #stemmed_item = stemmer.stem(lemmatized_item)
        stemmed_lemmatized_list.append(lemmatized_item)
   
    filtered_item = [items for items in stemmed_lemmatized_list if not items in stop_words]
    #print filtered_item
    pos_item = pos_tag(filtered_item)
    tg_item_tree = ne_chunk(pos_item)
    tree_leaves = tg_item_tree.leaves()
    itr1 = 0

    while(itr1 < len(tree_leaves)):
     
       if(tree_leaves[itr1][1] == 'NNP'):
            item = tree_leaves[itr1][0]
            tg_list.append(item)
            
       itr1 += 1

    itr +=1
    #UNCOMMENT FOR TESTING ON LIMITED NUMBER OF ITEMS:
    #if(itr == 10):
    #    break
    
most_common = [item for item in Counter(tg_list).most_common()]
print itr
print(str(most_common))

#UNCOMMENT WHEN SAVING CSV
with open('most_common_terms_after_outlier_removal.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(most_common)



