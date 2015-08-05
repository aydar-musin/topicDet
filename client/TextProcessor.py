__author__ = 'Aydar'

class TextProcessor:
    def __init__(self):
        self.stopwords = {}

        # loading stop-words
        file = open("stopwords.txt",mode='r')

        for line in file:
            self.stopwords[line.strip(' \t\n\r')] = 1

    """
    now it's just split(), remove stop-words and do case folding
    """
    def get_words(self, text):

        s = ".,!?#@"
        for i in range(0, len(s)):
            text = text.replace(s[i], "")

        myset = set(text.split())

        result=[]

        for word in myset: # case folding and removing stop-words
            term = word.lower()
            if (term not in self.stopwords):
                result.append(term)

        return result

    """
    returns words and pairs of words
    """
    def process(self, text):
        words=TextProcessor.__get_words(text)

        pairs=[]

        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    pairs.append(word1+" "+word2)

        return (words,pairs)