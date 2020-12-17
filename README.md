# Flask-Task

1 Copy repository.  
2 With the postman collection you need to create an enviroment on the options (the eye) click on add enviroment, and create the enviroment (ANY NAME).  
3 You need to create the variable {{Endpoint}} => http://127.0.0.1/, click on the eye then click add variable and create the name Endpoint, add the current value and initial value as http://127.0.0.1/.  
4 You can start testing.  
POSTMAN COLLECTION ==> https://www.getpostman.com/collections/7dd8be7273fb65c7cc52
    
The first function is <ins>token_required</ins> this function uses JWT to generate a token which experies and stops allowing the user to send requests in 120 minutes, you can always generate a new unique token.  
Then we start with the reoutes <ins>@app.route('/')</ins> in routes we can add a method such as **POST, GET, PUT, DELETE, PATCH, LOCK, UNLOCK, ETC.**, but we only use GET, POST, PUT, DELETE for this Flask API.

These are the libraries i've used on the project ***flask, flask_restful, flask_sqlalchemy, jwt, datetime and functools***.

The database schema is:

CREATE TABLE **Podcast**(
  artistName **varchar(500)**,
  releaseDate **varchar(500)**,
  id **varchar(500) primary key**,
  name **varchar(500)**,
  kind **varchar(500)**,
  copyright **varchar(500)**,
  artistId **varchar(500)**,
  artistUrl **varchar(500)**,
  url **varchar(500)**
);

CREATE TABLE PodcastGenre(
  genreId **varchar(500) primary key**,
  name **varchar(500)**,
  url **varchar(500)**
);

During the project i had to split the json file in different list because it's easier to manipulate date from splitted lists. Other way that i did a work around was creating a separate table as you can see in the schema GENRES AND PODCAST/results.

**PLEASE LET ME KNOW IF YOU FOUND A MISTAKE/BUG/IMPROVMENT THAT I CAN APPLY**

Happy coding.
