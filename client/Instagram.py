__author__ = 'Aydar'

access_token = "1139854136.bf74f35.330b479bc8ca4645b460120c65528f8c"
client_secret = "f3c9e7764acb4d8b86c1e2fe27928983"

from instagram.client import InstagramAPI
from TextProcessor import TextProcessor
from Photo import Photo

class Instagramm:
    def __init__(self):
        self.__api = InstagramAPI(access_token = access_token, client_secret=client_secret)
        self.__textProcessor = TextProcessor()

    def __get_photos_from_medialist(self, medialist):
        photos=[]
        for media in medialist[0]:
            photo = Photo()
            photo.id = media.id
            photo.words = self.__textProcessor.get_words(media.caption.text)
            photo.photo_url = media.images['low_resolution'].url
            photo.datetime = media.created_time

            photos.append(photo)
        return photos

    def get_photos_by_tag(self,tag):
        media_list = self.__api.tag_recent_media(tag_name=tag, count=10)
        photos = self.__get_photos_from_medialist(media_list)

        for photo in photos: # remove words with tag
            words=[]
            for word in photo.words:
                if tag in word: photo.words.remove(word)

        return photos

    def get_photos_by_location(self,location):
        print("get_photos_by_location is not impleneted yet :(")
        raise
