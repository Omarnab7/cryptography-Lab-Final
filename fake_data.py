from faker import Faker

counter = 0
# Language options with corresponding Faker locales
language_options = {
    '1': ('English', 'en_US'),
    '2': ('Hebrew', 'he_IL'),
    '3': ('Italian', 'it_IT'),
    '4': ('Japanese', 'ja_JP'),
}

def display_languages():
    print("\nChoose a language:")
    for key, (lang_name, _) in language_options.items():
        print(f"{key}. {lang_name}")

def generate_fake_data(fake):
    global counter
    counter += 1
    print("-" * 38 + f"{counter}")
    print(f"Name: {fake.name()}")
    print(f"Address: {fake.address()}")
    print(f"Email: {fake.email()}")
    print(f"Phone: {fake.phone_number()}")
    print(f"Company: {fake.company()}")
    print("-" * 40)

def main():
    while True:
        display_languages()

        try:
            choice = input("Enter your choice ( 1-4 | 5 to Exit ): ").strip()
        except ValueError as e:
            return f"Not a valid number FAKER! - {e}"

        if choice == "5":
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
