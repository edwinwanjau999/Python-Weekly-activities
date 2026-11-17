#Create a parent class named Vehicle
class Vehicle:
    def __init__(self, reg_number, model):
        # Parent attributes: Registration number and Model
        self.reg_number = reg_number
        self.model = model

    #Include a method named displayVehicle()
    def displayVehicle(self):
        print(f"Registration Number : {self.reg_number}")
        print(f"Model               : {self.model}")


#Create a child class named Bus that inherits from Vehicle
class Bus(Vehicle):
    def __init__(self, reg_number, model, passenger_capacity):
       
        super().__init__(reg_number, model)
        
        # iv. Add passenger capacity to the Bus class
        self.passenger_capacity = passenger_capacity

    #Include a method named displayBus() to display all vehicle information
    def displayBus(self):
        print("\n--- Bus Transport Profile ---")
        # Reuse parent display method to show registration and model
        self.displayVehicle()
        print(f"Passenger Capacity  : {self.passenger_capacity} seats")


if __name__ == "__main__":
    
    my_bus = Bus(
        reg_number="KDA 456Z",
        model="Isuzu FRR Bus",
        passenger_capacity=42
    )

    my_bus.displayBus()
