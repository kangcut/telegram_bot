import requests
from prettyprinter import pprint

def webhook(token):
    wh = requests.get(f"https://api.telegram.org/bot{token}/getwebhookinfo")
    result = wh.json()['result']['url']

    if not len(result):
       choice = input("\nwebhook is not set yet. do you wanna set webhook? (y/n): \n")
       yon = choice.upper()
       if yon == 'Y':
        uri = input("\nwebhook url: ")
        sethook = requests.get(f"https://api.telegram.org/bot{token}/setWebhook?url={uri}")
        disphook = sethook.json()
        pprint(disphook)
       else:
        exit()
       #print("\nwebhook is already set for your telegram bot\n")
       #pprint(result)
    else:
       print("\nwebhook is already set for your telegram bot\n")
       #pprint(result)
       #choice = input("\nwebhook is not set yet. do you wanna set webhook? (y/n): \n")
       #yon = choice.upper()
       #if yon == 'Y':
       #  uri = input("\nwebhook url: ")
       #  sethook = requests.get(f"https://api.telegram.org/bot{token}/setWebhook?url={uri}")
       #  disphook = sethook.json()
       #  pprint(disphook)
       #else:
       # exit()
         

tok = input("\nplease input your telegram bot token: ")

webhook(tok)

