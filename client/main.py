"""
This script downloads photos from Instagram by received subscription type and id.
args:
    0 -subscription_type: 'tag', 'location'
    1 -object_id: for example, if subscription_type is 'tag' then object_id is tag's name
"""
__author__ = 'Aydar'

from Sketch import Skecth
from TextProcessor import TextProcessor
from Instagram import Instagramm
from Photo import Photo
from MainModule import MainModule
import time

import sys

debug = 1
subscription_type = "tag"
object_id = "innopolis"

# args processing
if not debug:
    if len(sys.argv)!= 2:
        print("Error: Wrong arguments")
        raise

    subscription_type = sys.argv[0]
    object_id = sys.argv[1]

instagram = Instagramm()
mainModule = MainModule()

def get_photos():
    photos=[]
    if subscription_type == "tag":
        photos = instagram.get_photos_by_tag(object_id)
    elif subscription_type == "location":
        photos = instagram.get_photos_by_location(object_id)
    else:
        print("Error: Wrong subscription type")
        raise

    photos.sort(key=lambda x: x.datetime, reverse=True)
    return photos


while 1:
    print("updating...")
    photos = get_photos()
    for photo in photos:
        mainModule.try_add_photo(photo)

    mainModule.save_current_state()
    print("wait 30 sec")
    time.sleep(30)





