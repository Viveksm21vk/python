def validate(age):
    if(age >= 18):
        print("Eligible for voting...")
    else:
        raise ValueError("Age must be greater or equal to 18.")
age = int(input("Enter age - "))
validate(age)