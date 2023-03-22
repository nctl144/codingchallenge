## coding challenge

### how to use

Run 
```
docker-compose up
```
And all of the endpoints defined in app/__init__.py should be ready to be used at http://127.0.0.1:5000/

### Endpoints

POST /users: add users to the DB (duplication with id is not yet handled)
GET /users/<id>: retrieve a user
POST /users/search: provide a body of filter and return list of users
GET /users/most_popular: return a list of most searched users
GET /users/least_popular: return a list of least searched users
