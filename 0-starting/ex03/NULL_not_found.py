def NULL_not_found(object: any) -> int:
    #if bool(object):
    #    print("Type not Found")
    if object == None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool) and object == False:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == '':
        print(f"Empty: {object}{type(object)}")
    else:
        print("Type not Found")
    return 1
