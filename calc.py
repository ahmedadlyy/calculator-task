while (True) :
	x = int (input ("for standard  calc. press 1 \nfor scintific calc. press 2\nto exit press             3\n"))
	if x == 1 :
		y= input ("enter your operant ")
		if y == '+' :
			a = int (input("enter a "))
			b = int (input("enter b "))
			print ("a + b  = ",a+b)
		elif y == '-' :
			a = int (input("enter a "))
			b = int (input("enter b "))
			print ("a - b  = ",a-b)
		elif y == '*' :
			a = int (input("enter a "))
			b = int (input("enter b "))
			print ("a * b  = ",a*b)
		elif y == '/' :
			a = int (input("enter a "))
			b = int (input("enter b "))
			print ("a / b  = ",a/b)
	elif x == 2 :
		print ("enter your form of nums \nbinary perss       1\nhexadecimal press  2\noctaldecimal press 3\ndecimal press      4 ")
		d = int(input())
		if d == 1 :
			y= input ("enter your operant ")
		
			if y == '+' :
				a = int (input("enter a "),2)
				b = int (input("enter b "),2)
				print ("a + b  = ",a+b)
			elif y == '-' :
				a = int (input("enter a "),2)
				b = int (input("enter b "),2)
				print ("a - b  = ",a-b)
			elif y == '*' :
				a = int (input("enter a "),2)
				b = int (input("enter b "),2)
				print ("a * b  = ",a*b)
			elif y == '/' :
				a = int (input("enter a "),2)
				b = int (input("enter b "),2)
				print ("a / b  = ",a/b)
		elif d == 2 :
			y= input ("enter your operant ")
		
			if y == '+' :
				a = int (input("enter a "),16)
				b = int (input("enter b "),16)
				print ("a + b  = ",a+b)
			elif y == '-' :
				a = int (input("enter a "),16)
				b = int (input("enter b "),16)
				print ("a - b  = ",a-b)
			elif y == '*' :
				a = int (input("enter a "),16)
				b = int (input("enter b "),16)
				print ("a * b  = ",a*b)
			elif y == '/' :
				a = int (input("enter a "),16)
				b = int (input("enter b "),16)
				print ("a / b  = ",a/b)
		elif d == 3 :
			y= input ("enter your operant ")
		
			if y == '+' :
				a = int (input("enter a "),8)
				b = int (input("enter b "),8)
				print ("a + b  = ",a+b)
			elif y == '-' :
				a = int (input("enter a "),8)
				b = int (input("enter b "),8)
				print ("a - b  = ",a-b)
			elif y == '*' :
				a = int (input("enter a "),8)
				b = int (input("enter b "),8)
				print ("a * b  = ",a*b)
			elif y == '/' :
				a = int (input("enter a "),8)
				b = int (input("enter b "),8)
				print ("a / b  = ",a/b)
		elif d == 4 :
			y= input ("enter your operant ")
		
			if y == '+' :
				a = int (input("enter a "))
				b = int (input("enter b "))
				print ("a + b  = ",a+b)
			elif y == '-' :
				a = int (input("enter a "))
				b = int (input("enter b "))
				print ("a - b  = ",a-b)
			elif y == '*' :
				a = int (input("enter a "))
				b = int (input("enter b "))
				print ("a * b  = ",a*b)
			elif y == '/' :
				a = int (input("enter a "))
				b = int (input("enter b "))
				print ("a / b  = ",a/b)
	elif x == 3 :
		break
	else :
		print ("wrong entery try agian")