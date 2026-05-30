#made on 1/30/26
#I wanted to make a currency converter that can ask teh user for the currency it would like to change into USD
#I had fun making this!
def currency_converter():
    while True:
        print('Hello user! Welcome to currency converter.')
        print('Please choose the currency you would like to exchange into USD')
        chosen_currency = input('Enter currency here: ').lower()
        if chosen_currency == 'pesos':
            user_current_amount = float(input('Enter pesos amount here:'))
            exchange_rate = 3669.26
            print(
                f'The USD equivalent for {user_current_amount} {chosen_currency} is {user_current_amount * exchange_rate}')
        elif chosen_currency == 'soles':
            user_current_amount = float(input('Enter soles amount here:'))
            exchange_rate = 0.3
            print(
                f'The USD equivalent for {user_current_amount} {chosen_currency} is {user_current_amount * exchange_rate} USD')
        elif chosen_currency == 'reais':
            user_current_amount = float(input('Enter reais amount here:'))
            exchange_rate = 0.19
            print(
                f'The USD equivalent for {user_current_amount} {chosen_currency} is {user_current_amount * exchange_rate} USD')
        elif chosen_currency == 'rupees':
            user_current_amount = float(input('Enter rupees amount here:'))
            exchange_rate = 91.68
            print(
                f'The USD equivalent for {user_current_amount} {chosen_currency} is {user_current_amount * exchange_rate} USD')
        else:
            print('That currency is not in my database. Sorry!')
        print('Would you like to convert again?')
        calculate_again = input('Enter yes or no:').lower()
        if calculate_again == 'yes':
            continue
        else:
            print('Ok! Have a good day user!')
        break


currency_converter()

