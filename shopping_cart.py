foods=[]
prices=[]
total=0
while True:
	food=input("enter the food items you want(Q to stop) : ")
	if food.upper()=="Q":
		break
	else:
		price=float(input(f"enter the price of {food} : "))
		foods.append(food)
		prices.append(price)
		
print("-----YOUR FOOD ITEMS-----")		
for food in foods:
	print(food,end=" ")
print()
print("----YOUR BILL------")
for price in prices:
	total+=price
print(f"₹{total}")
