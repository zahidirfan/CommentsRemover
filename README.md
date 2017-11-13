# CommentsRemover

## How to setup
The project can be setup using the following procedure

- Clone the project 
- Create the virtual environment by using the following command
 ``` 
 $virtualenv ../remove-comments-venv
 $source ../remove-comments-venv/bin/activate
 $./manage.py migrate
 $./manage.py runserver
 ```
 - This would run the server
 
 Open another terminal 
 - cd to the client directory
 - Execute the following commands
 ```
  $npm install
  $npm run start
 ```
 
- The would run the client

Now open the http://localhost:3000 in the browser. 


