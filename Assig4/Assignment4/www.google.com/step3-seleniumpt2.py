import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pyvirtualdisplay import Display

if __name__ == "__main__":

    count_a = 0 #only HTTPS
    count_b = 0 #both
    count_c = 0 #only HTTP
    count_d = 0 #neither

    #line_count = 70

    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Chrome()


    with open("step0-othersites.csv", "r") as input_file:
        # Open result CSV file for writing
        with open("step3-othersites-selenium.csv", "a", newline='') as output_file:
            # Create a CSV writer
            csv_writer = csv.writer(output_file)
            
            # Iterate through each row in the input CSV file
            for i, line in enumerate(input_file):
                if i < 284:
                    continue
                # Extract the URL and index from the line
                index, destination = line.split(",", 1)
                index = index.strip()
                destination = destination.strip()
                try:
                    driver.implicitly_wait(10)
                    # Make HTTP requests with both HTTP and HTTPS
                    r = driver.get("http://" + destination)
                    time.sleep(5)
                    f = driver.current_url
                    #timeout
                    try:
                        driver.implicitly_wait(10)
                        r_secure = driver.get("https://" + destination) #timeout
                        time.sleep(5)
                        f_secure = driver.current_url    
        
                        if f == f_secure:
                            # HTTPS only
                            row = [index, destination, "HTTPS only"]
                            count_a = count_a + 1
                        else:
                            # Both HTTP and HTTPS
                            row = [index, destination, "both"]
                            count_b = count_b + 1

                    except:
                        # HTTP only
                        row = [index, destination, "HTTP only"]
                        count_c = count_c + 1
                except:
                    # Neither
                    row = [index, destination, "neither"]
                    count_d = count_d + 1
                # Write the updated row to the output CSV file
                csv_writer.writerow(row)
                output_file.flush()
                print(i)
                #line_count += 1

    
    input_file.close()   
    output_file.close()
    driver.quit()
    #print(line_count)
    print("Selly Other only HTTPS: " + str(count_a))
    print("Selly Other both: " + str(count_b))
    print("Selly Other only HTTP: " + str(count_c))
    print("Selly Other Neither: " + str(count_d))                
                     
    exit()