
AllowedVehiclesList_menu= [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
print(" all Allowed Vehicles")
print()
print(AllowedVehiclesList_menu)

print()

while True:
  
  print("*******************************")
  
  print("AutoCountry Vehicle Finder v0.1")
  print("*******************************")
  
  print()
  choice_num1=("1. PRINT all Authorized Vehicles") 
  print()
  choic_num2=("2. Exit")
  print()
  user_input=input("Please Enter the following number below from the following menu:" 
                   + choice_num1 + "     " + choic_num2+ "  ")
 
  print()
  
  

  if user_input=="1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    print(AllowedVehiclesList_menu) 
    print()
  if user_input=="2":
    print("Exit")
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    break
    
        
               

  

  
