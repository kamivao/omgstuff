#https://www2.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
#https://www.tutorialspoint.com/python/string_translate.htm
# document similarity



import nltk, string, os


from collections import Counter

def get_tokens():
   with open('/home/kamivao/git/PARS/txt20+/21_5.txt', 'r') as document_21_5:
    text = document_21_5.read()
    lowers = text.lower()
    #string.punctuation = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    #знаки пунктуации удалены с помощью метода maketrans()
    #https://www.tutorialspoint.com/python/string_translate.htm
    symbols_to_remove = "\"!#$%&\'()*+,./:;<=>?@[\\]^_`{|}~" # сохранен дефис

    #TODO: написать регулярное выражение, которое будет удалять тире

    table = str.maketrans("", "", symbols_to_remove)
    no_punctuation = lowers.translate(table)
   # no_punctuation = lowers.translate(string.punctuation)
    print(no_punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print(count.most_common(10))


