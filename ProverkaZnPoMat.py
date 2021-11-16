from math import *
from random import *
from keyboard import *
print("Math test".center(60,"*"))
level=0
while level not in [1,2,3]:
	try:
		level=int(input("Choose Difficulty 1,2 or 3: "))
	except ValueError:
		print("Only 1,2 or 3!")
	except:
		print("Nope, only 1,2 or 3!")
if level==1:
	min=2
	max=10
	tehed=["+","-"]
elif level==2:
	min=2
	max=15
	tehed=["+","-","*"]
elif level==3:
	min=2
	max=20
	tehed=["+","-","*","/"]#peremenaja dlja choice
while True:
	v=input("continue?")
	if v=="no":
		break
	else:
		a=randint(min,max)
		b=randint(min,max)
		tehe=choice(tehed)
		print(f"{a}{tehe}{b}",end=" ")
		vaja=eval(str(a)+tehe+str(b))
		answer=int(input("="))
		if answer==int(vaja):
			print("Nice answer bro")
		else:
			print("terrible answer bro")