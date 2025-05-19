# Fake Data Generator

This Python script generates fake personal and business data using the [Faker](https://faker.readthedocs.io/en/master/) library. It allows users to choose the language/locale for the fake data, and repeatedly generate new entries in that language until they choose to exit.

---

## Features

- Supports multiple languages:
  - English (`en_US`)
  - Hebrew (`he_IL`)
  - Italian (`it_IT`)
  - Japanese (`ja_JP`)
- Generates fake:
  - Name
  - Address
  - Email
  - Phone Number
  - Company
- Uses a counter to label each generated entry
- Runs in an interactive loop until the user chooses to exit

---

## Code Structure

### Language Options

```python
language_options = {
    '1': ('English', 'en_US'),
    '2': ('Hebrew', 'he_IL'),
    '3': ('Italian', 'it_IT'),
    '4': ('Japanese', 'ja_JP'),
}
```

### Functions

- `display_languages()`: Prints the list of supported languages.
- `generate_fake_data(fake)`: Prints fake data for the selected locale.
- `main()`: Main loop that prompts the user to select a language or exit.

---

## Requirements

Install the Faker library before running the script:

```bash
pip install faker
```

---

## Usage

Run the script in a Python environment:

```bash
python fake_data.py
```

Follow the prompts to choose a language and generate data.
