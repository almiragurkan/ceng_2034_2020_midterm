#!/usr/bin/python3
import os, threading, requests

print ("PID:", os.getpid())

print(os.getloadavg())

min1loadavg,min5loadavg,min15loadavg = os.getloadavg()
cpu_core_count=os.cpu_count()

if (cpu_core_count - min5loadavg < 1):
	exit()

def check_url(response_status_code):
	print("checking url: "+response_status_code)
	response=0
	try:
		response=requests.get(response_status_code)
	except:
		print("No response code, output was an error.")
		return
	if (response.status_code==200):
		print("response status code " + str(response.status_code) + " is successful")
	elif(response.status_code==400):
		print("Bad Request")	
	elif(response.status_code==500):
		print("Internal Server Error")
	else:
		print("Fail")	
	
array_of_url= ["https://api.github.com", "http://bilgisayar.mu.edu.tr/",
"https://www.python.org/", "http://akrepnalan.com/ceng2034",
"https://github.com/caesarsalad/wow"]

for i in range(len(array_of_url)):
	threads = threading.Thread(target=check_url, args=(array_of_url[i],))
	threads.start()
	threads.join()
	print("End of Script")
