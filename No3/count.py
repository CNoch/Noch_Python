import string

def extend_word(text):
    pass

def show_in_order(records):
    pass

with open('subtitle.txt','r') as file:
    article = file.read()
    no_pun_text = article
    #获取除专一符外所有的符号
    _puncuation = string.punctuation.replace('\'','')