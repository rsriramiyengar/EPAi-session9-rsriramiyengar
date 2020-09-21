import pytest
import random
import string
import pytest
from datetime import datetime

import session9
from  session9 import function_1a_odd_time
from  session9 import function_1b_logged
from  session9 import function_1c_authenticate_check_user
from  session9 import function_1d_timed
from  session9 import function_1e_user_privilege
from  session9 import htmlize
import os
import inspect
import re
import math
import random
import decimal
from decimal import Decimal
from random import randint




   
log=[]


README_CONTENT_CHECK_FOR = [
    'function_1a_odd_time',
    'function_1b_logged',
    'function_1c_authenticate_check_user',
    'function_1d_timed',
    'function_1e_user_privilege'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_1a_odd_time():
    """
    This function test for function checks if odd  time function works properly
    Limitation is if the time change just after execution of function it does not work properly
    """
    d=[]
    @function_1a_odd_time
    def add(a: "Number1", b: "Number1") -> "Sum of Numbers":
        """This Function Returns sum of Two given real numbers (Integer/Floats)"""
        return a + b

    for i in range(1000):
        a=randint(-100,100)
        b=randint(-100,100)
        c=add(a,b)    
        if int(datetime.now().strftime("%S"))%2 !=0:
            d.append(c==a+b)
        else:
            d.append(c=="Time not odd seconds and function cannot run")   
    assert set(d)=={True}, "Check function_1a_odd_time_function"


def test_function_1b_logged():
    """
    This function test for function checks if logged function works properly
    """
    d=[]
    def mul(a: "Number1", b: "Number1") -> "Multiplication of Numbers":
        """This Function Returns Multiplication of Two given real numbers(Integer/Floats)"""
        return a * b

    mul = function_1b_logged(mul, log)
    for i in range(100):
        a = randint(-100, 100)
        b = randint(-100, 100)
        c = mul(a, b)
        d.append(c == a * b)
    assert set(d)=={True} and len(log)!=0, "function_1b_logged"


def test_function_1c_authenticate_check_user1():
    """
    This function test for function checks if function_1c_authenticate_check works properly
    """
    def div(a:"Number1", b:"Number1")->"Division of Numbers":
        """This Function Returns division of Two given real numbers (Integer/Floats)"""
        return a / b if b != 0 else a
    div=function_1c_authenticate_check_user(div,"user1","asdfg")
    d = []
    for i in range(100):
        a = randint(-100, 100)
        b = randint(-100, 100)
        c = div(a, b)
        if b !=0:
            d.append(c == a/b)
        else:
            d.append(c==a)
    assert set(d)=={True}, "function_1c_authenticate_check_user"


def test_function_1c_authenticate_check_user2():
    """
    This function test for function checks if function_1c_authenticate_check works properly
    """
    def div(a:"Number1", b:"Number1")->"Division of Numbers":
        """This Function Returns division of Two given real numbers (Integer/Floats)"""
        return a / b if b != 0 else a
    div=function_1c_authenticate_check_user(div,"user1","1234")
    d = []
    for i in range(100):
        a = randint(-100, 100)
        b = randint(-100, 100)
        c = div(a, b)
        d.append(c =="you are a scamster")
    assert set(d)=={True}, "function_1c_authenticate_check_user_case2"


def test_function_1d_timed():
    """
    This function test for function checks if timed function works properly
    """
    def div(a:"Number1", b:"Number1")->"Division of Numbers":
        """This Function Returns division of Two given real numbers (Integer/Floats)"""
        return a / b if b != 0 else a
    div=function_1d_timed(div,10)
    d = []
    for i in range(100):
        a = randint(-100, 100)
        b = randint(-100, 100)
        c = div(a, b)
        if b !=0:
            d.append(c == a/b)
        else:
            d.append(c==a)
    assert set(d)=={True}, "function_1d_timed is not working properly"


customer_database={"customer1":{"username" :"customer1", "email": "abc@customer1.com","Phone":"+123458", "City": "Delhi"},
                   "customer2":{"username" :"customer2", "email": "abc@customer2.com","Phone":"+567891", "City": "Mumbai"},
                    "customer3":{"username" :"customer3", "email": "abc@customer3.com","Phone":"+10000", "City": "Mumbai"},
                    "customer4":{"username" :"customer4", "email": "abc@customer4.com","Phone":"+90000", "City": "Bangalore"}
                   }

user_data={"user1":{"password" :"asdfg", "PL" :4},"user2":{"password" :"hjk;","PL":3},"user3":{"password" :"zxcvb","PL":2},    "user4":{"password" :"nm,./","PL":1}}

def test_function_1e_user_privilege():
    """
    This function test for User privilege function for different privelge levels
    """
    def user_data_extraction(company_Name):
        user_name=customer_database[company_Name]["username"]
        Email=customer_database[company_Name]["email"]
        Phone=customer_database[company_Name]["Phone"]
        customer_address = customer_database[company_Name]["City"]
        return user_name,Email,Phone,customer_address
    user1=function_1e_user_privilege(user_data_extraction,"user1")
    user2 = function_1e_user_privilege(user_data_extraction,"user2")
    user3 = function_1e_user_privilege(user_data_extraction, "user3")
    user4 = function_1e_user_privilege(user_data_extraction, "user4")
    data1=user1("customer1")
    data2 = user2("customer2")
    data3 = user3("customer3")
    data4 = user4("customer4")
    print(data1)
    assert data1==("customer1","abc@customer1.com","+123458","Delhi")
    assert data2 == ("customer2", "abc@customer2.com", "+567891","No Access")
    assert data3 == ("customer3", "abc@customer3.com","No Access","No Access")
    assert data4 == ("customer4","No Access","No Access","No Access")


def test_htmlize():
    """
    This Function Test the htmplize function for different cases
    """
    a=htmlize(10)
    b = htmlize(10.0)
    c = htmlize([10,20,30])
    d = htmlize((30,40,50))
    e = htmlize({"user1":{"password" :"asdfg", "PL" :4},"user2":{"password" :"hjk;","PL":3},"user3":{"password" :"zxcvb","PL":2},    "user4":{"password" :"nm,./","PL":1}})
    f = htmlize("Very Big Line")
    g = htmlize(Decimal(4.502))
    assert a=='10' , "htmplize function is not working for Integer"
    assert b == "10.0" , "htmplize function is not working for float"
    assert c == "<ul>\n<li>10</li>\n<li>20</li>\n<li>30</li>\n</ul>" , "htmplize function is not working for List"
    assert d == "<ul>\n<li>30</li>\n<li>40</li>\n<li>50</li>\n</ul>", "htmplize function is not working for Tuple"
    assert e == "<ul>\n<li>user1={'password': 'asdfg', 'PL': 4}</li>\n<li>user2={'password': 'hjk;', 'PL': 3}</li>\n<li>user3={'password': 'zxcvb', 'PL': 2}</li>\n<li>user4={'password': 'nm,./', 'PL': 1}</li>\n</ul>" , "htmplize function is not working for Dictionary"
    assert f== "Very Big Line" , "htmplize function is not working for Str"
    assert g == "4.50", "htmplize function is not working for Decimal"
