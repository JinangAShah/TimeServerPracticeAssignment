
import requests

server = 'http://127.0.0.1:5000'

age_datetime = {'date': "12/25/1995", 'units': "years"}

r = requests.get(server + '/time')
print(r.text)

r = requests.get(server + '/date')
print(r.text)

r = requests.post(server + '/age', json=age_datetime)
print(r.text)

r = requests.get(server + '/until_next_meal/breakfast')
print(r.text)

r = requests.get(server + '/until_next_meal/lunch')
print(r.text)

r = requests.get(server + '/until_next_meal/dinner')
print(r.text)
