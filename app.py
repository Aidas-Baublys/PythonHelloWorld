is_started = False

while True:
    command = input("> ").upper()

    if command == "HELP":
        msg = """
Type:
    
help - shows this explanation.
start - starts the car.
stop - stops the car.
quit - exits the program.
    
Press enter to execute.
    """
    elif command == "START":
        if is_started:
            msg = "Car already started"
        else:
            is_started = True
            msg = "Car started, ready to GTA"
    elif command == "STOP":
        if is_started:
            is_started = False
            msg = "Car stopped"
        else:
            msg = "Car already stopped"
    elif command == "QUIT":
        print("Bey!")
        break
    else:
        msg = "Sorry, bro, no comprende"

    print(msg)
