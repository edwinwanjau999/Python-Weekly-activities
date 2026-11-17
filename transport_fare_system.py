#Create a parent class named Vehicle
class Vehicle:
    def calculateFare(self, distance):
        """Base method for calculating fare (to be overridden by subclasses)."""
        pass


#Create a class named Bus that implements calculateFare()
class Bus(Vehicle):
    def calculateFare(self, distance):
        # Fare = Distance × 50
        fare = distance * 50
        return fare


#Create a class named Taxi that implements calculateFare()
class Taxi(Vehicle):
    def calculateFare(self, distance):
        # Fare = Distance × 100
        fare = distance * 100
        return fare


#In the main section: Create objects and calculate fares
if __name__ == "__main__":
    # Create one Bus object and one Taxi object
    bus_obj = Bus()
    taxi_obj = Taxi()

   
    travel_distance = 10

    bus_fare = bus_obj.calculateFare(travel_distance)
    taxi_fare = taxi_obj.calculateFare(travel_distance)

    print("--- Transport Company Fare Summary ---")
    print(f"Distance Traveled: {travel_distance} km")
    print(f"Bus Fare  (KSh 50 per km) : KSh {bus_fare:,.2f}")
    print(f"Taxi Fare (KSh 100 per km): KSh {taxi_fare:,.2f}")
