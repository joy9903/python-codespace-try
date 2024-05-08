from typing import Any 


def do_it(a: Any = None, b:Any = None, c:Any = None):
    print(a,b,c)



do_it(["a","b","c"])

do_it(*["a","b","c"])

do_it(*["a","b"])