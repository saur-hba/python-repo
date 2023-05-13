command = ""
started = False
while True:
    command = input(">> ").lower()
    if command == "start":
        if started:
           print("Car has already started")
        else:
           started = True
           print("Car Started...")
    elif command == "stop":
        if not started:
           print("Car has already stopped")
        else:
           started = False
           print("Car stopped...")
    elif command == "help":
        print("""
Enter 'start' to start the car
Enter 'stop' to stop the car
Enter 'quit' to quit the game
             """)
    elif command == "quit":
       print("You moved out of the game")
       break
    else:
     print("Unsupported command")
