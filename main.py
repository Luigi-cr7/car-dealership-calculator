# Dealership name
dealership_name = "Madrid Enterprise"

# Print a welcome message
print(f"Welcome to {dealership_name}\n")

# Ask the customer which car they are intersted in
car_name = input("Which car are you interested in? ")

# Loop unitl a valid number is entered for the base price
while True:
    try:
        # Ask the customer how much they want to pay for the specific car they chose
        base_price = float(input(f"How much will you give us for the {car_name}? $"))

        # Check if the base price is a positive number
        if base_price > 0:
            break # Exit loop if the input is valid
        else:
            print("Please enter a positive number.")
    except ValueError:
                print("Invalid input. Please enter a valid number.")

# Define the fess
additional_dealer_markup = 1000
processing_fee = 100
destination_charge = 495
undercoating = 295
rust_proofing = 395
prep_fee = 250

# Calculate the sales tax and restocking fee
sales_tax = base_price * 0.05 # 5% of the base price
restocking_fee = base_price * 0.12 # 12% of the base price

# Calculate the total cost
total_cost = (base_price + additional_dealer_markup + processing_fee + destination_charge +
              undercoating + rust_proofing + prep_fee + sales_tax + restocking_fee)


# Print out the detailed cost breakdown
print(f"\n{car_name}")
print(f"Base Price:\t${base_price:,.2f}")
print(f"Additional Dealer Markup:\t${additional_dealer_markup:,.2f}")
print(f"Procesing Fee:\t${processing_fee:,.2f}")
print(f"Destination Charge:\t${destination_charge:,.2f}")
print(f"Undercoating:\t\t${undercoating:,.2f}")
print(f"Rust-Proofing:\t\t${rust_proofing:,.2f}")
print(f"Prep Fee:\t\t${prep_fee:,.2f}")
print(f"Sales Tax (5%):\t${sales_tax:,.2f}")
print(f"Restocking Fee (12%):\t${restocking_fee:,.2f}")
print(f"Total Cost:\t\t${total_cost:,.2f}")
