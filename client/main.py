"""
This script downloads photos from Instagram by received subscription type and id.
args:
    0 -subscription_type: 'tag', 'location'
    1 -object_id: for example, if subscription_type is 'tag' then object_id is tag's name
"""
__author__ = 'Aydar'

from instagram.client import InstagramAPI
from Sketch import Skecth
from Photo import Photo
from TextProcessor import TextProcessor
import sys

debug = 1
subscription_type = "tag"
object_id = "Kazan"

# args processing
if not debug:
    if len(sys.argv)!= 2:
        print("Error: Wrong arguments")
        raise

    subscription_type = sys.argv[0]
    object_id = sys.argv[1]



access_token = "1139854136.bf74f35.330b479bc8ca4645b460120c65528f8c"
client_secret = "f3c9e7764acb4d8b86c1e2fe27928983"

api = InstagramAPI(access_token = access_token, client_secret=client_secret)
media_list = None

if subscription_type == "tag":
    media_list = api.tag_recent_media(tag_name=object_id, count=10)
elif subscription_type == "location":
    media_list = api.location_recent_media(location_name=object_id, count=10)
else:
    print("Error: Wrong subscription type")
    raise

sketch = Skecth()
textProcessor = TextProcessor()


def get_photos_from_medialist(medialist):
    photos=[]
    for media in medialist:
        photo = Photo()
        photo.id = media.id
        photo.words = textProcessor.get_words(media.caption.text)
        photo.photo_url = media.images['low_resolution'].url
        photo.time = media.created_time

        photos.append(photo)
    return photos


def save_photos_list(photos_list):
    file = open("photos.txt", 'w', encoding="utf-8")

    for photo in photos_list:
        file.write(photo.id+'\t')
        file.write(str(photo.time)+'\t')
        file.write(photo.get_words_as_str()+'\t')
        file.write(photo.photo_url+'\n')
    file.close()

photos = get_photos_from_medialist(media_list[0])
save_photos_list(photos)


