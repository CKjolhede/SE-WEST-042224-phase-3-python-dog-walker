#!/usr/bin/env python3
# 📚 Review With Students:
# Introduction to Object Oriented programming, classes, instances, methods

from lib.cat import *
from lib.handler import *
from lib.job import *
from lib.owner import *

# Importing the pet class
from lib.pet import *

# Instances of the pet classes
rose = Cat("rose", 11, "domestic longhair", "sweet", "rose.jpg", True)
cookie = Pet("cookie", 1, "Dachshund", "hyper", "cookie.jpg")
princess_grace = Cat(
    "princess grace", 7, "domestic longhair", "affectionate", "gracy.png", False
)

jess = Owner("jess", "jess@mail.com")
chris = Owner("chris", "chris@mail.com")
jess.add_pet(cookie)
jess.add_pet(rose)
chris.add_pet(princess_grace)

aixe = Handler("Aixe", "aixe@mail.com", 22)
hodor = Handler("Hodor", "hodor@mail.com", 19.99)

rose.book_handler(aixe, "7-31-24", 2)
rose.book_handler(hodor, "6-22-24", 3)
cookie.book_handler(aixe, "6-20-24", 1.5)


import ipdb

ipdb.set_trace()
