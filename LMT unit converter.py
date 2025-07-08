def lengthConv():
	print("Supported units: mm, cm, m, km")
	userIn = input("Enter length: ").lower()
	num = ''
	unit = ''
	for ch in userIn:
		if ch.isdigit() or ch=='.':
			num += ch
		else:
			unit += ch
	if num=='' or unit=='':
		print("Invalid input!")
		return

	value = float(num)

	if unit=="mm":
		meters = value/1000
	elif unit=="cm":
		meters = value/100
	elif unit=="m":
		meters = value
	elif unit=="km":
		meters = value*1000
	else:
		print("Invalid unit!")
		return

	print("\nConversions for " + str(value) + unit + ":")

	if unit!="mm":
		print("→", meters*1000, "mm")
	if unit!="cm":
		print("→", meters*100, "cm")
	if unit!="m":
		print("→", meters, "m")
	if unit!="km":
		print("→", meters/1000, "km")


def massConv():
	print("Supported units: mg, g, kg, tonne")
	userIn = input("Enter mass: ").lower()
	num = ''
	unit = ''
	for ch in userIn:
		if ch.isdigit() or ch=='.':
			num += ch
		else:
			unit += ch
	if num=='' or unit=='':
		print("Invalid input!")
		return

	value = float(num)

	if unit=="mg":
		grams = value/1000
	elif unit=="g":
		grams = value
	elif unit=="kg":
		grams = value*1000
	elif unit=="tonne":
		grams = value*1000000
	else:
		print("Invalid unit!")
		return

	print("\nConversions for " + str(value) + unit + ":")

	if unit!="mg":
		print("→", grams*1000, "mg")
	if unit!="g":
		print("→", grams, "g")
	if unit!="kg":
		print("→", grams/1000, "kg")
	if unit!="tonne":
		print("→", grams/1000000, "tonne")


def tempConv():
	print("Supported units: C, F, K")
	userIn = input("Enter temperature: ").upper()
	num = ''
	unit = ''
	for ch in userIn:
		if ch.isdigit() or ch=='.':
			num += ch
		else:
			unit += ch
	if num=='' or unit=='':
		print("Invalid input!")
		return

	value = float(num)

	if unit=="C":
		c = value
	elif unit=="F":
		c = (value-32)*5/9
	elif unit=="K":
		c = value-273.15
	else:
		print("Invalid unit!")
		return

	print("\nConversions for " + str(value) + unit + ":")

	if unit!="C":
		print("→", c, "C")
	if unit!="F":
		print("→", c*9/5+32, "F")
	if unit!="K":
		print("→", c+273.15, "K")


def menu():
	while True:
		print("\nChoose conversion type:")
		print("1. Length")
		print("2. Mass")
		print("3. Temperature")
		print("4. Exit")
		choice = input("Enter choice (1-4): ")
		if choice=="1":
			lengthConv()
		elif choice=="2":
			massConv()
		elif choice=="3":
			tempConv()
		elif choice=="4":
                        print("Thankyou for using me :)")
			break
		else:
			print("Invalid choice!")


if __name__=="__main__":
	menu()
