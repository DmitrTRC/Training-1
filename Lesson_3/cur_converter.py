from forex_python.converter import CurrencyRates

rates = CurrencyRates()
if input('Do you need currency exchange table ? y/n -> ').lower() == 'y':
    for cur in rates.get_rates('RUB'):
        print(f'{cur}   :   {rates.get_rate(cur, "RUB"):.2f} Rub.')

amount = float(input('Enter the amount -> '))
source_currency = input('Enter the source currency -> ').upper()
target_currency = input('Enter target currency -> ').upper()
result = rates.convert(source_currency, target_currency, amount)
print(f'{amount} {source_currency} is {result} {target_currency} ')
