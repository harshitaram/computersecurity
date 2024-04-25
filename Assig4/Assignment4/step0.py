import sys

#, file = resultFile

if __name__ == "__main__":
    resultFile1 = open('step0-topsites.csv', 'w') #https://howtodoinjava.com/python-examples/python-print-to-file/
    resultFile2 = open('step0-othersites.csv', 'w')

    with open("tranco-1m-2024-01-25.csv", 'r') as file:  #r for read 
        #create top 1000 file
        count = 0 
        for i in file: #https://stackoverflow.com/questions/1767513/how-to-read-first-n-lines-of-a-file
            print(i, end='', file=resultFile1) #https://learnpython.com/blog/python-print-function/
            count+= 1
            if count == 1000:
                break
        #create every 1000th file
    resultFile1.close()

    with open("tranco-1m-2024-01-25.csv", 'r') as file:
            for i, line in enumerate(file): #use of enumerate in for loop to iterate through file: https://stackoverflow.com/questions/6473283/basic-python-file-io-variables-with-enumerate
                if 1999 <= i <= 1000000 and (i - 1999) % 1000 == 0: #use modulo to skip to every 1000th value 
                    print(line, end='', file=resultFile2)
    
    resultFile2.close()
    file.close()
    exit()