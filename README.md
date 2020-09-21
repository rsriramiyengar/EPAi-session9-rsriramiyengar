# Readme File for Assignment for Session 9- Decorators
### Created by Sriram Iyengar
## Session 9 - Decorators and Decorator Applications
- Decorators
- Parameterized Decorators
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Assignment 
### Write separate decorators that:
- allows a function to run only on odd seconds - 100pts
- log - 100pts
- authenticate - 300pts
- timed (n times) - 100pts
- Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params) - 200pts
### Write our htmlize code using inbuild singledispatch - 100pts
No readme or no docstring for each function, or no test cases → 0.
Write test cases to check boundary conditions that might cause your code to fail. 


## Function creared based on Assignment
### function_1a_odd_time (fn:"input function"):
    """
    This Function add a decorator to function and only runs when local time is odd seconds
    """    

### function_1b_logged (fn:"input function",log:" Input Log variable"):
    """
    This Function add a decorator to function that logges information in given variable for number of times with details of each run
    """
### function_1c_authenticate_check_user (fn:"Function Name",user:"Name of User",password:"User Password")-> "funcion output based on authecation":
    """
    This Decorator adds authenticats user and then function is run
    Limitation The dictionary is static at print as it part of session9 
    """
### function_1d_timed (fn:"Function Name",reps:"number of repitation")-> "funcion output with number of times":
    """
    This Decorator runs function for n times and prints the avg time on screen
    """
### function_1e_user_privilege (fn:"Function Name",user_name:"User Name to check Privilege Level"):
    """ This decorator return output of function with 4 output based on Priveledge level 4 being max and 1 being least
	    Limitation The dictionary is static at print as it part of session9 
    """

### htmlize function is created using single dispacth for following 
- strings
- floats
- integers
- dictionary
- Integrals
- Lists
- tuple

## Functions used in Test File
### test_readme_exists 
- checks if Readme files exists

### test_readme_contents length 
- checks the content length of  Readme file
### test_readme_proper_description 
- checks the content length of  Readme file

### test_readme_file_for_formatting 
- checks the formatting of  Readme file

### test_indentations 
- checks if the Assignment code is properly formated

### test_function_name_had_cap_letter 
- checks if the Assignment code is function has capital letters

### test_function_1a_odd_time ():
- This function test for function checks if odd  time function works properly
  Limitation is if the time change just after execution of function it does not work properly

### test_function_1b_logged ():
- This function test for function checks if logged function works properly

### test_function_1c_authenticate_check_user1 ():
- This function test for function checks if function_1c_authenticate_check works properly

### test_function_1c_authenticate_check_user2 ():
- This function test for function checks if function_1c_authenticate_check works properly
 
### test_function_1d_timed ():
- This function test for function checks if timed function works properly

### test_function_1e_user_privilege ():
- This function test for User privilege function for different privelge levels

### test_htmlize ():
- This Function Test the htmplize function for different cases

***
> ![My Image](https://github.com/rsriramiyengar/EPAi-session9-rsriramiyengar/blob/master/images/Image01.JPG)
***

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder

