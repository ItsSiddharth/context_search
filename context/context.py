import pickle
from gensim.models.keyedvectors import KeyedVectors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import argparse
import json
import subprocess
import PyPDF2 
import textract
import time

start_time = time.time()

class model:

    def load_model(self):
        modelname = 'glove_model.pickle'
        infile = open(modelname,'rb')
        glove_model = pickle.load(infile)
        infile.close()
        return glove_model


    def getting_list_of_words(self, filepath='tensorflow.pdf'):
        pdfFileObj = open(filepath,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        entire_pdf = []
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text = pageObj.extractText()

            if text != "":
                text = text

            else:
                text = textract.process(fileurl, method='tesseract', language='eng')
                

            tokens = word_tokenize(text)
            punctuations = ['(',')',';',':','[',']',',','.']
            stop_words = stopwords.words('english')
            keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
            for words in keywords:
                entire_pdf.append([count, words])
        return(entire_pdf)

    def perform_skip(self, pageno_word_list, input_word):
        counter, pos = [], []
        count, distance, current_page = 0, 0, 0
        glove_model = self.load_model()
        for element in pageno_word_list:
            word = element[1]
            page = element[0]
            if page < current_page + 1 :
                pass
            else:
                if word == input_word:
                    pos.append(count)
                    current_page = page
    
            count = count + 1
        for i in range (0,len(pos)-1):
            for j in range (pos[i]+1,pos[i+1]):
                try:
                    distance = distance + glove_model.similarity(pageno_word_list[j][1], input_word)
                except:
                    pass
            counter.append(distance/j)
            distance = 0

        counter, pos = (list(x) for x in zip(*sorted(zip(counter, pos))))

        return(pageno_word_list[pos[-1]][0], pageno_word_list[pos[-2]][0], pageno_word_list[pos[-3]][0], pageno_word_list[pos[-4]][0], pageno_word_list[pos[-5]][0])

#pickle.dump(model, open('modelforapi.pickle', 'wb'))
#filename = 'tensorflow.pdf'
#testing = model()
#x, y, z, a, b = testing.perform_skip(testing.getting_list_of_words(), 'convolution')
#subprocess.call(['evince -i ' + str(z) + ' ' + filename],shell =True)

context = model()
 

