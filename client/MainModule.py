__author__ = 'Aydar'

from Instagram import Instagramm
from Photo import Photo
import datetime
import operator

class MainModule:
    def __init__(self):
        self.photos_on_pool = [] #ordered pool of latest photos
        self.photos_in_history = {}
        self.__load_history()

    @staticmethod
    def __parse_photo_fromline(line):
        photo=Photo()
        args = line.split('\t')
        photo.id=args[0]
        photo.datetime=datetime.datetime.strptime(args[1], "%Y-%m-%d %H:%M:%S")
        photo.words=args[2].split()
        photo.photo_url=args[3]

        return photo

    def __load_history(self):
        print("loading history...")
        file = open("photos.txt","r",encoding="utf-8")
        for line in file:
            photo = MainModule.__parse_photo_fromline(line)
            self.photos_in_history[photo.id]=photo

    def save_photos_list(self,photos_list):
        file = open("photos.txt", 'w', encoding="utf-8")

        for photo in photos_list:
            file.write(photo.id+'\t')
            file.write(str(photo.time)+'\t')
            file.write(photo.get_words_as_str()+'\t')
            file.write(photo.photo_url+'\n')
        file.close()

    def try_add_photo(self, photo):
        if photo.id not in self.photos_in_history:
            self.photos_in_history[photo.id] = photo

    def save_current_state(self):
        words={}
        for key in self.photos_in_history:
            for word in self.photos_in_history[key].words:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        words=sorted(words.items(), key=operator.itemgetter(1), reverse=True)

        state = State()
        state.photos = list(self.photos_in_history.values())


        for word in words[0:10]:
            state.topics.append(word[0])

        state.save("state.txt")
        return state

class State:
    def __init__(self):
        self.photos = []
        self.topics = []

    def save(self,filename):
        str=""
        for word in self.topics:
            str+=word
            str+=" "

        for photo in self.photos:
            str+="\n" + photo.__str__()

        file=open(filename, 'w', encoding="utf-8")
        file.write(str)
        file.close()