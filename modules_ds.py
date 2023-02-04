# Core modules

# import
import datetime

today_ds = datetime.date.today()

print(today_ds)

# from
import datetime
from datetime import date

today_ds = date.today()

print(today_ds)

#
import datetime
from datetime import date
import time

today = date.today()
timestamp_ds = time.time()

print(timestamp_ds)

#
import datetime
from datetime import date
import time
from time import time

today = date.today()
timestamp_ds = time()

print(timestamp_ds)

# Pip module

# pip (pip3 install camelcase)(global)

from camelcase import CamelCase

c_ds = CamelCase()
print(c_ds.hump('hello there world'))

# Import custom modul
import validator
from validator import validate_email

email_ds = 'test@test.com'
if validate_email(email_ds):
  print('Email is valid')
else:
  print('Email is bad')
  
