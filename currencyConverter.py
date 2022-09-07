from forex_python.converter import CurrencyRates
c = CurrencyRates()

print("Welcome to the python currency converter!")
print("Supported currencies include: USD, GBP, EUR, AUD, CNY, INR, CAD, JPY")

conversionRates = {
#USD to ..

"USD" : 1.0,	
"GBP" : c.get_rate('USD','GBP'),
"EUR" : c.get_rate('USD','EUR'),
"AUD" : c.get_rate('USD','AUD'),
"CNY" : c.get_rate('USD','CNY'),
"INR" :	c.get_rate('USD','INR'),
"CAD" : c.get_rate('USD','CAD'),
"JPY" : c.get_rate('USD','JPY')

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