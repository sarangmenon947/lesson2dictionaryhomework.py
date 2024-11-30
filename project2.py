# Function to create a dictionary from user input
def create_user_dict():
    user_info = {}
    
    # Collecting Basic Details From The User
    user_info['name'] = input("Enter your name: ")
    user_info['age'] = input("Enter your age: ")
    user_info['city'] = input("Enter your city: ")
    
    return user_info

# Function To Update A Specific Value In The Dictionary
def update_user_info(user_info):
    print("\nCurrent details:")
    for key, value in user_info.items():
        print(f"{key}: {value}")
    
    # Asking Which Detail To Update
    key_to_update = input("\nWhich detail would you like to update (name, age, city)? ").strip()
    
    if key_to_update in user_info:
        new_value = input(f"Enter new value for {key_to_update}: ")
        user_info[key_to_update] = new_value
        print(f"{key_to_update} updated successfully!")
    else:
        print("Invalid key. No changes made.")

# Main Execution
if __name__ == "__main__":
    user_details = create_user_dict()
    
    # Printing The Initial Dictionary
    print("\nUser details:", user_details)
    
    # Updateing A Specified Value In The Dictionary
    update_user_info(user_details)
    
    # Printing The Updated Dictionary
    print("\nUpdated User details:", user_details)
