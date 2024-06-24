from mylib import show_all_contacts, add_contact, delete_contact, update_contact, clear_screen

def main():
    while True:
        print("Yellow Pages - Emergency Ambulance Contacts")
        print("1. Show all contacts")
        print("2. Add contact")
        print("3. Delete contact")
        print("4. Update contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_all_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            clear_screen()
            print("Thank You For Using YellowPages...")
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()