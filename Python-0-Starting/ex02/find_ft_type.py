def all_thing_is_obj(object: any = None) -> int:
    if object is None:
        print("Type not found")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    return 42
