import os
import time
os.system("toilet -f mono12 --gay \"update & upgrade\"")
t =  time.time()
ok = True
os.system("apt update && apt upgrade")
if time.time() - t > 1:
	print("\n[+] updated and upgrated succesfully")
else:
	print("\n[-] error ( don't forget to run with \"sudo\" )") 
	ok = False
	quit()
if ok == True:
	user = input(" \nWanna reboot [y/n] ")
	if user == "y":
		print("the device will be rebooted")
		os.system("reboot")
	elif user == "n":
		print("[-] the program will quit ")
		quit()
	else:
		print("\n[+] invalid input")
		quit()
