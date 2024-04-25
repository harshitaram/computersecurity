import json
import random

def generate_password(model):
    password = ''
    current_char = random.choices(list(model["Start"].keys()), weights=list(model["Start"].values()))[0]
    
    while current_char != 'End':
        password += current_char
        next_char = random.choices(list(model[current_char].keys()), weights=list(model[current_char].values()))[0]
        current_char = next_char
    
    return password

def main():
   
    with open("markov_model_correct.json", "r", encoding="utf8") as file:
        model = json.load(file)
    
    

    passwords = [generate_password(model) for _ in range(1000)]
    

    with open("generated_passwords.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")

if __name__ == "__main__":
    main()
