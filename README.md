It is an API for the project [Abled Taha's Website](https://github.com/Abled-Taha/abled-taha-website).
It stores the data in a MongoDB which needs to be setup in a specific way.

1) After creating the user ADMIN, database "contact-me" must be created with collection "people" inside it.

2) A user "contact-me-api-python" must be created with password "MongoContact-me-api-python" and "readWrite" access to "contact-me" database.

As of now all of the details are hard coded which will be stored in environmental variables later in the development so as for now the exact credentials must be matched when creating user and database.