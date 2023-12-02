class WaterManagementSystem:
    def __init__(self):
        self._water_sources = {}
        self._water_consumption = {}

    def add_water_source(self, source_name, capacity):
        """Add a new water source to the system."""
        self._water_sources[source_name] = capacity
        self._water_consumption[source_name] = 0
        print(f"Water source '{source_name}' added with a capacity of {capacity} liters.")

    def use_water(self, source_name, amount):
        """Use water from a specified source."""
        if source_name not in self._water_sources:
            print(f"Error: Water source '{source_name}' not found.")
            return

        if amount <= 0:
            print("Error: Please enter a valid positive amount of water.")
            return

        if amount > self._water_sources[source_name]:
            print(f"Error: Not enough water in '{source_name}' to fulfill the request.")
            return

        self._water_sources[source_name] -= amount
        self._water_consumption[source_name] += amount
        print(f"{amount} liters of water used from '{source_name}'.")

    def display_water_status(self):
        """Display the status of all water sources."""
        print("\nWater Sources:")
        for source_name, capacity in self._water_sources.items():
            consumption = self._water_consumption[source_name]
            remaining = capacity - consumption
            print(f"{source_name}: {remaining}/{capacity} liters remaining")

    def run(self):
        """Run the water management system."""
        while True:
            print("\n1. Add Water Source")
            print("2. Use Water")
            print("3. Display Water Status")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                source_name = input("Enter water source name: ")
                try:
                    capacity = int(input("Enter capacity in liters: "))
                except ValueError:
                    print("Error: Please enter a valid numeric value for capacity.")
                    continue
                self.add_water_source(source_name, capacity)

            elif choice == "2":
                source_name = input("Enter water source name: ")
                try:
                    amount = int(input("Enter amount of water to use in liters: "))
                except ValueError:
                    print("Error: Please enter a valid numeric value for the amount.")
                    continue
                self.use_water(source_name, amount)

            elif choice == "3":
                self.display_water_status()

            elif choice == "4":
                print("Exiting water management system.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    water_system = WaterManagementSystem()
    water_system.run()
