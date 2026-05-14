print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

cost = 0
if(size == 'S'):
    cost = cost + 15
    if(pepperoni == 'Y'):
        cost = cost + 2
elif(size == 'M'):
    cost = cost + 20
    if (pepperoni == 'Y'):
        cost = cost + 3
elif(size == 'L'):
    cost = cost + 25
    if (pepperoni == 'Y'):
        cost = cost + 3

if(extra_cheese == 'Y'):
    cost = cost + 1

print(f"Your final bill is: ${cost}.")