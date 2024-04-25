import json
from math import log, exp

def load_markov_model(filename):
    with open(filename, "r", encoding="utf8") as file:
        return json.load(file)

def calculate_password_probability(password, model):
    log_probability = 0.0
    
    starting_char = password[0]
    log_probability += log(model["Start"].get(starting_char))  
    
   
    for i in range(len(password) - 1):
        current_char = password[i]
        next_char = password[i + 1]
        log_probability += log(model.get(current_char).get(next_char)) 

    ending_char = password[-1]
    log_probability += log(model.get(ending_char).get("End"))  
    
    # Convert log probability back to norm
    probability = exp(log_probability)
    
    return probability

def main():
 
    markov_model = load_markov_model("markov_model_correct.json")
    
   
    with open("step4-input.txt", "r") as file:
        passwords = [line.strip() for line in file if line.strip()]
    
    
    with open("step4-output.txt", "w") as output_file:
        for password in passwords:
            probability = calculate_password_probability(password, markov_model)
            output_file.write(f"{password}\t{probability}\n")

if __name__ == "__main__":
    main()
