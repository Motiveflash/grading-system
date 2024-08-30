# Sample credentials stored as a dictionary
# In a real application, this data would be stored in a database and passwords would be hashed.
credentials = {
    "user1": "password123",
    "user2": "mypassword",
    "admin": "adminpass"
}

def login(username, password):
    """
    Function to check the validity of the user's credentials.

    :param username: str: The username entered by the user.
    :param password: str: The password entered by the user.
    :return: bool: True if credentials are valid, False otherwise.
    """
    # Check if the username exists in the credentials dictionary
    if username in credentials:
        # Check if the password matches
        if credentials[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid password. Please try again.")
            return False
    else:
        print("Username not found. Please try again.")
        return False

# Example usage
if __name__ == "__main__":
    # Get the username and password from the user
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
    
    # Check the credentials
    if login(input_username, input_password):
        print("Access granted.")
    else:
        print("Access denied.")
