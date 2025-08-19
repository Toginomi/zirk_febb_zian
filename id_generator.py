while True:
    first_name=input("Enter your first name here please: ")
    last_name=input("Enter your last name here please: ")
    email_address=input("Enter your email address please: ")
    phone_number=int(input("Enter your phone number please: "))
    job_title=input("Enter the name of your job please: "))
    id_number=int(input("Enter your ID number please: "))
    print(f"Your ID Badge is below:\n----------------------------\n{last_name.upper()}, {first_name.capitalize()}\nPhone Number: {phone_number}\n Job Title: {job_title.title()}\n ID Number: {id_number}\n\n Email Address: {email_address.lower()}\n Phone Number: {phone_number}\n----------------------------\n")
