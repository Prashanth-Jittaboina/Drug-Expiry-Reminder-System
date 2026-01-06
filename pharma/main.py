import csv
from datetime import datetime

FILE_NAME = "drugs.csv"


 
class Drug:
    def __init__(self, name, batch, expiry_date):
        self.name = name
        self.batch = batch
        self.expiry_date = expiry_date


 
class DrugManager:

    def __init__(self):
        self.create_file()

     
    def create_file(self):
        try:
            with open(FILE_NAME, "x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Batch", "Expiry Date"])
        except FileExistsError:
            pass

    
    def add_drug(self):
        name = input("Enter drug name: ")
        batch = input("Enter batch number: ")
        expiry = input("Enter expiry date (YYYY-MM-DD): ")

        try:
            datetime.strptime(expiry, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            return

        drug = Drug(name, batch, expiry)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([drug.name, drug.batch, drug.expiry_date])

        print("Drug added successfully!")

    
    def check_expiry(self):
        today = datetime.today()
        found = False

        print("\nDrug Expiry Status:\n")

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expiry_date = datetime.strptime(row["Expiry Date"], "%Y-%m-%d")
                days_left = (expiry_date - today).days

                if days_left < 0:
                    print(
                        f"EXPIRED  Drug: {row['Name']}, "
                        f"Batch: {row['Batch']}, "
                        f"Expired {-days_left} days ago"
                    )
                    found = True

                elif days_left <= 30:
                    print(
                        f"NEAR EXPIRY  Drug: {row['Name']}, "
                        f"Batch: {row['Batch']}, "
                        f"Days Left: {days_left}"
                    )
                    found = True

        if not found:
            print("No expired or near-expiry drugs found.")


 
def main():
    manager = DrugManager()

    while True:
        print("\n--- Drug Expiry Reminder System ---")
        print("1. Add Drug")
        print("2. Check Expiry")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_drug()
        elif choice == "2":
            manager.check_expiry()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


main()
