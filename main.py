import random
import string

def random_password(length,lowercase=False,uppercase=False,numbers=False,special=False):
    chars = string.ascii_letters

    if uppercase:
        chars += string.ascii_uppercase
    elif numbers:
        chars += string.digits
    elif special:
        chars += string.punctuation
    elif lowercase:
        chars += string.ascii_lowercase

    if not chars:
        return "Error: No characters selected for password generation!"    

    password = ''.join(random.choice(chars) for _ in range(length))   
    return password 


def main():
    length = int(input("Enter the length of the password : "))
    uppercase = input("The password should contain uppercase or not (yes/no) :  ").lower() == "yes"
    lowercase = input("Enter the password should contain lowercase letters or not (yes/no) : ").lower() == "yes"
    digits = input("Enter the password should contain digits or not (yes/no) : ").lower() == "yes"
    special = input("Enter the password should contain digits or not (yes/no) : ").lower() == "yes"

    password = random_password(length,lowercase,uppercase,digits,special)
    print("Your Generated Password is : ", password)

if __name__ == "__main__":
    main()    

