from forex_python.converter import CurrencyRates

rates = CurrencyRates()

amount = float(input('Enter amount -> '))
source_currency = input('Enter the source currency -> ').upper()
target_currency = input('Enter target currency -> ').upper()
result = rates.convert(source_currency, target_currency, amount)
print(f'{amount} {source_currency} is {result} {target_currency} ')
