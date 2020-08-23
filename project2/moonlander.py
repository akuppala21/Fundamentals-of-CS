from landerFuncs import * 
def main():
   showWelcome()
   altitude = getAltitude()  
   tank_fuel = getFuel()
   print("\nLM state at retrorocket cutoff")
   elapsedTime = 0
   velocity = 0
   rate = 0 
   acceleration = 0
   displayLMState(elapsedTime, altitude, velocity, tank_fuel, rate)
   while (not  altitude <= 0 and tank_fuel  > 0):
     rate = getFuelRate(tank_fuel)
     acceleration = updateAcceleration(1.62, rate)
     tank_fuel = updateFuel(tank_fuel, rate)
     altitude = updateAltitude(altitude, velocity, acceleration)
     velocity = updateVelocity(velocity, acceleration)
     elapsedTime += 1 
     if (tank_fuel > 0 and altitude >= 0):
      displayLMState(elapsedTime, altitude, velocity, tank_fuel, rate)
   while (not altitude <= 0):
     print("OUT OF FUEL - Elapsed Time:%4d Altitude:%8.2f Velocity:%8.2f"     %(elapsedTime, altitude, velocity))
     rate = 0
     acceleration = updateAcceleration(1.62, rate)
     altitude = updateAltitude(altitude, velocity, acceleration)
     velocity = updateVelocity(velocity, acceleration)
     elapsedTime += 1
     tank_fuel = 0
   altitude = 0
   print("\nLM state at landing/impact")
   displayLMState(elapsedTime, altitude, velocity, tank_fuel, rate)
   displayLMLandingStatus(velocity)

if __name__ == '__main__':
   main()
