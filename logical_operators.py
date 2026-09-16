#or
temp = 30
is_raining =False
if temp >= 37 or temp <= 0 or is_raining :
    print("no outside for today")
else :
   print("no problem you can go out!")


#and not
temp_cook = 409
is_cooking = False
if temp_cook == 40 and is_cooking :
    print("you can eat it ")
elif temp_cook == 40 and not is_cooking :
    print("not for eating")
elif temp_cook != 40 and not is_cooking: 
    print("it burning ")

