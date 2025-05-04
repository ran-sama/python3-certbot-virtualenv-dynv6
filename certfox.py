#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Check certificate lifetimes"""

import ssl
import json
import datetime
import subprocess

MINIMUM_LIFETIME = 14
CER_ISO_TIME = r'%b %d %H:%M:%S %Y %Z'
UTC_ISO_TIME = r'%Y-%m-%d %H:%M:%S'

CERT_1 = "/home/ran/keys/fullchain.pem"
COMMAND_1 = 'certbot certonly --config /home/ran/keys/cli.ini'
TIMESTAMP_1 = str(datetime.datetime.now(datetime.UTC)) + " UTC\n"


def cert_fox_sniff(domain, renew):
    """Perform memory unsafe checks"""
    present_day = datetime.datetime.now(datetime.UTC)
    present_time = present_day.replace(tzinfo=None)
    hahaha = present_time.isoformat(sep=" ", timespec="seconds")
    load_cert = ssl._ssl._test_decode_cert(domain)
    j = json.loads(json.dumps(load_cert))
    time_left = datetime.datetime.strptime(j['notAfter'], CER_ISO_TIME)
    days_left = time_left - datetime.datetime.strptime(hahaha, UTC_ISO_TIME)
    finaldays = days_left < datetime.timedelta(days=MINIMUM_LIFETIME)
    if finaldays is True:
        process = subprocess.Popen(renew.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        output, error = process.communicate()
        print(output)
        print(TIMESTAMP_1, error)
    elif finaldays is False:
        pass
    else:
        pass


cert_fox_sniff(CERT_1, COMMAND_1)
