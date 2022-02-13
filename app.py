while True:
    command = input("> ")
    formatted_command = command.upper()

    if formatted_command == "HELP":
        msg = """
    type:
    
    help - shows this explanation.
    start - starts the car.
    stop - stops the car.
    quit - exits the program.
    """
    elif formatted_command == "START":
        msg = "Car started, ready to GTA"
    elif formatted_command == "STOP":
        msg = "Car stopped"
    elif formatted_command == "QUIT":
        print("Bey!")
        break
    else:
        msg = "Sorry, bro, no comprende"

    print(msg)
