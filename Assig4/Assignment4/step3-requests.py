import requests
import csv

if __name__ == "__main__":  
    count_a = 0 #only HTTPS
    count_b = 0 #both
    count_c = 0 #only HTTP
    count_d = 0 #neither

    ##measure for top sites 
    with open("step0-topsites.csv", "r") as input_file:
        # Open result CSV file for writing
        with open("step3-topsites-requests.csv", "a", newline='') as output_file:
            # Create a CSV writer
            csv_writer = csv.writer(output_file)
    
            # Iterate through each row in the input CSV file
            for i, line in enumerate(input_file):
                if i < 823:
                    continue
                # Extract the URL and index from the line
                index, destination = line.split(",", 1)
                index = index.strip()
                destination = destination.strip()

                try:
                    # Make HTTP requests with both HTTP and HTTPS
                    r = requests.get("http://" + destination, timeout= 10)
                    s = r.status_code
                    f = r.url

                    try:
                        r_secure = requests.get("https://" + destination, timeout= 10)
                        s_secure = r_secure.status_code
                        f_secure = r_secure.url
                        if s != s_secure:
                            s = s_secure ##only print HTTPS code if it is different from HTTP code (ED post #268)
                        if f == f_secure:
                            # HTTPS only
                            row = [index, destination, "HTTPS only", s]
                            count_a = count_a + 1
                        else:
                            # Both HTTP and HTTPS
                            row = [index, destination, "both", s]
                            count_b = count_b + 1

                    except:
                        # HTTP only
                        row = [index, destination, "HTTP only", s]
                        count_c = count_c + 1
                except:
                    # Neither
                    row = [index, destination, "neither", ""]
                    count_d = count_d + 1
                # Write the updated row to the output CSV file
                csv_writer.writerow(row)
                output_file.flush()
                print(i)

    input_file.close()   
    output_file.close()

    print("TOP only HTTPS: " + str(count_a))
    print("TOP both: " + str(count_b))
    print("TOP only HTTP: " + str(count_c))
    print("TOP Neither: " + str(count_d)) 


"""  count_ao = 0 #only HTTPS
    count_bo = 0 #both
    count_co = 0 #only HTTP
    count_do = 0 #neither

    ##measure for Other Sites
    with open("step0-othersites.csv", "r") as input_file:
        # Open result CSV file for writing
        with open("step3-othersites-requests.csv", "a", newline='') as output_file:
            # Create a CSV writer
            csv_writer = csv.writer(output_file)

            # Iterate through each row in the input CSV file
            for i, line in enumerate(input_file):
                # Extract the URL and index from the line
                if i < 694:
                    continue
                index, destination = line.split(",", 1)
                index = index.strip()
                destination = destination.strip()
                try:
                    # Make HTTP requests with both HTTP and HTTPS
                    r = requests.get("http://" + destination, timeout = 10)
                    s = r.status_code
                    f = r.url

                    try:
                        r_secure = requests.get("https://" + destination, timeout = 10)
                        s_secure = r_secure.status_code
                        f_secure = r_secure.url
                        if s != s_secure:
                            s = s_secure ##only print HTTPS code if it is different from HTTP code (ED post #268)
                        if f == f_secure:
                            # HTTPS only
                            row = [index, destination, "HTTPS only", s]
                            count_ao = count_ao + 1
                        else:
                            # Both HTTP and HTTPS
                            row = [index, destination, "both", s]
                            count_bo = count_bo + 1
                    except:
                        # HTTP only
                        row = [index, destination, "HTTP only", s]
                        count_co = count_co + 1
                except:
                    # Neither
                    row = [index, destination, "neither", ""]
                    count_do = count_do + 1
                # Write the updated row to the output CSV file
                csv_writer.writerow(row)

    input_file.close()   
    output_file.close()
    

    print("OTHER only HTTPS: " + str(count_ao))
    print("OTHER both: " + str(count_bo))
    print("OTHER only HTTP: " + str(count_co))
    print("OTHER Neither: " + str(count_do))
 """

exit()


