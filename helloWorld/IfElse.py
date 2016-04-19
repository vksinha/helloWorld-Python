from builtins import all    

num = 12
print ("Output of first block\n")
if num > 5: #Note that block is not in braces. Its indented.
   print("Bigger than 5")
   if num <=47:
      print("Between 5 and 47")

# We can use If- Else
print ("Output of second block\n")
num = 7
if num == 5:
  print("Number is 5")
else: 
  if num == 11:
    print("Number is 11")
  else:
    if num == 7:
      print("Number is 7")
    else: 
      print("Number isn't 5, 11 or 7")

# Instead of Else-If, we can write elif:
print ("Output of third block\n")
num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")