print(":currency_exchange: Nigerian Currency Converter")
try:
    # Ask for inputs
    amount_naira = float(input("Enter amount in Naira (₦): "))
    rate_usd = float(input("Enter exchange rate to US Dollars ($): "))
    rate_gbp = float(input("Enter exchange rate to British Pounds (£): "))
    # Control flow check
    if amount_naira < 0:
        print("Amount in Naira cannot be negative.")
    elif rate_usd <= 0 or rate_gbp <= 0:
        print("Exchange rates must be greater than zero!")
    else:
        # Conversion
        usd = amount_naira / rate_usd
        gbp = amount_naira / rate_gbp
        # Print table
        print("\n\t:currency_exchange: NIGERIAN CURRENCY CONVERTER")
        print("\t------------------------------------")
        print(f"\tAmount in Naira:    ₦{amount_naira:,.2f}")
        print(f"\tEquivalent in USD:  ${usd:,.2f}")
        print(f"\tEquivalent in GBP:  £{gbp:,.2f}")
        print("\t------------------------------------")
except ValueError:
    print("Invalid input! Please enter numbers only.")
finally:
    print("Thank you for using the Nigerian Currency Converter!")