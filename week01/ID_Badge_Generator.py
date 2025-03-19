print("Please enter the following information:\n")

first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email Address: ")
phone_number = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")
hair = input("Hair color: ")
eyes = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")

print("\nThe ID Card is:")
print("-" * 40)
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")
print(f"\n{email_address.lower()}")
print(f"{phone_number}")
print()
print(f"Hair: {hair.capitalize():<10} Eyes: {eyes.capitalize()}")
print(f"Month: {month.capitalize():<9} Training: {training.capitalize()}")
print("-" * 40)

# The ID Card is:
# ----------------------------------------
# DOE, Jane
# Chief Software Architect
# ID: 83-23821

# janedoe@email.com
# (208) 555-1234

# Hair: Brown           Eyes: Blue
# Month: September      Training: Yes
# ----------------------------------------