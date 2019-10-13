class ClassA:
    cp1 = "hello"
    cp2 = "heel0"

def add_dynamic_method(info):
    fn_name = "resolve_" + info

    def fn(self):
        print("invoke info")
    setattr(ClassA, fn_name, fn)

a = ClassA()
for attr in dir(a):
    print(attr)
    if attr.startswith("cp"):
        add_dynamic_method(attr)

print(dir(a))

