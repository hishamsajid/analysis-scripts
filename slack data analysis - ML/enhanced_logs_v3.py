import pandas as pn
from nltk import word_tokenize
from nltk import pos_tag 
from nltk import ne_chunk
from collections import Counter
import csv
import sys

reload(sys)
sys.setdefaultencoding('latin-1')
logs = pn.read_csv('logs_enhanced.csv',encoding='latin-1')
q_messages = logs.loc[(logs['num_questions'] > 0) & (logs['channel'] == 'adobe-analytics (C03AFUKHC)'), 'message_utf8']    

tg_list = []
itr = 0
for item in q_messages.iteritems():

    tg_item_tree = ne_chunk(pos_tag(word_tokenize(item[1])))
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
#with open('most_common_adobeChannel.csv', 'wb') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(most_common)



