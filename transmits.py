"""
This file holds the functions used to transmit addresses and
subnets from global app ti the import app
via API.
"""
import logging
import csv
import json
import requests
from classes.Address import Address
from classes.Subnet import Subnet
from classes.CustomAttribute import CustomAttribute
from classes.CustomAttribute import CustomFilter
requests.packages.urllib3.disable_warnings()


def transmit_subnets(session, settings_i, session_i, options):
    """
    Reads subnets addresses from the [global] application and imports them to the [import] application
    """
    logging.debug('------- ENTERING FUNCTION: transmit_subnets() -------')
    
    url_subnets = settings_i.url_app + '/subnets/'
    headers = {'app_id': str(settings_i.app),
               'Content-Type': 'application/json',
               'content': 'application/json',
               'token': str(session_i.token)  # calling token will auto-validate freshenss
               }
    try:
        for s_subnet in session.subnets:
            s_subnet.convert_json()
            json_prop = json.dumps(s_subnet.dict_props)
            req = requests.post(url_subnets, headers=headers, data=json_prop, verify=False)
            logging.debug(req.content)
    except Exception as e:
        logging.debug("Exception: " + str(e)) 

def transmit_addresses(session, settings_i, session_i, options):
    """
    Reads ip addresses from the [global] application and imports them to the [import] application
    """
    logging.debug('------- ENTERING FUNCTION: transmit_addresses() -------')
    
    url_addresses = settings_i.url_app + '/addresses/'
    headers = {'app_id': str(settings_i.app),
               'Content-Type': 'application/json',
               'content': 'application/json',
               'token': str(session_i.token)  # calling token will auto-validate freshenss
               }
    try:
        for s_addr in session.addresses:
            s_addr.convert_json()
            json_prop = json.dumps(s_addr.dict_props)
            logging.debug("Attempting to create ip: " + str(s_addr.ip))
            req = requests.post(url_addresses, headers=headers, data=json_prop, verify=False)
            logging.debug(req.content)
            print req.content
    except Exception as e:
        logging.debug("Exception: " + str(e))


if __name__ == '__main__':
    pass
