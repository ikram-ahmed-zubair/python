def title():
    print("=" * 40)
    print("      Heart Rate Analyzer")
    print("=" * 40)
    print()


def menu():
    print(
        "1. Add Heart Rate\n"
        "2. View Heart Rates\n"
        "3. Analyze Heart Rates\n"
        "4. Clear All Data\n"
        "0. Exit\n"
    )


def add_hr(hrs):
    try:
        r = int(input("Enter heart rate (bpm): "))

        if r <= 0:
            print("Heart rate must be positive.\n")
            return

        hrs.append(r)  # new
        print("Heart rate added successfully.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def view_hr(hrs):
    if not hrs:
        print("No heart rates recorded.\n")
        return

    print("\nRecorded Heart Rates")
    for i, r in enumerate(hrs, 1):  # new
        print(f"{i}. {r} bpm")
    print()


def stat_hr(hrs):
    if not hrs:
        print("No data available.\n")
        return

    avg = sum(hrs) / len(hrs)

    abn = sum(r < 60 or r > 100 for r in hrs)  # see

    print("\nAnalysis Report")
    print("-" * 30)
    print(f"Total Readings     : {len(hrs)}")
    print(f"Average Rate       : {avg:.2f} bpm")
    print(f"Highest Rate       : {max(hrs)} bpm")
    print(f"Lowest Rate        : {min(hrs)} bpm")
    print(f"Abnormal Readings  : {abn}\n")


def clr(hrs):
    hrs.clear()
    print("All heart rates deleted.\n")


def main():
    hrs = []

    title()

    while True:
        menu()

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.\n")
            continue

        if ch == 1:
            add_hr(hrs)
        elif ch == 2:
            view_hr(hrs)
        elif ch == 3:
            stat_hr(hrs)
        elif ch == 4:
            clr(hrs)
        elif ch == 0:
            print("Thank you for using Heart Rate Analyzer.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
