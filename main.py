#this program is named CraFinder for a company named AutoCountry.
#the program enables users to navigate through the menu options.

def CarFinder():

  print("AutoCountry")
  
 #recall the fuction  
CarFinder()

# display the list of cars 
AllowedVehiclesList= [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#start your loop 
while True:
  
   print("*******************************")

   print("AutoCountry Vehicle Finder v0.1")
   print("*******************************")
  
   print()
   choice_num1=("1. PRINT all Authorized Vehicles") 
   print()
   choic_num2=("2. Exit")
   print()
  
  #allow the user to choose/inter a number from the menue after the menu loads  
   user_input=input("Please Enter the following number below from the following menu:" 
 +"                                "+ "    "+
   choice_num1 + "     " + choic_num2+ "  "+ "     ")
 
   print()
  
  
# start your if statement to direct the user to the correct path after the user chooses a number from the menu.
  
   if user_input=="1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    print(AllowedVehiclesList) 
    print()
   if user_input=="2":
    print("Exit")
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
     
#initilize your terminator aftre the user chooses the number 2 from the menue to stop the program.
    break

        
               

  

  
