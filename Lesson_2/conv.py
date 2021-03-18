from forex_python.converter import CurrencyRates

rates = CurrencyRates()

while True:
    try:
        amount = float(input('Enter the amount (0 - for EXIT)  -> '))
        if not amount: break
        from_currency = input("From Currency: ").upper()
        to_currency = input("To Currency: ").upper()
        print(from_currency, " To ", to_currency, amount)
        result = rates.convert(from_currency, to_currency, amount)
        print(result)
    except ValueError:
        print('Wrong value!')
