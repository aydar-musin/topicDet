__author__ = 'Aydar'

"""
representation for Instagram photo
"""
class Photo:
    def __init__(self):
        self.id = ''
        self.words = []
        self.photo_url = " "

    def get_words_as_str(self):
        str = u''
        for word in self.words:
            str += word + ' '
        return str
