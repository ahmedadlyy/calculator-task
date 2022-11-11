def arrow_right () :
	for x in range(5) :
		print("                      ",end='')
		for y in range(x+1) :
			print("*",end='')
		print("\n",end='')
	for x in range(29) :
		print("*",end='')
	print("\n",end='')
	for x in reversed(range(5)):
		print("                      ",end='')
		for y in range(x+1) :
			print("*",end='')
		print("\n",end='')


def arrow_up ():
	for x in reversed(range(5)):
		print ("           ",end='')
		for x in range (x) :
			print (" ",end='')
		for x in range (4-x) :
			print ("*",end='')
		for x in range (x) :
			print ("*",end='')	
		print("\n",end='')
	for x in range (10) :
		print("               ",end='')
		print("*\n",end='')
		
def arrow_down ():
	for x in range (10) :
		print("               ",end='')
		print("*\n",end='')
	for x in range(5):
		print ("           ",end='')
		for x in range(x) :
			print (" ",end='')
		for x in range(4-x) :
			print ("*",end='')
		for x in range(x) :
			print ("*",end='')
		print("\n",end='')
		
def arrow_left ():
	for x in reversed(range(4)):
		print(" ",end='')
		for x in range(x) :
			print(" ",end='')
		for x in range(3-x) :
			print("*",end='')
		print("\n",end='')
	for x in range(29) :
		print("*",end='')
	for x in reversed(range(5)):
		# print(" ",end='')
		for x in range(4-x) :
			print(" ",end='')
		for x in range(4-x) :
			print("*",end='')
		print("\n",end='')

import time
import os
while (True):
	arrow_right()
	time.sleep(1)
	os.system('cls')
	arrow_down()
	time.sleep(1)
	os.system('cls')
	arrow_left()
	time.sleep(1)
	os.system('cls')
	arrow_up()
	time.sleep(1)
	os.system('cls')
