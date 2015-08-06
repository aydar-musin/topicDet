__author__ = 'Aydar'
import datetime
"""
representation for Instagram photo
"""
class Photo:
    def __init__(self):
        self.id = ''
        self.words = []
        self.photo_url = " "
        self.datetime = None

    def get_words_as_str(self):
        str = u''
        for word in self.words:
            str += word + ' '
        return str

    def __str__(self):
        return self.id+'\t'+str(self.datetime)+'\t'+self.get_words_as_str()+'\t'+self.photo_url+'\n'
