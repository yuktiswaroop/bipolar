* Please make requests using either Postman or the terminal.

Get access token by hitting the following url:
http://127.0.0.1:8000/api/token/
(token expires after 5 minutes)

Steps :-
$ python3
>>> import requests
>>> res = requests.get('http://127.0.0.1:8000/userbookdetail',headers={"Authorization":"Bearer <access token>"})
>>> print(res.json())

[{'id': 1, 'title': 'ABCDEF', 'amazon_url': 'https://www.amazon.in/', 'author': 'yukti', 'genre': 'Romcom'},
 {'id': 2, 'title': 'Django Backend Developer', 'amazon_url': 'https://www.amazon.in/', 'author': 'Jeff Kinney', 'genre': 'comedy'}]

>>> res = requests.delete('http://127.0.0.1:8000/userbookdelete/1',headers={"Authorization":"Bearer <access token>"})
>>> print(res.json())
{'message': 'ok'}

>>> res = requests.get('http://127.0.0.1:8000/userbookdetail',headers={"Authorization":"Bearer <access token>"})
>>> print(res.json())

[{'id': 2, 'title': 'Django Backend Developer', 'amazon_url': 'https://www.amazon.in/', 'author': 'Jeff Kinney', 'genre': 'comedy'}]
