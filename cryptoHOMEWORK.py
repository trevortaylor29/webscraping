from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys
from twilio.rest import Client

url = 'https://cryptoslate.com/coins/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)


webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

tablecells = soup.findAll('td')



counter = 1


for x in range(5):
    name = tablecells[counter].text
    price = tablecells[counter + 1].text
    change = tablecells[counter+2].text
    changeC = tablecells[counter+1].text.replace(',', '')
    changeP = float(changeC.replace('$',''))
    change_to_decimal = float(change.replace('%','')) * .01
    calculation = changeP * change_to_decimal

    print(f'Name: {name}')
    print(f'Price: {price}')
    print(f"% change in 24hr: {change}")
    print(f"Price changed by: ${calculation}")
    print()
    print()
    counter += 10

#bitcoin text

btc_string = tablecells[2].text.replace(',','')
btc_no_dollarsign = float(btc_string.replace('$', ''))

if btc_no_dollarsign < 40000:
    client = Client(keys.accountSID, keys.authToken)

    twilionumber = '+16693568831'
    myCellphone = '+18325809005'

    textmsg = client.messages.create(to=myCellphone,from_=twilionumber, body='Bitcoin value is less than $40,000')

    print(f'Bitcoin text status: {textmsg.status}')

# Ethereum text
eth_string = tablecells[12].text.replace(',','')
eth_no_dollarsign = float(eth_string.replace('$', ''))
if eth_no_dollarsign < 3000:
    client = Client(keys.accountSID, keys.authToken)

    twilionumber = '+16693568831'
    myCellphone = '+18325809005'

    textmsg = client.messages.create(to=myCellphone,from_=twilionumber, body='Ethereum value is less than $3,000')

    print(f'Ethereum text status: {textmsg.status}')
