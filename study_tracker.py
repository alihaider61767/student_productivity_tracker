import csv
from datetime import datetime, timedelta

# File to store data
DATA_FILE = "study_data.csv"

# Ensure the CSV file exists with headers
def initialize_file():
    try:
        with open(DATA_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Subject', 'Hours', 'Topics'])
    except FileExistsError:
        pass  # File already exists

# Add a study log entry
def add_study_log(subject, hours, topics):
    date_today = datetime.now().strftime("%Y-%m-%d")
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)   
        writer.writerow([date_today, subject, hours, topics])
    print(f"\n✅ Study log added: {hours} hours on {subject} ({topics})")

# Get summary of the last 7 days
def get_weekly_summary():
    summary = {}
    seven_days_ago = datetime.now() - timedelta(days=7)
    with open(DATA_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry_date = datetime.strptime(row['Date'], "%Y-%m-%d")
            if entry_date >= seven_days_ago:
                subject = row['Subject']
                hours = float(row['Hours'])
                if subject in summary:
                    summary[subject] += hours
                else:
                    summary[subject] = hours
    return summary

# Program starts here
initialize_file()

print("📚 Welcome to Student Study Tracker!")
while True:
    print("\nChoose an option:")
    print("1. Add a study log")
    print("2. View weekly summary")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == '1':
        subject = input("Enter subject name: ")
        hours = float(input("Enter hours studied: "))
        topics = input("Enter topics covered: ")
        add_study_log(subject, hours, topics)

    elif choice == '2':
        summary = get_weekly_summary()
        print("\n📊 Weekly Summary:")
        for sub, hrs in summary.items():
            print(f"- {sub}: {hrs} hours")
    
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")