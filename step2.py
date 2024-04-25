with open('shadow', 'r') as file:
    crackme_info = [line.split(':')[1] for line in file if line.startswith('crackme')]


with open('step2.txt', 'w') as output_file:
    output_file.write('\n'.join(crackme_info))
