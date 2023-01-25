import requests

sheety_endpoint = "https://api.sheety.co/ebbf7d484406c0881977170c10e6d0cf/copyOfFlightDeals/users"


print("Welcome to Prisoe's Flight Club.\nWe find the best deals and email you.")
first_name = input("What is your first name?: ").title()
last_name = input("What is your last name?: ").title()
email = input("What is your email?: ").lower()
confirmed_email = input("Enter email again for confirmation: ").lower()

def email_confirmation():
    if confirmed_email == email:
        return confirmed_email
    else:
        print("Emails do not match")


if email_confirmation():
    # print(confirmed_email)
    parameters = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": confirmed_email
        }
    }
    try:
        response = requests.post(url=sheety_endpoint, json=parameters)
        response.raise_for_status()
    except KeyError():
        print("Emails do not match")
    finally:
        print(response.text)
        print("Welcome to the club!")

email_confirmation()