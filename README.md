# csv-import-poc
import csv and save data in database


1. go to settings.py file 

        'NAME': 'bulk_upload',          "your data base name"
        'USER': 'postgres',             "your Local database user name"
        'PASSWORD': 'postgres_123',     "your Database Password"
        'HOST': 'localhost',            "your HOST"        
        'PORT': '5432',                 "your PORT"

   change in to this fields 

2. First Of all doing regular setup for python project 
    like migrations and migrate 

3. you need to create superuser first  