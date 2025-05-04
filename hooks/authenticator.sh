#!/usr/bin/env sh
#echo $CERTBOT_DOMAIN
#echo $CERTBOT_VALIDATION
#ssh -i /home/ran/.ssh/dynv6 api@dynv6.com hosts $CERTBOT_DOMAIN records set _acme-challenge txt data $CERTBOT_VALIDATION
python3 /home/ran/keys/create_txt.py $CERTBOT_VALIDATION
sleep 4
exit 0
