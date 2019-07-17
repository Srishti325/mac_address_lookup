
# mac_address_lookup
search for a valid MAC address



This program is designed for MAC address lookup. Used https://macaddress.io/  API to search for MAC address and returns the company name:
Usage: python <filename.py> <MAC address>
example :In terminal enter:
python mac_address_look_srishti.py 44:38:39:ff:ef:57

Output:(string format)
Cumulus Networks, Inc

Running a single python file with docker without building image file:

docker run -it --rm --name my-first-python-script -v "$PWD":/my_new_docker python:3 python mac_address_look_srishti.py

