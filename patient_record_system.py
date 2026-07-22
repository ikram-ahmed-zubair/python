def title():
    print("=" * 45)
    print("       Biomedical Patient Record System")
    print("=" * 45)
    print()


def menu():
    print("""
1. Add Patient Record
2. View All Patients
3. Search Patient
0. Exit
""")


def add_patient(patients):
    print("\n--- Add New Patient ---")

    try:
        
        patient_id = len(patients) + 1

        name = input("Enter Name: ").strip().title()
        if not name:
            print("[Error] Name cannot be empty.\n")
            return

        age = int(input("Enter Age: "))
        if age <= 0:
            print("[Error] Age must be greater than 0.\n")
            return

        gender = input("Enter Gender: ").strip().title()
        blood_group = input("Enter Blood Group: ").strip().upper()
        diagnosis = input("Enter Diagnosis: ").strip().title()

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "blood_group": blood_group,
            "diagnosis": diagnosis
        }

        patients.append(patient)
        print(f"\n[Success] Record created for ID: {patient_id}\n")

    except ValueError:
        print("[Error] Invalid input. Age must be a number.\n")


def view_patients(patients):
    print("\n--- Current Patient Records ---")

    if not patients:
        print("No patient records found.\n")
        return

    
    print(f"{'ID':<4} {'Name':<20} {'Age':<5} {'Gender':<8} {'Blood':<8}")
    print("-" * 50)

    for patient in patients:
        
        print(
            f"{patient.get('id'):<4} "
            f"{patient.get('name'):<20} "
            f"{patient.get('age'):<5} "
            f"{patient.get('gender'):<8} "
            f"{patient.get('blood_group'):<8}"
        )

    print()


def search_patient(patients):
    print("\n--- Search Patient ---")

    if not patients:
        print("No patient records available.\n")
        return

    try:
        search_id = int(input("Enter Patient ID: "))
        found = False

       
        for patient in patients:
            if patient.get("id") == search_id:
                print(f"""
Patient Found
------------------------------
ID          : {patient.get('id')}
Name        : {patient.get('name')}
Age         : {patient.get('age')}
Gender      : {patient.get('gender')}
Blood Group : {patient.get('blood_group')}
Diagnosis   : {patient.get('diagnosis')}
------------------------------
""")
                found = True
                break

        if not found:
            print("Patient not found.\n")

    except ValueError:
        print("[Error] Please enter a valid numeric ID.\n")


def main():
    patients = []

    title()

    while True:
        menu()

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        if choice == 1:
            add_patient(patients)

        elif choice == 2:
            view_patients(patients)

        elif choice == 3:
            search_patient(patients)

        elif choice == 0:
            print("\nExiting Patient Record System...")
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()