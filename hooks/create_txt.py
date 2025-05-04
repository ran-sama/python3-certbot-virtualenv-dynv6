#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Upload TXT data to dynv6."""

import re
import sys
import time
import requests

ZONE_ID = '1234567'
API_TOKEN = 'SUPER_SECRET_TOKEN'
API_URI = 'https://dynv6.com/api/v2/zones/' + ZONE_ID + '/records'
API_HEADER = {'Authorization': 'Bearer ' + API_TOKEN, 'content-type': 'application/json'}
TXT_DATA = sys.argv[1]

MY_JSON_OBJECT = """{
"type": "TXT",
"name": "_acme-challenge",
"data": "blank",
"zoneID": 1234567
}"""


def autofill_record():
    """POST TXT data to API."""
    temp_route = re.sub(r'blank', TXT_DATA, MY_JSON_OBJECT)
    my_post = requests.post(url=API_URI, data=temp_route, headers=API_HEADER, timeout=10)
    print(my_post.content.decode('utf-8'))
    time.sleep(3)


autofill_record()
