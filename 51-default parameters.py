def user_info(first_name,last_name,age=24): #age=23 default parameter 
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
print(user_info('vaishali','jain',24)) #if we dont pass the value of age the default value will automatically print
