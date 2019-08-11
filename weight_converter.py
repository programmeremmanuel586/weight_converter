# calculates and converts user weight from pounds to kilograms

def kilograms_to_pounds():
    user_kilograms = input("Your weight in kg: ")
    user_pounds = float(user_kilograms) * 2.20462
    print("Your weight in pounds: " + str(user_pounds))

def pounds_to_kilograms():
    user_pounds = input("Your weight in lbs: ")
    user_kilograms = int(user_pounds) * 0.453592
    print("Your weight in kilograms: " + str(user_kilograms))


def user_weight():
    user_name = input("What is your name? (You don't have to enter your full name) ")
    weight_choice = input("Welcome, " + user_name + ", to the weight converter! Would you like to convert your weight into"
                                                    "pounds or kilograms?\nPick one of the following\nPounds (lbs)"
                                                    " or Kilograms (kg): ").lower()
    if weight_choice == "lbs" or weight_choice == "pounds":
        kilograms_to_pounds()
        print("Enjoy your day, " + user_name + " :D")
    elif weight_choice == "kg" or weight_choice == "kilograms":
        pounds_to_kilograms()
        print("Enjoy your day, " + user_name + " :D")
    else:
        print("Your selection was invalid.")


user_weight()
