while True:
    command = input("> ").upper()

    if command == "HELP":
        msg = """
    type:
    
    help - shows this explanation.
    start - starts the car.
    stop - stops the car.
    quit - exits the program.
    """
    elif command == "START":
        msg = "Car started, ready to GTA"
    elif command == "STOP":
        msg = "Car stopped"
    elif command == "QUIT":
        print("Bey!")
        break
    else:
        msg = "Sorry, bro, no comprende"

    print(msg)
