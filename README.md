root@kali:~# cd Downloads
root@kali:~/Downloads# python final.py -h
    _          _____      _   _      _   
   / \   _ __ | ____|_  _| \ | | ___| |_ 
  / _ \ | '_ \|  _| \ \/ /  \| |/ _ \ __|
 / ___ \| | | | |___ >  <| |\  |  __/ |_ 
/_/   \_\_| |_|_____/_/\_\_| \_|\___|\__|
                                         

usage: final.py [-h] [--operation OPERATION]

This is a program to fetch information from a .pcap file. Enter operation= hd-
get host and destination ip g- get geolocation n- get total number of packets
including separate TCP and UDP packets p- get first and last packet including
date and time

optional arguments:
  -h, --help            show this help message and exit
  --operation OPERATION
                        What operation? Can choose hd, g, or n
root@kali:~/Downloads# python final.py -h
    _          _____      _   _      _   
   / \   _ __ | ____|_  _| \ | | ___| |_ 
  / _ \ | '_ \|  _| \ \/ /  \| |/ _ \ __|
 / ___ \| | | | |___ >  <| |\  |  __/ |_ 
/_/   \_\_| |_|_____/_/\_\_| \_|\___|\__|
                                         

usage: final.py [-h] [--operation OPERATION]

This is a program to fetch information from a .pcap file. Enter operation= hd
- get host and destination ip. || g - get geolocation. || n - get total number
of packets including separate TCP and UDP packets.

optional arguments:
  -h, --help            show this help message and exit
  --operation OPERATION
                        What operation? Can choose hd, g, or n
root@kali:~/Downloads# python final.py --operation=hd
    _          _____      _   _      _   
   / \   _ __ | ____|_  _| \ | | ___| |_ 
  / _ \ | '_ \|  _| \ \/ /  \| |/ _ \ __|
 / ___ \| | | | |___ >  <| |\  |  __/ |_ 
/_/   \_\_| |_|_____/_/\_\_| \_|\___|\__|
                                         

please enter your file name and path.test2.pcap

a file was get from  104.95.190.54 file was download by ip host  10.0.2.15


a file was get from  104.95.190.54 file was download by ip host  10.0.2.15

Noneroot@kali:~/Downloads# python final.py --operation=g
    _          _____      _   _      _   
   / \   _ __ | ____|_  _| \ | | ___| |_ 
  / _ \ | '_ \|  _| \ \/ /  \| |/ _ \ __|
 / ___ \| | | | |___ >  <| |\  |  __/ |_ 
/_/   \_\_| |_|_____/_/\_\_| \_|\___|\__|
                                         

please enter your file name and path.test2.pcap
which section you want to see0
{u'country_code3': u'USA', u'ip': u'104.95.190.54', u'area_code': u'0', u'longitude': u'-97.822', u'organization_name': u'National Internet Backbone', u'continent_code': u'NA', u'country_code': u'US', u'organization': u'AS9829 National Internet Backbone', u'latitude': u'37.751', u'timezone': u'America/Chicago', u'country': u'United States', u'asn': 9829, u'accuracy': 1000}
Noneroot@kali:~/Downloads# python final.py --operation=g
    _          _____      _   _      _   
   / \   _ __ | ____|_  _| \ | | ___| |_ 
  / _ \ | '_ \|  _| \ \/ /  \| |/ _ \ __|
 / ___ \| | | | |___ >  <| |\  |  __/ |_ 
/_/   \_\_| |_|_____/_/\_\_| \_|\___|\__|
                                         

please enter your file name and path.test2.pcap
which section you want to see1
{u'country_code3': u'USA', u'ip': u'104.95.190.54', u'area_code': u'0', u'longitude': u'-97.822', u'organization_name': u'National Internet Backbone', u'continent_code': u'NA', u'country_code': u'US', u'organization': u'AS9829 National Internet Backbone', u'latitude': u'37.751', u'timezone': u'America/Chicago', u'country': u'United States', u'asn': 9829, u'accuracy': 1000}
Noneroot@kali:~/Downloads# python final.py --operation=n
    _          _____      _   _      _   
   / \   _ __ | ____|_  _| \ | | ___| |_ 
  / _ \ | '_ \|  _| \ \/ /  \| |/ _ \ __|
 / ___ \| | | | |___ >  <| |\  |  __/ |_ 
/_/   \_\_| |_|_____/_/\_\_| \_|\___|\__|
                                         

('Total number of packets in the pcap file: ', 5005)
('Total number of ip packets: ', 5005)
('Total number of tcp packets: ', 4833)
('Total number of udp packets: ', 172)
Noneroot@kali:~/Downloads# 
