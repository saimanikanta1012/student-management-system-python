# StudentUpdate.py
import pickle

def studUpdate():
    try:
        sno_to_update = int(input("Enter Student Number to update the Record Details: "))
        found = False
        updatedrecords = []

        # Read all records
        with open("student.pick", "rb") as f:
            while True:
                try:
                    record = pickle.load(f)
                    updatedrecords.append(record)
                except EOFError:
                    break

        # Search and update the required record
        for i in range(len(updatedrecords)):
            if updatedrecords[i][0] == sno_to_update:
                print("=" * 40)
                print("\t\tCurrent Details")
                print("=" * 40)
                print(f"Student Name       : {updatedrecords[i][1]}")
                print(f"Student Marks      : {updatedrecords[i][2]}")
                print(f"Student College    : {updatedrecords[i][3]}")
                print("=" * 40)
                print("Update New Details:")
                print("=" * 40)

                nsname = input("Enter New Name: ")
                try:
                    nmarks = int(input("Enter New Marks: "))
                except ValueError:
                    print("Invalid marks! Keeping previous.")
                    nmarks = updatedrecords[i][2]
                ncolname = input("Enter New College Name: ")

                # Update values
                if nsname.strip():
                    updatedrecords[i][1] = nsname
                updatedrecords[i][2] = nmarks
                if ncolname.strip():
                    updatedrecords[i][3] = ncolname

                found = True
                print("✅ Record updated successfully.")
                break

        if not found:
            print("❌ Student number not found.")

        # Write updated records back to the file
        with open("student.pick", "wb") as f:
            for record in updatedrecords:
                pickle.dump(record, f)

    except FileNotFoundError:
        print("⚠️ File not found.")
    except ValueError:
        print("❗ Please enter a valid number.")
