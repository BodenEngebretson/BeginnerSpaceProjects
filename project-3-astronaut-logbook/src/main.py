# Astronaut Logbook Project

class AstronautLogbook:
    def __init__(self):
        self.entries = []

    def add_entry(self, date, activity):
        entry = {
            'date': date,
            'activity': activity
        }
        self.entries.append(entry)
        print(f"Entry added for {date}: {activity}")

    def view_entries(self):
        if not self.entries:
            print("No entries found.")
            return
        for entry in self.entries:
            print(f"Date: {entry['date']}, Activity: {entry['activity']}")

    def save_logbook(self, filename):
        with open(filename, 'w') as file:
            for entry in self.entries:
                file.write(f"{entry['date']}: {entry['activity']}\n")
        print(f"Logbook saved to {filename}")

    def load_logbook(self, filename):
        try:
            with open(filename, 'r') as file:
                self.entries = []
                for line in file:
                    date, activity = line.strip().split(': ', 1)
                    self.entries.append({'date': date, 'activity': activity})
            print(f"Logbook loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

def main():
    logbook = AstronautLogbook()
    
    while True:
        print("\nAstronaut Logbook")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Save Logbook")
        print("4. Load Logbook")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            activity = input("Enter activity: ")
            logbook.add_entry(date, activity)
        elif choice == '2':
            logbook.view_entries()
        elif choice == '3':
            filename = input("Enter filename to save logbook: ")
            logbook.save_logbook(filename)
        elif choice == '4':
            filename = input("Enter filename to load logbook: ")
            logbook.load_logbook(filename)
        elif choice == '5':
            print("Exiting the logbook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()