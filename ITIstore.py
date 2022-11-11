print("wellcome to ITI store")
menu  = ['apples','25','bananas','20','grapes','30','watermalons','35']
loop1 = 1
loop2 = 1
total = 0
while(loop1==1) :
	choise=int(input("select mode :\ncustomer-------1\nowner----------2\nleave----------0\n"))
	if   (choise==1):
		print("wellcome to customer mode")
		while(loop2==1) :
			choise=int(input("select mode :\nshow menu---------------1\nadd a product-----------2\nprint the bill----------3\nback------0\n"))
			if   (choise==1):
				print("Menu :",menu)
			elif (choise==2) :
				print("select product",menu)
				pro=int(input())
				print("\n")
				if pro==1 :
					total+=int(menu[1])
				elif pro==2 :
					total+=int(menu[3])
				elif pro==3 :
					total+=int(menu[5])
				elif pro==4 :
					total+=int(menu[7])
				elif pro==5 :
					total+=int(menu[9])
				elif pro==6 :
					total+=int(menu[11])
				elif pro==7 :
					total+=int(menu[13])
			elif (choise==3) :
				print("bill : ",total)
			elif (choise==0) :
				loop2=0
	elif (choise==2) :
		print("wellcome to owner mode")
		while(loop2==1) :
			choise=int(input("select mode :\nshow menu---------------1\nadd new product-----------2\nremove item----------3\nback------0\n"))
			if   (choise==1):
				print("Menu :",menu)
			elif (choise==2) :
				print("enter the product and cost")
				m=input()
				menu.append(m)
				m=int(input())
				menu.append(m)
			elif (choise==3) :
				print("enter the place of the element remove ")
				x=int(input())
				menu.pop(x-1)
				menu.pop(x)
			elif (choise==0) :
				loop2=0
	elif (choise==0) :
		loop=0