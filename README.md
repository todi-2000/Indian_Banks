# Indian_Banks
An API in which IFSC code is used to get bank details and city and bank name is used to get details of all the branches of that bank in city.


## Clone and run following commands on your local server.
```
env/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```
## Urls:
```
1. http://127.0.0.1:8000/api/{ifsccode}
For example: http://127.0.0.1:8000/api/BARB0KHATOD
```
```
2. http://127.0.0.1:8000/api/{city}/{bankname}
For example: http://127.0.0.1:8000/api/NOIDA/HDFC BANK
```

