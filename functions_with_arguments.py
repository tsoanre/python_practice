# def func(name, rollno):
#     print("Your name is ", name +" and roll number is " +rollno)

# func('Tanuj Sonare','0832CS181168')

def greeting(*names):
    for name in names:
        print("Good Morning ",name )

greeting('Tanuj','Shubham','Vidhan','Ankur','Chetan')