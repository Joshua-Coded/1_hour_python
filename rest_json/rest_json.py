import requests
import urllib.request
import json
# payload = {'username': "alana", 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
url = ("https://www.reddit.com/r/learnprogramming/")
# r_dict = r.json()   

response = urllib.request.urlopen(url)

data = response.read().decode("utf-8")

my_file = open("data.json", "w")
my_file.write(data)

new_data = json.load(data)
get_articles = new_data["articles"]
new_data_articles = json.dumps(get_articles)
f = open("data.json", "r")
new_data = json.loads(f.read())
print(new_data)