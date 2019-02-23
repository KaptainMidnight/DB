# -*- coding: utf-8 -*-

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from utils_1 import get_random_id
import mysql.connector
from time import time


vk_session = vk_api.VkApi(token="c0a9ae78d65852efad873d0ae29664145911b961e34fcaf83939e9bac3d8dd284dc65b11a058aacf36011")

vk = vk_session.get_api()

longpool = VkLongPoll(vk_session)


while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            pass
