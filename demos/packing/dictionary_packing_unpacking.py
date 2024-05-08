person = { "first_name": "John", "last_name": "Doe" }
person2 = {"age":42, **person}


print(person2)



def do_it(a:str, b:str, c:str) -> None:
    print(a,b,c)

do_it(**{'a': 1, 'b': 2, 'c': 3})


def do_it_2(**rest) -> None:
    print(rest)


do_it_2(a=2,b=4)