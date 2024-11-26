def all_thing_is_obj(obj: any = None) -> None:
    if obj is not None:
        obj_type = type(obj).__name__.capitalize()
        if isinstance(obj, str):
            print(f"{obj} is in the kitchen : <class '{obj_type.lower()}'>")
        else:
            print(f"{obj_type} \t: {type(obj)}")
    else:
        print("Type not found")
