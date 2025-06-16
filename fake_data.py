from faker import Faker

counter = 0
# Language options with corresponding Faker locales
language_options = {
    '1': ('English', 'en_US'),
    '2': ('Hebrew', 'he_IL'),
    '3': ('Italian', 'it_IT'),
    '4': ('Japanese', 'ja_JP'),
    '5': ('Arabic', 'ar_LB'),
}

def display_languages():
    print("\nChoose a language:")
    for key, (lang_name, _) in language_options.items():
        print(f"{key}. {lang_name}")

def generate_fake_data(fake):
    global counter
    counter += 1
    print("-" * 38 + f"{counter}")
    name = fake.name()
    address = fake.address()
    email = fake.email()
    phone = fake.phone_number()
    company = fake.company()

    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Company: {company}")
    print("-" * 40)

    return [name, address, email, phone, company]

def main():
    while True:
        display_languages()

        try:
            choice = input("Enter your choice ( 1-5 | 6 to Exit ): ").strip()
        except ValueError as e:
            return f"Not a valid number FAKER! - {e}"

        if choice == "6":
            print("See  U later FAKER")
            return
        
        if choice not in language_options:
            print("Invalid choice. Please select a valid option.")
            continue

        lang_name, locale = language_options[choice]
        fake = Faker(locale)
        print(f"\nYou selected: {lang_name}")

        generate_fake_data(fake)

if __name__ == "__main__":
    main()
