def pizza_order():
    print("Hello! Welcome to our pizza restaurant!")
    print("What can I get for you today?")
    print("Please provide your pizza toppings separated by commas.")

    toppings_input = input("> ")
    toppings = [topping.strip() for topping in toppings_input.split(",")]

    print("Great! Now, let's choose the size of your pizza.")
    print("We have small, medium, and large sizes.")
    size_input = input("> ")
    size = size_input.lower()

    print("Awesome! Would you like any extra toppings?")
    print("Please provide the extra toppings separated by commas, or enter 'none' if you don't want any.")
    extra_toppings_input = input("> ")
    extra_toppings = [topping.strip() for topping in extra_toppings_input.split(",")]

    print("Alright! Finally, would you like any drinks with your order?")
    print("Please provide the drink options separated by commas, or enter 'none' if you don't want any.")
    drinks_input = input("> ")
    drinks = [drink.strip() for drink in drinks_input.split(",")]

    print("Thank you for your order!")
    print("Here is your order summary:")
    print("Pizza Toppings:", toppings)
    print("Pizza Size:", size)
    print("Extra Toppings:", extra_toppings)
    print("Drinks:", drinks)
    print("Total Price: $XX.XX")

#Rendelés generálása
    order_form = "Pizza Toppings: {', '.join(toppings)}\n"
    order_form += "Pizza Size: {size}\n"
    order_form += "Extra Toppings: {', '.join(extra_toppings)}\n"
    order_form += "Drinks: {', '.join(drinks)}\n"
    order_form += "Total Price: $XX.XX\n"


    print("That's it for now. Have a nice day!")

#Pizza rendelés megkezdése
pizza_order()
