from password_logic import generate_password

def main():
    print("Welcome to my simple Python password generator")

    length_str = input("Enter password length: ").strip()
    if length_str.isdigit():
        length = int(length_str)
    else:
        length = 12

    special_chars_prompt = input("Special characters? (y/n): ").lower().strip()
    use_special_chars = (special_chars_prompt != "n")

    password = generate_password(length=length, use_special_chars=use_special_chars)

    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()