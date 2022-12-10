# ������ YaMDb
?
������ YaMDb �������� ������ (Review) ������������� �� ������������ (Titles). ������������ ������� �� ���������: ������, ��������, �������. ������ ��������� (Category) ����� ���� �������� ��������������� (��������, ����� �������� ��������� ���������������� ��������� ��� ���������).
?
## ���� ����������: 
* Python3
* Django REST Framework
* SQLite3
* Git
---
## ��� ��������� ������: 
?
**����������� ����������� � ������� � ���� � ��������� ������:**
```
cd api_yamdb 
```
**C������ ����������� ���������:**
```
python -m venv venv (Windows)
```
?
**������������ ����������� ���������:**
```
source venv/Scripts/activate (Windows)
```
?
?
**���������� ����������� �� ����� requirements.txt:**
?
```
python -m pip install --upgrade pip 
```
```
pip install -r requirements.txt 
```
**��������� ��������:**
```
python manage.py migrate 
```
**��������� ������:**
```
python manage.py runserver
```
## API ��� ������� YaMDb
?
������ ������� �������, �� ������ http://127.0.0.1:8000/redoc/ ����� �������� ������������ ��� API YaMDb. ��� ���� � ������� �������� � API.
?
## �� ��� ������� YaMDb
### Windows
?
**������� ��������� sqlite3**
?
https://www.sqlite.org/
?
**������� <file_sh>**
```
#!/bin/bash
```
```
echo -e ".separator \",\"\n.mode csv\n.import  --skip 1 <file_csv> <db_table_name>" | ./sqlite3.exe db.sqlite3
```
**��������� <file_sh>**
```
chmod a+x ./<file_sh> (��� ������� ������ �������)
```
```
./<file_sh> (����������� ������� �������� ������)
```
### Linux
?
**���������� ��������� sqlite3**
```
pip install pysqlite3
```
**C������ <file_sh>**
```
#!/bin/bash
```
```
echo -e ".separator \",\"\n.mode csv\n.import  --skip 1 <file_csv> <db_table_name>" | ./sqlite3 db.sqlite3
```
**��������� <file_sh>**
```
chmod a+x ./<file_sh> (��� ������� ������ �������)
```
```
./<file_sh> (����������� ������� �������� ������)
```
```
```
### ������:
```
[����� �������](https://github.com/Komanok-dev/)
[���� ��������](https://github.com/Ilya-Kirillov/)
[���� ������](https://github.com/Komanok-dev/)
