import random
import string

def generate_password():
    print("--- Password Generator ---")
    length = int(input("Password ki length kitni chahiye? "))
    
    # Symbols, numbers aur letters ka mixture
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    
    print(f"Aapka naya password: {password}")

generate_password()