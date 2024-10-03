import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    This function encrypts the email by assigning variables to the email.

    Args:
        This defines how the email encrypts, must be 6 characters.

    Returns:
        str: The encrypted email or an error message if validation fails.
    """
    output = "" 
    len_flag = len(email) != 6

    # This function validates the length of the email
    if len_flag:  
        output = "Length check failed\nEmail must be 6 characters long."
        logging.info(output)
        return output        

    # This function tells the computer to give an error if the email is longer than 6 characters 
    if not (email[:3].isalpha() and email[3:].isdigit()):  
        output = "Validation failed\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     

    email_lst = list(email)

    for i in range(len(email_lst)):
        if email_lst[i].isalpha():  
            email_lst[i] = chr((ord(email_lst[i]) - ord('a') + 3) % 26 + ord('a'))
        elif email_lst[i].isdigit():  
            email_lst[i] = str((int(email_lst[i]) + 3) % 10)  

    # This converts the list back into a string using the .join function 
    email_str = ''.join(email_lst)
    return email_str 

def decrypt(email="def345"):
    """
    This function decrypts the input email by shifting characters down by 3.

    Args:
        email (str): The email to decrypt, expected to be 6 alphanumeric characters.

    Returns:
        str: The decrypted email or an error message if validation fails.
    """
    output = "" 
    len_flag = len(email) != 6

    # Validate length
    if len_flag:  
        output = "Length check failed\nEmail must be 6 characters long."
        logging.info(output)
        return output        

    # Validate format: 3 letters followed by 3 digits
    if not (email[:3].isalpha() and email[3:].isdigit()):  
        output = "Validation failed\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # Process the email string into a list
    email_lst = list(email)

    # Shift each character down by 3
    for i in range(len(email_lst)):
        if email_lst[i].isalpha():  
            # Handle wrap-around for letters
            email_lst[i] = chr((ord(email_lst[i]) - ord('a') - 3) % 26 + ord('a'))
        elif email_lst[i].isdigit():  
            email_lst[i] = str((int(email_lst[i]) - 3) % 10)  

    # Convert list back to string
    email_str = ''.join(email_lst)
    return email_str 

def main():
    email = 'abc012'
    enc = encrypt(email)
    print(f"{email} is now {enc}\n")

    dmail = 'def345'
    dec = decrypt(dmail)
    print(f"{enc} is now {dec}\n")
    # Runs the code 
if __name__ == "__main__":
    main()
