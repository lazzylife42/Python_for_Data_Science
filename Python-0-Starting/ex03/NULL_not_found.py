def NULL_not_found(obj: any) -> int:
    try:
        checks = [
            (lambda x: x is None, "Nothing"),
            (lambda x: isinstance(x, float) and x != x, "Cheese"),
            (lambda x: isinstance(x, int) and x == 0, "Zero"),
            (lambda x: isinstance(x, str) and len(x) == 0, "Empty"),
            (lambda x: isinstance(x, bool) and not x, "Fake"),
        ]
        for check, name in checks:
            if check(obj):
                print(f"{name}: {obj} <class '{type(obj).__name__}'>")
                return 0
            
        print("Type not Found")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
