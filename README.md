# Django-Rest-Boilerplate
## Run the following commands to run the project
```
git clone git@github.com:Younext19/Django-Rest-Boilerplate.git
docker-compose build
docker-compose up
```
Create .env file for Database Data For me i used Postgres DB
For example:
```
export SECRET_KEY = Secret Key value
export CLIENT_ID = Client Id value
export CLIENT_SECRET = Client Secret Value
export CODE = Code Value
// Your database name
NAME=postgres
USER=postgres
PASSWORD=postgres
HOST=db
PORT=5432
```

## Functionnalities 
```
0Auth2 
https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html

Web Socket Channels Integrated
https://djangochannelsrestframework.readthedocs.io/en/latest/
```
Simple CRUD For Articles
Modal : 
```
{
  created:DateTimeField()
  medicament:CharField()
  imgLinkAddress:URLField()
  description: TextField()
  quantite: IntegerField()
}
```

URLS & Requests : 




Simple CRUD For Complex Products Modals


