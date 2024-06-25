from tabulate import tabulate
import os

emergency_contacts = [
    {"No": 1, "Kota": "Jakarta", "Nomor Telepon Ambulans": "114", "Provinsi": "DKI Jakarta", "Jenis Rumah Sakit": "Pemerintah", "Negara": "Indonesia"},
    {"No": 2, "Kota": "Surabaya", "Nomor Telepon Ambulans": "112", "Provinsi": "Jawa Timur", "Jenis Rumah Sakit": "Swasta", "Negara": "Indonesia"},
    {"No": 3, "Kota": "Bandung", "Nomor Telepon Ambulans": "119", "Provinsi": "Jawa Barat", "Jenis Rumah Sakit": "Pemerintah", "Negara": "Indonesia"},
    {"No": 4, "Kota": "Yogyakarta", "Nomor Telepon Ambulans": "176", "Provinsi": "DI Yogyakarta", "Jenis Rumah Sakit": "Pemerintah", "Negara": "Indonesia"},
    {"No": 5, "Kota": "Denpasar", "Nomor Telepon Ambulans": "118", "Provinsi": "Bali", "Jenis Rumah Sakit": "Swasta", "Negara": "Indonesia"}
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_all_contacts():
    clear_screen()
    print("Select the filter option:")
    print("1. Show all contacts")
    print("2. Filter by Provinsi")
    print("3. Filter by Kota")
    print("4. Filter by Jenis Rumah Sakit")
    print("5. Search by Nomor Telepon Ambulans")  # Add this option
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        filtered_contacts = emergency_contacts
    elif choice == "2":
        provinsi = input("Enter the Provinsi: ")
        filtered_contacts = [contact for contact in emergency_contacts if contact["Provinsi"].lower() == provinsi.lower()]
    elif choice == "3":
        kota = input("Enter the Kota: ")
        filtered_contacts = [contact for contact in emergency_contacts if contact["Kota"].lower() == kota.lower()]
    elif choice == "4":
        jenis_rs = input("Enter the Jenis Rumah Sakit (Pemerintah/Swasta): ")
        filtered_contacts = [contact for contact in emergency_contacts if contact["Jenis Rumah Sakit"].lower() == jenis_rs.lower()]
    elif choice == "5":  # Add this condition
        nomor_telepon = input("Enter the Nomor Telepon Ambulans: ")
        filtered_contacts = [contact for contact in emergency_contacts if contact["Nomor Telepon Ambulans"] == nomor_telepon]
    else:
        print("Invalid choice.")
        return
    
    if filtered_contacts:
        print(tabulate(filtered_contacts, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No contacts found.")

def add_contact():
    clear_screen()
    while True:
        try:
            no = int(input("No: "))
            for contact in emergency_contacts:
                if contact["No"] == no:
                    print("Contact with the same No already exists. Please choose a different No.")
                    break
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for No.")
    
    while True:
        kota = input("Kota: ")
        if not kota.replace(" ", "").isalpha():
            print("Invalid input. Please enter alphabetic characters for Kota.")
        else:
            break
    
    while True:
        nomor_telepon = input("Nomor Telepon Ambulans: ")
        if not nomor_telepon.isdigit() or len(nomor_telepon) != 3:
            print("Invalid Nomor Telepon Ambulans. Enter a 3-digit numeric value.")
        elif any(contact["Nomor Telepon Ambulans"] == nomor_telepon for contact in emergency_contacts):
            print("Nomor Telepon Ambulans must be unique. Please choose a different value.")
        else:
            break
    
    while True:
        provinsi = input("Provinsi: ")
        if not provinsi.replace(" ", "").isalpha():
            print("Invalid input. Please enter alphabetic characters for Provinsi.")
        else:
            break
    
    while True:
        negara = input("Negara: ")
        if not negara.replace(" ", "").isalpha():
            print("Invalid input. Please enter alphabetic characters for Negara.")
        else:
            break
    
    jenis_rs = input("Jenis Rumah Sakit: ")
    
    if jenis_rs.lower() == 'p' or jenis_rs.lower() == 'pemerintah':
        jenis_rs = "Pemerintah"
    elif jenis_rs.lower() == 's' or jenis_rs.lower() == 'swasta':
        jenis_rs = "Swasta"
    else:
        print("Invalid Jenis Rumah Sakit. Enter 'p' or 'pemerintah' for Pemerintah or 's' or 'swasta' for Swasta.")
        return
    
    new_contact = {
        "No": no,
        "Kota": kota,
        "Nomor Telepon Ambulans": nomor_telepon,
        "Provinsi": provinsi,
        "Negara": negara,
        "Jenis Rumah Sakit": jenis_rs
    }
    emergency_contacts.append(new_contact)
    print("Contact added successfully!")

def delete_contact():
    clear_screen()
    while True:
        try:
            no = int(input("Enter the No of the contact to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for No.")
    
    index = -1
    for i, contact in enumerate(emergency_contacts):
        if contact["No"] == no:
            index = i
            break
    
    if index != -1:
        print("Are you sure you want to delete this contact?")
        confirmation = input("Enter 'yes' to confirm deletion, or 'no' to cancel: ")
        if confirmation.lower() in ['yes', 'y']:
            del emergency_contacts[index]
            print("Contact deleted successfully!")
        elif confirmation.lower() in ['no', 'n']:
            print("Contact deletion canceled.")
        else:
            print("Invalid input. Contact deletion canceled.")
    else:
        print("Contact not found!")

    # Display the available table
    show_all_contacts()

# Rest of the code...

def update_contact():
    clear_screen()
    while True:
        try:
            no = int(input("Enter the No of the contact to update: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for No.")
    
    index = -1
    for i, contact in enumerate(emergency_contacts):
        if contact["No"] == no:
            index = i
            break
    
    if index != -1:
        print("Select the columns to update:")
        print("1. Kota")
        print("2. Nomor Telepon Ambulans")
        print("3. Provinsi")
        print("4. Negara")
        print("5. Jenis Rumah Sakit")
        
        choice = input("Enter your choice (comma-separated): ")
        columns = choice.split(",")
        
        for column in columns:
            if column == "1":
                while True:
                    kota = input("Kota: ")
                    if not kota.replace(" ", "").isalpha():
                        print("Invalid input. Please enter alphabetic characters for Kota.")
                    else:
                        break
                emergency_contacts[index]["Kota"] = kota
            elif column == "2":
                while True:
                    nomor_telepon = input("Nomor Telepon Ambulans: ")
                    if not nomor_telepon.isdigit() or len(nomor_telepon) != 3:
                        print("Invalid Nomor Telepon Ambulans. Enter a 3-digit numeric value.")
                    elif any(contact["Nomor Telepon Ambulans"] == nomor_telepon for contact in emergency_contacts):
                        print("Nomor Telepon Ambulans must be unique. Please choose a different value.")
                    else:
                        break
                emergency_contacts[index]["Nomor Telepon Ambulans"] = nomor_telepon
            elif column == "3":
                while True:
                    provinsi = input("Provinsi: ")
                    if not provinsi.replace(" ", "").isalpha():
                        print("Invalid input. Please enter alphabetic characters for Provinsi.")
                    else:
                        break
                emergency_contacts[index]["Provinsi"] = provinsi
            elif column == "4":
                while True:
                    negara = input("Negara: ")
                    if not negara.replace(" ", "").isalpha():
                        print("Invalid input. Please enter alphabetic characters for Negara.")
                    else:
                        break
                emergency_contacts[index]["Negara"] = negara
            elif column == "5":
                jenis_rs = input("Jenis Rumah Sakit: ")
                if jenis_rs.lower() == 'p' or jenis_rs.lower() == 'pemerintah':
                    jenis_rs = "Pemerintah"
                elif jenis_rs.lower() == 's' or jenis_rs.lower() == 'swasta':
                    jenis_rs = "Swasta"
                else:
                    print("Invalid Jenis Rumah Sakit. Enter 'p' or 'pemerintah' for Pemerintah or 's' or 'swasta' for Swasta.")
                    return
                emergency_contacts[index]["Jenis Rumah Sakit"] = jenis_rs
            else:
                print(f"Invalid choice: {column}")
        
        valid_input = False
        while not valid_input:
            confirmation = input("Update contact? (yes/no): ")
            if confirmation.lower() in ['yes', 'y']:
                valid_input = True
                print("Contact updated successfully!")
            elif confirmation.lower() in ['no', 'n']:
                valid_input = True
                print("Contact not updated.")
            else:
                print("Invalid input. Enter 'yes' or 'no'.")
    else:
        print("Contact not found!")