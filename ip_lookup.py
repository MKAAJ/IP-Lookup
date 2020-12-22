import requests
import json


Welcome="""
\n***********************
          ***          \n
Welcome To IP Lookup Script\n
          ***            
***********************\n
"""
print(Welcome)

def isIP(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False

print("Options: 1) Whois Service               2)Reverse DNS lookup\n")


while True:
	try:
		selectednum=int(input("\nEnter Your Option: "))
	except ValueError:
		print("Error: Please use numeric digits.\n")
		continue
	break


if selectednum==1:
	print("\n1) Whois Service:-")
	while True:
		inputIP=input("	Please Enter IP: ")
		if inputIP.count(".") == 3 and all(isIP(i) for i in inputIP.split(".")):
			response= requests.get("http://ipwhois.app/json/"+inputIP)
			#https://ipwhois.io/documentation

			if response.status_code==200:
				print("\nWhois Information for "+inputIP+" :")
				ipwhois=json.loads(response.text)
				request_status=str(ipwhois["success"])
				str1=request_status.strip()
				if str1=="True":
					print("IP:  "+ipwhois["ip"])
					print("Type:  "+ipwhois["type"])
					print("Country:  "+ipwhois["country"])
					print("Country Code:  "+ipwhois["country_code"])
					print("Region:  "+ipwhois["region"])
					print("City:  "+ipwhois["city"])
					print("ASN:  "+ipwhois["asn"])
					print("Organization:  "+ipwhois["org"])
					print("ISP:  "+ipwhois["isp"])
				else:
					print(ipwhois["success"])	
			else:
				print(response.raise_for_status)
			break		
		else:
			print("\nError: Invalid IP Address.\n")
			continue		
elif selectednum==2:
	#https://viewdns.info/api/docs/reverse-dns-lookup.php
	APIKEY="Enter Your APIKEY"
	print("\n2) Reverse DNS Lookup:-")
	while True:
		inputIP2=input("	Please Enter IP: ")
		if inputIP2.count(".") == 3 and all(isIP(i) for i in inputIP2.split(".")):
			response2=requests.get("https://api.viewdns.info/reversedns/?ip="+inputIP2+"&apikey="+APIKEY+"&output=json")
			jsonResponse=json.loads(response2.text)
			print("\nDNS: "+jsonResponse["response"]["rdns"])
			break
		else:
			print("\nError: Invalid IP Address.\n")
			continue	
	
	



