**Please make requests using either Postman or the terminal.** 
**Get access token by hitting the following url:**
**http://127.0.0.1:8000/api/token/**
**(token expires after 5 minutes)**


Steps :-
$ python3
>import requests


**CREATE**

>res=requests.post('http://127.0.0.1:8000/userbookcreate/',headers={"Authorization":"Bearer <access token>"}, data = {"title": "ABCDEFGH", "amazon_url": "https://www.amazon.in/", "author": "yukti", "genre": "horror"})
>print(res.json())

**RETRIEVE**

>res=requests.get('http://127.0.0.1:8000/userbookdetail/',headers={"Authorization":"Bearer <access token>"})
>print(res.json())

**UPDATE**

/*The given book id must exist for updation.*/
>res=requests.put('http://127.0.0.1:8000/userbookupdate/14/',headers={"Authorization":"Bearer <access token>"}, data = {"title": "AB", "amazon_url": "https://www.amazon.in/", "author": "yuktiswaroop", "genre": "horror comedy"})
>print(res.json())

**DELETE**

/*The given book id must exist for deletion.*/
>res=requests.delete('http://127.0.0.1:8000/userbookdelete/10'/,headers={"Authorization":"Bearer <access token>"})
>print(res.json())
