################################################################################
# program for MAC address lookup. This program uses https://macaddress.io/  API
# to search for MAC address and returns the company name:
# Usage: python <filename.py> <MAC address>
###############################################################################

import requests
import sys
import re
import json


def mac_address_lookup(search_address):
    try:
        api_key = "at_l7BGgu2v0H48MaWvWB8mHIehFkns6"
        output_type = "json"
        url = "https://api.macaddress.io/v1?apiKey={}&output={}&search={}".format(api_key, output_type, search_address)
        response = requests.get(url=url)
        if response.status_code == 200:
            content = response.content
            return content
        return

    except (requests.HTTPError, requests.ConnectionError) as e:
        return


if __name__ == "__main__":
    try:
        # take command line argument
        entered_search_address = sys.argv[1]
        # validate entered MAC Address
        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", entered_search_address.lower()):
            connection_response = mac_address_lookup(entered_search_address)
            if connection_response is not None:
                response = json.loads(connection_response)
                if "vendorDetails" in response:
                    print(response["vendorDetails"]["companyName"])
                else:
                    print("Company Name doesn't Exist")
            else:
                print("Connection error or HTTPError")
        else:
            print("Entered Incorrect MAC Address")
    except Exception as e:
        print(str(e))