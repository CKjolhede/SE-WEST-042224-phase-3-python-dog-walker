#!/usr/bin/env python3

import ipdb
from lib.pet import *

cookie = Pet("Cookie", 5, "Dachshund", "fiesty", "./assets/cookie.jpg")
rose = Pet("Rose", 10, "domestic longhair", "sweet", "./assets/rose.jpg")

print(rose)
rose.print_pet_details()

rose.age = "nothin' but a number"
print(rose.age)

cookie.age = 6
print(cookie.age)

print(cookie == rose)

ipdb.set_trace()
