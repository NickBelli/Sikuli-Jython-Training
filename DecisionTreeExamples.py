temp = input("Enter the current temperature: ")

if int(temp) > 95:
    popup("Stay inside and play video games")
elif int(temp) > 65:
    popup("Go on a bike ride")
else:
    popup("Make a bonfire and roast marshmallows")