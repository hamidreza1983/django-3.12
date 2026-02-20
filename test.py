def test(*args, **keywargs):
    if keywargs.get("name") and keywargs.get("age") :
        print("Hello " + keywargs["name"] + " Your age is " + str(keywargs["age"]))
    
    elif keywargs.get("name") :
        print("Hello " + keywargs["name"])

    elif keywargs.get("age") :
        print("Your age is " + str(keywargs["age"]))
    
    else:
        print ("nothins")


test(age=25)

