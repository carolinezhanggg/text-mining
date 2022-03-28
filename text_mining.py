import urllib.request 
import string
from mediawiki import MediaWiki
from thefuzz import fuzz
from thefuzz import process

def get_content_wiki(topic):
    """
    This function takes a parameter topic, which is the title of a text form Wekipedia.
    It would read in the text content and return a string.
    """
    wikipedia = MediaWiki()
    target = wikipedia.page(topic)
    return target.content


def freq(topic):
    """
    This function takes a parameter topic, which is the title of the text in Wekipedia.
    This function would return dictionary with keys of words appear in the text 
    and values of the how many times each word appears.
    The returned dictionary would be sorted by frequency from high to low.
    """
    text = get_content_wiki(topic)
    dic = {}
    new_dic = {}
    strippables = string.punctuation
    for c in strippables:
        text = text.replace(c," ")
    text_new = text.lower()
    for word in text_new.split():
        dic[word] = dic.get(word, 0) + 1  
    for key in dic:
        if dic[key] > 10:
            new_dic[key] = dic[key]
    new_dic = dict(sorted(new_dic.items(), key=lambda x:x[1],reverse= True))
    return new_dic


def stop_word(filename):
    """
    This function takes a parameter filename, and would read in the according file,
    and return a dictionary of the words in this file and how many times each word appears.
    """
    f = open(filename, encoding='UTF8')
    stop_word_d = {}
    for line in f:
        word = line.strip()
        stop_word_d[word] = 0
    return stop_word_d


def subtract(d1, d):
    """
    This function takes two parameters, d1 and d.
    It would return a dictionary with all keys that appear in d1 but not d.
    d1, d: dictionaries.
    """
    result_d = {}
    for key in d1:
        if key not in d:
            result_d[key] = d1[key]
    return list(result_d.items())[0:10]


def similarity(content1,content2):
    """
    This function takes two parameters, content1 and content2, which are strings.
    It would print the similarity percentage between the two strings, 
    the similarity between the two strings after sorted,
    and the similarity between the set of the two strings.
    """
    print(f'The similarity ratio between the Wekipedia articles of Harry Potter and Fantastic Beasts and Where to Find Them is:{fuzz.ratio(content1,content2)}%')
    print(f'The similarity ratio between the sorted Wekipedia articles of Harry Potter and Fantastic Beasts and Where to Find Them is: {fuzz.token_sort_ratio(content1, content2)}%')
    print(f'The similarity ratio between the set of Wekipedia articles of Harry Potter and Fantastic Beasts and Where to Find Them is: {fuzz.token_set_ratio(content1,content2)}%')

def main():
    topic1 = "Harry Potter"
    topic2 = "Fantastic Beasts and Where to Find Them"
    content1 = get_content_wiki(topic1)
    content2 = get_content_wiki(topic2)
    filename = "stopwords.txt"
    d = stop_word(filename)
    freq_d1 = freq(topic1)
    freq_d2 = freq(topic2)
    print(f'The top ten words appear in the book Harry Potter and the frequncies of each word are: {subtract(freq_d1,d)}')
    print(f'The top ten words appear in the book Fantastic Beasts and Where to Find Them and the frequncies of each word are: {subtract(freq_d2,d)}')
    similarity(content1, content2)

if __name__ == "__main__":
    main()