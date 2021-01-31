import requests

params = {'access_key': '855f177bb3e58718e9f6d64168aa674f', 'currencies': 'USD,EUR,INR,CAD', 'format': 1}

taking_response = requests.get('http://apilayer.net/api/live', params = params)

live_data = taking_response.json()

def live_currency():
    "Welcome to Live Currency Convetor"
    user_input = int(input('''[1] :: INR to USD\n[2] :: USD to INR\n[3] :: USD to EUR\n[4] :: EUR to USD\n[5] :: INR to EUR\n[6] :: EUR to INR\n'''))
    if user_input == 1:
        inr = float(input('Enter INR Amount : '))
        usd = inr / live_data['quotes']['USDINR']
        print("Current Exchange Rate :", live_data['quotes']['USDINR'])
        print("USD Amount : ",usd)
    elif user_input == 2:
        usd = float(input("Enter USD Amount : "))
        inr = usd * live_data['quotes']['USDINR']
        print("Current Exchange Rate :",live_data['quotes']['USDINR'])
        print("INR Amount : ",inr)
    elif user_input == 3:
        usd = float(input("Enter USD Amount : "))
        eur = usd * live_data ['quotes']['USDEUR']
        print("Current Exchange Rate :", live_data['quotes']['USDEUR'])
        print("EUR Amount : ",eur)
    elif user_input == 4:
        eur = float(input("Enter EUR Amount : "))
        usd = eur / live_data['quotes']['USDEUR']
        print("Current Exchange Rate :", live_data['quotes']['USDEUR'])
        print("EUR Amount : ", usd)
    elif user_input == 5:
        inr = float(input("Enter INR Amount : "))
        eur = (inr / live_data['quotes']['USDINR']) * live_data['quotes']['USDEUR']
        print("Current Exchange Rate :", (1/live_data['quotes']['USDINR'])*live_data['quotes']['USDEUR'])
        print("EUR Amount : ", eur)
    elif user_input == 6:
        eur = float(input("Enter EUR Amount : "))
        inr = (eur / live_data['quotes']['USDEUR']) * live_data['quotes']['USDINR']
        print("Current Exchange Rate :", (1/live_data['quotes']['USDEUR'])*live_data['quotes']['USDINR'])
        print("INR Amount : ", inr)
live_currency()
print('''Thank you for using this Tool
Made with ❤''')