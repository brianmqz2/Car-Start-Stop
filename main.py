command = ""
started = False
while True:
    command = input(">").lower()
    if command == "help":
        print("""start - to start car
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("The car has already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("I dont understand that...")
