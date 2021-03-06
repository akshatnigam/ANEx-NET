import dpkt
import optparse
import socket
import requests
import pyfiglet
import argparse
import sys
import os
result = pyfiglet.figlet_format("AnExNet")
print(result)
g=[]
k=[]
def userDownload(pcap):
    for(ts,buf) in pcap:
        try:
            global g
            eth=dpkt.ethernet.Ethernet(buf)
            ip=eth.data
            src=socket.inet_ntoa(ip.src)
            dst=socket.inet_ntoa(ip.dst)
            tcp=ip.data
            http=dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                        print '\n'+'a file was get from  '+dst+' file was download by ip host  '+src+'\n'
            g.append(dst)
            	
	except:
            pass
def Nscans(pcap):
    for(ts,buf) in pcap:
        try:
            global g
            global k
            eth=dpkt.ethernet.Ethernet(buf)
            ip=eth.data
            src=socket.inet_ntoa(ip.src)
            dst=socket.inet_ntoa(ip.dst)
            tcp=ip.data
            http=dpkt.http.Request(tcp.data)
            if http.method == 'GET':
               print '\n'+'a file was get from  '+dst+' file was download by ip host  '+src+'\n'
               g.append(src)
               k.append(dst)	
        except:
            pass
    n=int(input('which section you want to see '))
    d=raw_input('what you want to scan host(h) or source(s) ')
    if d == "h":
       ip=g[n]
    else:
       ip=k[n]
    flag=raw_input("which flag you want to implement ")
    a=raw_input("are you root(y or n) ")
    if a == "y":
            os.system("nmap "+flag+" "+ip)
    else:
            os.system("sudo nmap "+flag+" "+ip)        
def geoLoc(pcap):
    for(ts,buf) in pcap:
        try:
            global g
            global k
            eth=dpkt.ethernet.Ethernet(buf)
            ip=eth.data
            src=socket.inet_ntoa(ip.src)
            dst=socket.inet_ntoa(ip.dst)
            tcp=ip.data
            http=dpkt.http.Request(tcp.data)
            if http.method == 'GET':
               print '\n'+'a file was get from   '+dst+' file was download by ip host   '+src+'\n'
               g.append(dst)
               k.append(src)
        except:
            pass
    n=int(input('which section you want to see '))
    d=raw_input('Who\'s Geolocation you want to see host(h) or source(s) ')
    if d == "h":
       ip=g[n]
    else:
       ip=k[n]
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    print(geo_data)  

def countPac():
	counter=0
	ipcounter=0
	tcpcounter=0
	udpcounter=0

	filename=raw_input('please enter your file name and path. ')

        for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):

    	    counter+=1
   	    eth=dpkt.ethernet.Ethernet(pkt) 
    	    if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
       	      continue

    	    ip=eth.data
    	    ipcounter+=1

    	    if ip.p==dpkt.ip.IP_PROTO_TCP: 
       	      tcpcounter+=1
    	    if ip.p==dpkt.ip.IP_PROTO_UDP:
              udpcounter+=1

	print ("Total number of packets in the pcap file: ", counter)
	print ("Total number of ip packets: ", ipcounter)
	print ("Total number of tcp packets: ", tcpcounter)
	print ("Total number of udp packets: ", udpcounter)    
def main():
    
 
    
    parser = argparse.ArgumentParser(description='This is a program to fetch information from a .pcap file.	Enter operation=	hd - get host and destination ip.  ||  g - get geolocation.  ||  n - get total number of packets including separate TCP and UDP packets || nm - for nmap scan.')

   
    parser.add_argument('--operation', type=str, default='n',
                        help='What operation? Can choose hd, g, nm or n')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
   
def calc(args):
    if args.operation == 'hd':
      filename =raw_input('please enter your file name and path. ')
      f=open(filename)
      pcap = dpkt.pcap.Reader(f) 
      userDownload(pcap)
    elif args.operation == 'g':
        filename =raw_input('please enter your file name and path. ')
        f=open(filename)
        pcap = dpkt.pcap.Reader(f) 
        geoLoc(pcap)
    elif args.operation == 'nm':
        filename =raw_input('please enter your file name and path. ')
        f=open(filename)
        pcap = dpkt.pcap.Reader(f) 
        Nscans(pcap)
    elif args.operation == 'n':
         countPac()
if __name__ == '__main__':
    main()
	  
