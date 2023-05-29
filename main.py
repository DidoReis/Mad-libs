def mad_libs():
    # Welcome message
    print("Welcome to Mad Libs!")
    print("")

    # Getting user input
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb in infinitive form: ")

    # Printing the filled story
    print("")
    print("Story:")
    print("The", adjective, noun, verb, "in the park.")

# Calling the function to start the game
mad_libs()
