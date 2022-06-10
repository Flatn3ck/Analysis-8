from models.enums import authentication_level
from datetime import datetime
import utils.database as db
from utils.encryption import encrypt
import utils.value_checks as value_checks, secret

def create_advisor_or_admin(role):
    """
    This function creates an advisor or a system administrator account.
    """
    if role == "advisor":
        authentication_level = int(encrypt(str(1), secret.SECRET_KEY))
    elif role == "system_administrator":
        authentication_level = int(encrypt(str(2), secret.SECRET_KEY))

    # first name
    first_name = input("Enter first name: ")
    while not value_checks.is_valid_name(first_name):
        first_name = input("Enter first name: ")
    first_name_enc = encrypt(first_name, secret.SECRET_KEY)
    
    # last name
    last_name = input("Enter last name: ")
    while not value_checks.is_valid_name(last_name):
        last_name = input("Enter last name: ")
    last_name_enc = encrypt(last_name, secret.SECRET_KEY)
    
    # username
    username = input("Enter username: ")
    while not value_checks.is_valid_username(username):
        username = input("Enter username: ")
    username_enc = encrypt(username, secret.SECRET_KEY)
    
    # password
    password = input("Enter password: ")
    while not value_checks.is_valid_password(password):
        print("Password not following the requirements, try again")
        password = input("Enter password: ")
    password_enc = encrypt(password, secret.SECRET_KEY)
    
    # automatically add current date as registration date
    registration_date = str(datetime.today())
    
    # Encrypting first name, last name, street, house number, zip code, city, email, mobile phone
    db.insert_advisor(authentication_level, first_name_enc, last_name_enc, username_enc, password_enc, registration_date)
    if role == "advisor":
        print("Advisor registered")
    elif role == "system_administrator":
        print("System administrator registered")
    return