# Project 2 - Moonlander
# Author: Tushar Sharma 
# Version: Workman

def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator")
   print("\n   To begin you must specify the LM's initial altitude\n   and fuel level.  To simulate the actual LM use\n   values of 1300 meters and 500 liters, respectively.")
   print("\n   Good luck and may the force be with you!\n")
   
def getFuel():
  fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
  while (fuel <= 0 ):
   print("ERROR: Amount of fuel must be positive, please try again")
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): ")) 
  return fuel
def getAltitude():
  altitude = int(input("Enter the initial altitude of the LM (in meters): "))
  while (altitude <  1 or altitude > 9999):
   print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
   altitude = int(input("Enter the initial altitude of the LM (in meters): "))
  return altitude 
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
  # print("LM state at retrorocket cutoff")
   print("Elapsed Time:%5d s" % elapsedTime)
   print("        Fuel:%5d l" % fuelAmount)
   print("        Rate:%5d l/s" % fuelRate)
   print("    Altitude:%8.2f m" % altitude)
   print("    Velocity:%8.2f m/s\n" %velocity)

def getFuelRate(currentFuel):
   fuel_rate  = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while not(fuel_rate >= 0 and fuel_rate<=9):
      print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
      fuel_rate  = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")) 
   if (fuel_rate >= currentFuel):
    return currentFuel
   else:
    return fuel_rate
def updateAcceleration(gravity, fuelRate):
   acceleration = gravity * ((fuelRate/5)-1)
   return acceleration
def updateAltitude(altitude, velocity, acceleration):
   new_alt = altitude + velocity + (acceleration/2)
   return new_alt

def updateVelocity(velocity, acceleration):
   new_vel = velocity + acceleration
   return new_vel
def updateFuel(fuel, fuelRate):
   new_fuel = fuel - fuelRate
   return new_fuel

def displayLMLandingStatus(velocity):
   if (-1 <= velocity <= 0):
    print("Status at landing - The eagle has landed!")
   elif (-10 < velocity < -1):
    print("Status at landing - Enjoy your oxygen while it lasts!")
   elif ( velocity <= -10):
    print("Status at landing - Ouch - that hurt!")
   else:
     print("code error")
