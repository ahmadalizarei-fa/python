import requests

res = requests.get('http://www.york.ac.uk/teaching/cws/wws/webpage1.html')
if res.status_code == 200: 

  print(res.content)
