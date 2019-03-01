#!/user/bin/python
a=int(raw_input("please input num1"))
b=int(raw_input("please input num1"))
operator=raw_input("please input operator")


if operator.__eq__("+"):
    print a+b
elif operator.__eq__("-"):
    print a-b
elif operator.__eq__("*"):
    print a*b
else:
    print a/b
