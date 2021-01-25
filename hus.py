age=input("Are you a cigarette addict older than 75 years old? Yes/No: ")

chronic=input("Do you have a severe chronic disease? Yes/No: ")

immune=input("Is your immune system too weak? Yes/No: ")

if (age.upper() or chronic.upper() or immune.upper()) == "YES":

    print("You are in risky group")

else:

    print("You are NOT in risky group")