import json
from collections import defaultdict

def train_markov_model(data):
    
    model = defaultdict(lambda: defaultdict(int)) 
    
    
    for password in data:
        if not password: #skip blank line
            continue
       

        model["Start"][password[0]] += 1

        for i in range(len(password) - 1):
            current_char = password[i]
            next_char = password[i + 1]
            
            
            model[current_char][next_char] += 1
    
        model[next_char]["End"] += 1
   
    for current_char in model: #count to probability
        total_count = sum(model[current_char].values())
        for next_char in model[current_char]:
            model[current_char][next_char] /= total_count
    
    return model

def main():
    
    with open("rockyou.txt", "r", encoding="utf8", errors="ignore") as file:
        file.readline()  # Skip the first line which has the date
        data = [line.strip() for line in file if line.strip()]
    
   
    markov_model = train_markov_model(data)
    
   
    with open("markov_model_correct.json", "w", encoding="utf8") as file:
        json.dump(markov_model, file, ensure_ascii=False)

if __name__ == "__main__":
    main()
