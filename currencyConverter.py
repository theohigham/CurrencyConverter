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

symbols = {
	
"USD" : "$",
"GBP" : "£",
"EUR" : "€",
"AUD" : "$",
"CNY" : "¥",
"JPY" : "¥",
"CAD" : "$",
"INR" : "₹"

}

original = input("Enter your original currency: ")
desired = input("Enter your desired currency: ")
quantity = input("Enter your quantity of " + original + ": " + symbols[original])

#Convert quantity to USD
quantityUSD = (1/conversionRates[original]) * float(quantity) 

#Convert quantity from USD to desired currency
quantityDesired = conversionRates[desired] * quantityUSD

print(symbols[original] + str(quantity) + " " + original + " = " + symbols[desired] + str(quantityDesired) + " " + desired) 