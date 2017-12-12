#Erin J Sinclair
#112112
#Password Check
#Enter the password to find confidential information

password="Milky Cow"
username= "Erin J Sinclair"

player_guess=input ("Username:")
if player_guess=="Erin J Sinclair":
    password_guess=input ("Password:")
    if password_guess=="Milky Cow":
        print ("Access Granted")
        print("CONFIDENTIAL:")
        print("The enterance to the Lost City of Atlantas is located at 10621 Marbury Road, in the top right room facing south, under the frog in the 'rainforest'")
    else:
        print ("Access Denied")
     
else:
  print ("Access Denied")
