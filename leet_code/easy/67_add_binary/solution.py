def addBinary(a: str, b: str) -> str:
    add: dict[tuple[str, str], tuple[str, str]] = {
        ("1", "1"): ("1", "0"),
        ("1", "0"): ("0", "1"),
        ("0", "1"): ("0", "1"),
        ("0", "0"): ("0", "0"),
    }

    while len(a) != len(b):
        if len(a) < len(b):
            a = "0" + a
        else:
            b = "0" + b

    r: str = ""
    cout: str = "0"
    for b1, b2 in zip(a[::-1], b[::-1]):
        cin: str = cout

        c1, b3 = add[(b1, b2)]
        c2, b4 = add[(cin, b3)]

        cout = "1" if c1 == "1" or c2 == "1" else "0"
        r = b4 + r

    if cout == "1":
        r = "1" + r

    return r


print(addBinary("11", "1"))
