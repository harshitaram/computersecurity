import random

with open("rockyou.txt", "r", encoding="utf8", errors="ignore") as file:
    file.readline() #skip the first line which has the date

    passwords = file.readlines()

password_lengthfreq = {}
total_count = 0

unique_passwords = set()
unique_frequency = {}

for password in passwords:
    total_count += 1
    passy = password.strip()
    length = len(passy)
    if length not in password_lengthfreq:
        password_lengthfreq[length] = 1
    else:
        password_lengthfreq[length] += 1
    unique_passwords.add(passy)
    if passy in unique_passwords:
        if passy not in unique_frequency:
            unique_frequency[passy] = 1
        else:
            unique_frequency[passy] += 1


mode = max(password_lengthfreq, key=password_lengthfreq.get)

print(mode, password_lengthfreq[mode])

twelve_plus = 0
sixteen_plus = 0

for password_length in password_lengthfreq:
    if password_length >= 12:
        twelve_plus += password_lengthfreq[password_length]
    if password_length >= 16:
        sixteen_plus += password_lengthfreq[password_length]

print("At least 12 characters:", twelve_plus/total_count)
print("At least 16 characters:", sixteen_plus/total_count)
print("Total", total_count)


random_passwords = random.sample(list(unique_passwords), 10)

print(random_passwords)

password_frequency_list = [(password, unique_frequency[password]) for password in unique_passwords]

# Sort the list based on frequency in descending order
sorted_password_frequency = sorted(password_frequency_list, key=lambda x: x[1], reverse=True)

with open("ordered_passwordlist.txt", "w") as file:
    for password, frequency in sorted_password_frequency:
        file.write(password + "\n")

with open("ordered_passwordlist.txt", "r") as ordered_file:
    lines = ordered_file.readlines()[:1000]

# Write the first 1000 lines to step1.txt
with open("step1.txt", "w") as step1_file:
    for line in lines:
        step1_file.write(line)