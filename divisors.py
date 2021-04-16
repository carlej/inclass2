def divisors(a):
	i=0
	while i<a:
		i+=1
		if a%i == 0:
			print(i"\n")
		if i==a:
			break

val = input("Enter a number = ")
divisors(val);