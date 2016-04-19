from builtins import all
print ("I don't think he is 18 yet.")
print ('I don\'t think he is 18 yet.')
line = "I don't think he is 18."
line = "I don't think he is 18.\n"
print (line * 7) # Will work.
#print (line * 7.0) # Will be an error. 
# If actually have to print \n, then add 'r' before statement. 
print (r"C:\Users\vsin0305\newfolder") # Here is we remove 'r', there will be an error.
# Adding strings-- 

firstname = "Bill "
print (firstname + "Gates")
print (firstname + "Melinda" + " Gates")
print (firstname * 5)
#String variable values can be sliced up automatically. Treated as Array sort of.
print (firstname [0])
print (firstname [1])
# To get the last character of a string, use [-1].
secondname = "Brad" 
print (secondname [-1]) # should print d. iN case of 'firstname' it'll print 'blank space'.  
# Can also use -3, -2, -4 etc to get characters from last.
print (secondname [-3]) #should print 'r'.
# Can also slice up characters from a string in range
thirdname = "Jethalal"
print (thirdname [3:8])
# If starting postion is blank, it starts with [0], similarly if end is not specified, ends at [-1]
print (thirdname [:5])
print (thirdname [3:])
print (len(firstname))
print (len(secondname))