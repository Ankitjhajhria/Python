#Convertor

  #HEIGHT


    #HEIGHT IN FOOT
Foot = input("ENTER YOUR HEIGHT IN FOOT > ")


    #HEIGHT IN INCHE
Inche = input("ENTER YOUR HEIGHT IN INCHE >")


    #FOOT IN METERS
FootInMeters = 0.3048


    #INCHE IN METERS
IncheInMeters = 0.0254


    #HEIGHT AFTER CALCULATION
HeightInMeters = (Foot*FootInMeters)  +   (Inche*IncheInMeters)


    #ENTER WEIGHT
YourWeight = input("EnterYourWeight>")


    #BMI
YourBmi = (YourWeight)/(HeightInMeters**2)


    #FINAL
print(YourBmi)

        

          

          



