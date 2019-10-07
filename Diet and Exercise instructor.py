
#A function to show the recent time.
def getdate():
    import datetime
    return datetime.datetime.now()

#Dictionary of client.
client_list={1:"Mohan",2:"Rajan",3:"Lathor"}
#Instructor recommended list.
recommended_list={1:"Diet",2:"Exercise"}
#To log or retrieve option.
log_or_retrieve={1:"log",2:"retrieve"}

#Client dictionary process-
print()
print("Please select one of the client:")
for key,value in client_list.items():
    print(f"Press {key} for {value}")
try:
    client_name=int(input("Enter here:"))

    if client_name == 1 or client_name == 2 or client_name == 3:
        print(f"You have selected to {client_list[client_name]}")

    #Instructor recommended dictionary process-
    print()
    print("Please select the recommended option:")
    for key,value in recommended_list.items():
        print(f"Press {key} for {value}")
    recommended_name=int(input("Enter here:"))
    if recommended_name == 1 or recommended_name == 2:
        print(f"You have selected to {recommended_list[recommended_name]}")

    #Option for log or retrieve
    print()
    print("sir/Ma'am what you want to do [log or retrieve] :")
    for key,value in log_or_retrieve.items():
        print(f"Press {key} for {value}")
    log_or_retrieve_input=int(input("Enter here:"))

    #if User select log then it will create a new file for that.
    if log_or_retrieve_input == 1:
        print("You have selected to log:")
        print("Generating: "+client_list[client_name]+"_"+recommended_list[recommended_name]+" type schedule:")
        file=open(client_list[client_name]+"_"+recommended_list[recommended_name]+".txt","a")
        repeat="y"
        while repeat not in "n":
            input_txt=input(f"Enter the recommended to do {recommended_list[recommended_name]}:")
            file.write("["+str(getdate())+"]" + input_txt + "\n")
            repeat=input("Press y to continue or n to stop:")
            continue
        file.close()

    #if retrieve then it will show what the instructor gave the advice to client.
    elif log_or_retrieve_input == 2:
        print("You have selected to retrieve:")
        print(client_list[client_name]+"_"+recommended_list[recommended_name]+" Report:")
        file=open(client_list[client_name]+"_"+recommended_list[recommended_name]+".txt","rt")
        contant=file.readlines()
        for line in contant:
            print(line,end="")
        file.close()
    else:
        print("Please put the correct number to proceed")
except:
    print("[You are not allow to give these option see above you have type wrong input..]")

