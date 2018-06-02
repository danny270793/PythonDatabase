# Database
A database library for python, this library is a wrapper for other commons libraries
## Installation
To install the libary first install git
```bash
sudo apt-get install git
```
Clone the repository
```bash
git clone https://github.com/danny270793/PythonDatabase.git
```
Enter to the folder and install it on python 2
```bash
cd Database
pip install .
```
Or with python 3
```bash
cd Database
pip3 install .
```
## Usage
The library open the database "database.sqlite3" if do not exists create a new
```python
from database import SqliteDatabase
database=SqliteDatabase('database.sqlite3')
```
We can use the shortcuts functions "drop", "create", etc. to get easy access to the database functions
```python
from database import SqliteDatabase

database=SqliteDatabase('database.sqlite3')
database.drop('measurements')
database.create('measurements',{'name':'text','value':'float'})
database.insert('measurements',{'name':'Temperature','value':'35.6'})
database.insert('measurements',{'name':'Humidity','value':'4'})
database.insert('measurements',{'name':'Temperature','value':'34.6'})
database.insert('measurements',{'name':'Humidity','value':'3.8'})
measurements=database.select('measurements',('name','value'),(('name','Temperature'),('and','value','>','35')))
print(measurements)
```
Or can run the full query
```python
from database import SqliteDatabase

database=SqliteDatabase('database.sqlite3')
database.query('drop table if exists users')
database.query('create table users (name text,lastname text)')
database.query('insert into users (name,lastname) values ("Danny","Vaca")')
database.query('insert into users (name,lastname) values ("Pedro","Picapiedra")')
database.query('insert into users (name,lastname) values ("Pablo","Marmol")')
users=database.query('select * from users')
print(users)
```
## Follow me
* [Facebook](https://www.facebook.com/danny.vaca.9655)
* [Instagram](https://www.instagram.com/danny27071993/)
* [Youtube](https://www.youtube.com/channel/UC5MAQWU2s2VESTXaUo-ysgg)
* [Github](https://www.github.com/danny270793/)
* [LinkedIn](https://www.linkedin.com/in/danny270793)

## License
Copyright (c) Danny Vaca. All rights reserved.

Licensed under the [MIT](LICENSE.txt) License.