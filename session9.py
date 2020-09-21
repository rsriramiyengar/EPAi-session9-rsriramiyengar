from datetime import datetime, timezone, timedelta
from time import perf_counter
from random import randint
from functools import wraps

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from html import escape


user_data={"user1":{"password" :"asdfg", "PL" :4},"user2":{"password" :"hjk;","PL":3},"user3":{"password" :"zxcvb","PL":2},    "user4":{"password" :"nm,./","PL":1}}


def function_1a_odd_time(fn:"input function"):
    """
    This Function add a decorator to function and only runs when local time is odd seconds
    """    
    ntime=0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal ntime
        ntime=datetime.now()
        #print(ntime)
        return fn(*args, **kwargs) if  int(ntime.strftime("%S")) %2 !=0 else "As Time is not odd seconds and function cannot run"
    return inner

def function_1b_logged(fn:"input function",log:" Input Log variable"):
    """
    This Function add a decorator to function that logges information in given variable for number of times with details of each run
    """
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        start = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        end = datetime.now(timezone.utc)
        delta_time=end-start
        count += 1
        print(f'{fn.__name__} -start time {start}: end time{end} Run Time {delta_time}  has run {count} times')
        log.append(fn.__name__+" count-"+str(count)+ "start time" +str(start) + "end time"+ str(end) +"Run Time" + str(delta_time))
        return result
    return inner

def function_1c_authenticate_check_user(fn:"Function Name",user:"Name of User",password:"User Password")-> "funcion output based on authecation":
    """
    This Decorator adds authenticats user and then function is run
    """
    result=[]
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal result
        if user_data[user]["password"]==password:
            result=fn(*args, **kwargs)
        else:
            result="you are a scamster"
            print("you are a scamster")
        return result
    return inner


def function_1d_timed(fn:"Function Name",reps:"number of repitation")-> "funcion output with number of times":
    """
    This Decorator runs function for n times and prints the avg time on screen
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)
        avg_run_time = total_elapsed / reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
        return result
    return inner


def function_1e_user_privilege(fn:"Function Name",user_name:"User Name to check Privilege Level"):
    """
    This decorator return output of function with 4 output based on Priveledge level 4 being max and 1 being least
	Limitation The dictionary is static at print as it part of session9
    """
    result=[]
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal result
        PL =user_data[user_name]["PL"]
        output1,output2,output3,output4=fn(*args, **kwargs)
        output1= output1
        output2 = output2 if PL>=2 else "No Access"
        output3 = output3 if PL >= 3 else "No Access"
        output4 = output4 if PL == 4 else "No Access"
        result=output1,output2,output3,output4
        return result
    return inner

### This is the html function
@singledispatch
def htmlize(a):
    return escape(str(a))

### This is the html for integer
@htmlize.register(int)
def html_real(a):
    return f'{a}'

### This is the html for float
@htmlize.register(float)
def html_real(a):
    return f'{round(a, 2)}'


from decimal import Decimal
### This is the html for decimal
@htmlize.register(Decimal)
def html_real(a):
    return f'{round(a, 2)}'

### This is the html for strings
def html_escape(arg):
    return escape(str(arg))

@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

### This is the html for tuples and Lists
@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = (f'<li>{html_escape(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
 
### This is the html for tuples and dict

@htmlize.register(dict)
def html_dict(d):
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

### This is the html for Integrals
@htmlize.register(Integral)
def htmlize_integral_numbers(a):
    return f'{a}(<i>{str(hex(a))}</i>)'