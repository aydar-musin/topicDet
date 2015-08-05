__author__ = 'Aydar'

import time

from TextProcessor import TextProcessor

"""
class for term representation
"""
class Term:
    def __init(self):
        self.name = ""
        self.occurrence_list = [] # list of tuples where each tuple consist of timestamp and number of occurrences

class Skecth:
    def __init__(self):
        self.terms={}  # dictinary of terms (words and pairs of words)

    """
    updates sketch by posted text
    """
    def update(self, text):
        words, pairs = TextProcessor.process(text)
        cur_time = time.time()

        for word in words:
            if(word in self.terms):
                self.terms[word].append(cur_time)
            else:
                self.terms[word]=[cur_time]

