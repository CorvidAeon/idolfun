import json
import requests
import time
import sys
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","idolfun.settings")
django.setup()
from idol.models import CardData, CharaData, SkillData

api_url_base = "https://starlight.kirara.ca/api/v1/"
api_chara = "char_t/"
api_chara_list = "list/char_t"
api_card = "card_t/"

def get_name_list_from_db():
    chara_names = {}
    req = requests.get(api_url_base+api_chara_list)
    chara_list = req.json()
    for chara in chara_list['result']:
        chara_names[chara['chara_id']] = chara['conventional']
    return chara_names


#def get_card_list_from_db():

def save_img(link, save_loc):
    try:
        img_req = requests.get(link)
        if img_req.headers['content-type'] == 'image/png':
            with open(save_loc, 'wb') as f:
                f.write(img_req.content)
        else:
            print("Invalid content type: {}".format(img_req.headers['content-type']))
    except:
        print("Could not get file")

# should only run once
def get_all_images():
    spread_save_loc = "images/spread/"
    puchi_save_loc = "images/puchi/"
    icon_save_loc = "images/icon/"
    resume = False
    resume_point = 300612
    for card_id in CardData.objects.values_list('id', flat=True):
        if card_id == resume_point:
            resume = True
        if not resume:
            continue
        card_id_png_string = str(card_id)+".png"

        retry=0
        while True:
            try:
                req = requests.get(api_url_base+api_card+str(card_id))
                print(card_id)
                card_data = req.json()
            except json.JSONDecodeError:
                if retry >= 5:
                    break
                print("JSON issue, waiting 10 seconds to retry")
                time.sleep(10)
                retry+=1
            break
        if card_data['result'][0] is None:
            continue
        icon_loc = card_data['result'][0]['icon_image_ref']
        spread_loc = card_data['result'][0]['spread_image_ref']
        #api doesn't return puchi locations yet.
        puchi_loc = "https://hidamarirhodonite.kirara.ca/puchi/"+card_id_png_string
        if spread_loc is not None:
            save_img(spread_loc, spread_save_loc+card_id_png_string)

        save_img(icon_loc, icon_save_loc+card_id_png_string)
        save_img(puchi_loc, puchi_save_loc+card_id_png_string)
        time.sleep(2)


# only run if object isn't already translated
#def get_name_translation(name):

#def get_skill_translation(skill):

#def get_card_translation(card):

#puchi link https://hidamarirhodonite.kirara.ca/puchi/<spread file name>
#<p class="card_image_offlink"><a class="petit_link" target="_blank" href="{{ image_host }}/puchi/{{ card.id }}.png">{{ _("Petit sprite") }}</a></p>
get_all_images()