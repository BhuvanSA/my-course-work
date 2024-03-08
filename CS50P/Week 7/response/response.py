from validator_collection import validators

data = input("What's your email address? ").strip()

try:
    email_address = validators.email(data)
    print("Valid")
except:
    print("Invalid")
