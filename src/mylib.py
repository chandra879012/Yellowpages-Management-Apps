from tabulate import tabulate
import os

emergency_contacts = [
    {"No": 1, "Kota": "Jakarta", "Nomor Telepon Ambulans": "114", "Provinsi": "DKI Jakarta", "Jenis Rumah Sakit": "Pemerintah"},
    {"No": 2, "Kota": "Surabaya", "Nomor Telepon Ambulans": "112", "Provinsi": "Jawa Timur", "Jenis Rumah Sakit": "Pemerintah"},
    {"No": 3, "Kota": "Bandung", "Nomor Telepon Ambulans": "119", "Provinsi": "Jawa Barat", "Jenis Rumah Sakit": "Pemerintah"},
    {"No": 4, "Kota": "Yogyakarta", "Nomor Telepon Ambulans": "176", "Provinsi": "DI Yogyakarta", "Jenis Rumah Sakit": "Pemerintah"},
    {"No": 5, "Kota": "Denpasar", "Nomor Telepon Ambulans": "118", "Provinsi": "Bali", "Jenis Rumah Sakit": "Pemerintah"}
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_all_contacts():
    clear_screen()
    print(tabulate(emergency_contacts, headers="keys", tablefmt="fancy_grid"))

def add_contact():
    clear_screen()
    no = int(input("No: "))
    kota = input("Kota: ")
    nomor_telepon = input("Nomor Telepon Ambulans: ")
    provinsi = input("Provinsi: ")
    jenis_rs = input("Jenis Rumah Sakit: ")
    
    if jenis_rs.lower() == 'p' or jenis_rs.lower() == 'pemerintah':
        jenis_rs = "Pemerintah"
    elif jenis_rs.lower() == 's' or jenis_rs.lower() == 'swasta':
        jenis_rs = "Swasta"
    else:
        raise ValueError("Jenis Rumah Sakit tidak valid. Masukkan 'p' atau 'pemerintah' untuk Pemerintah atau 's' atau 'swasta' untuk Swasta.")
    
    new_contact = {
        "No": no,
        "Kota": kota,
        "Nomor Telepon Ambulans": nomor_telepon,
        "Provinsi": provinsi,
        "Jenis Rumah Sakit": jenis_rs
    }
    emergency_contacts.append(new_contact)
    print("Contact added successfully!")

def delete_contact():
    clear_screen()
    no = int(input("Enter the No of the contact to delete: "))
    index = -1
    for i, contact in enumerate(emergency_contacts):
        if contact["No"] == no:
            index = i
            break
    
    if index != -1:
        del emergency_contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def update_contact():
    clear_screen()
    no = int(input("Enter the No of the contact to update: "))
    index = -1
    for i, contact in enumerate(emergency_contacts):
        if contact["No"] == no:
            index = i
            break
    
    if index != -1:
        kota = input("Kota: ")
        nomor_telepon = input("Nomor Telepon Ambulans: ")
        provinsi = input("Provinsi: ")
        jenis_rs = input("Jenis Rumah Sakit: ")
        
        
        updated_contact = {
            "No": no,
            "Kota": kota,
            "Nomor Telepon Ambulans": nomor_telepon,
            "Provinsi": provinsi,
            "Jenis Rumah Sakit": jenis_rs
        }
        emergency_contacts[index] = updated_contact
        print("Contact updated successfully!")
    else:
        print("Contact not found!")