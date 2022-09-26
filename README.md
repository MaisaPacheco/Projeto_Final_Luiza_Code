# shopping-cart
MongoDB database integration for LuizaCode's shopping-cart project

## libs
* motor = Driver Python async for MongoDB
* pydantic = Data validation for Python 

## Install
* Create venv
    ```
    At the terminal in the project's folder 
    $ python -m venv venv
    ```
    Linux
    ```
    $ source venv/bin/activate
   ```
   Windows
    ```
    $ .\venv\Scripts\activate
   ```
   After the the inserted command, it should appear the virtual environment name
* Install requirements
     ```
     $ pip install -r requirements.txt
     ```
* Connect mongodb
  
     ```´

     $ create a .env file with your mongoDB connect string according to .env.example file 
     ```
     
  
     | name_env | value |
     |------------|------------|
     |DATABASE_URI|connection string Atlas|
          

* Run
  ```
  $ uvicorn main:app 
   ```

* How to test
  ```
  Open the cases test files and test the routes
  Tip: you can install the "Rest Client" extension in the Visual Studio Code to run tests in the *.http files directly
     ```
  
