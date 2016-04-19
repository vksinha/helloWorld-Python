from builtins import all
'''
Some boolean operations
There are only 2- True & False (case sensitive)
!= results to True if evaluation is false. Results in False if evaluation is True.
'''

mybool = "True"
print (mybool)
mybool2 = ("True" != mybool) #Will result in False
mybool3 = ("False" != mybool) #Will result in True
print (mybool2)
print (mybool3)
mybool4 = (7 !=8) #Since 7 is NEQ to 8, evaluation is False & hence result is True because of negation.
print (mybool4)

# Other Comparisions
bool1 = (7<8) #True
bool2 = (7>8) #False
bool3 = (7==7.0) #True
bool4 = (7<7.0) #False
print (bool1)
print (bool2)
print (bool3)
print (bool4)