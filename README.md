##  TITLE
 AWWARDS

## AUTHOR
 Built By Faith Gakori

## PROJECT DESCRIPTION
 The application is used to display projects build by users and can be viewed by other users. Users can also be able to post their projects.The users can also rate according to design, usability and content.
    

## SCREENSHOTS
![Screenshot](images/s1.png)
![Screenshot](images/s2.png)
![Screenshot](images/s3.png)

## USER STORIES

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page


## SetUp / Installation Requirements
  Clone the repo by running:
*   git clone https://github.com/Gakori/awwards.git

 Navigate to the project directory;
*   cd Awwards

 Create a virtual environment and activate it
*   python3 -m venv virtual
*   source virtual/bin/activate

  Create a database
  using postgress, type the following commands;
*   $psql

Then run the command to create a new database
*   #create database gram

 Install dependencies
*   pip install -r requirements.txt

 Create database migrations
*   python3 manage.py makemigrations gram
*   python3 manage.py migrate

 Run the app
*   python3 manage.py runserver

## TECHNOLOGIES USED
* Django
* Python
* Bootstrap
* Html
* Css
* Postgres

## KNOWN BUGS
  Ratings not working at the moment but it is under development

## CONTACT INFORMATION
 For email reach us through faithgakori506@gmail.com

## LICENCE
MIT License

Copyright (c) 2020 Faith Gakori

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.