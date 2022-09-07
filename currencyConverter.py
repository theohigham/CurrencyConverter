print("Welcome to the python currency converter!")
print("Supported currencies include: USD, GBP, EUR, AUD, CNY, INR, CAD, JPY")

conversionRates = {
#USD to ..

"USD" : 1.0,	
"GBP" : 0.87125,
"EUR" : 1.0053,
"AUD" : 1.4858,
"CNY" : 1.3171,
"INR" : 79.820,
"CAD" : 1.3172,
"JPY" : 144.42

}

original = input("Enter your original currency: ")
desired = input("Enter your desired currency: ")
quantity = input("Enter your quantity of " + original + ": ")

#Convert quantity to USD
quantityUSD = (1/conversionRates[original]) * float(quantity) 

#Convert quantity from USD to desired currency
quantityDesired = conversionRates[desired] * quantityUSD

print(str(quantity) + " " + original + " = " + str(quantityDesired) + " " + desired) 