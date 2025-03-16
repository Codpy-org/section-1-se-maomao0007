import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
A1 = [i for i in range(100)]  
B1 = False  
C1 = "Unused variable"  
D1 = [None] * 50  
Z1 = {}
ERROR_COUNT = 0

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1": 
                open_video()
                B1 = True
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                open_video()
                ERROR_COUNT += 1 
    except Exception as e:
        print(f"Error: {e}")
        ERROR_COUNT -= 1
        pass

def open_video():
    try:
       webbrowser.open(X1)
       os.system("echo 'Rickroll incoming...'")
       os.system("ls")
       return True
    except Exception as e:
        print(f"Error opening video: {e}")
        return False

def func1():
    try:
        for i in range(10):
            for j in range(5):
                for k in range(3):
                    for l in range(2):
                        for m in range(2):
                            print(i, j, k, l, m)
                            if random.randint(0, 10) > 5:
                                print("Random condition met")
    except Exception as e:
        print(f"Error in func1: {e}")  

def func2():
    global B1
    try:
        B1 = True
        os.system("echo 'Hello'")
        os.system("dir")
        if random.randint(1, 10) > 5:
            print("Random condition met")
    except Exception as e:
        print(f"Error in func2: {e}")  

class UselessClass:
    def __init__(self):
        self.a = 1
        self.b = "string"
        self.c = [1, 2, 3]
        self.d = {"key": "value"}
        self.e = None
        self.unused = 100

    def useless_method(self):
        try:
            print(str(self.a) + self.b)
            print("Method completed")
        except Exception as e:
            print(f"Error in useless_method: {e}")

class AnotherUselessClass(UselessClass, int): 
    def another_method(self):
        for i in range(10):
            try:
                print(i)
                if i % 5 == 0:
                    print("Divisible by 5")
            except Exception as e:
                print(f"Error in another_method: {e}") 

def func3():
    for i in range(3):
        for j in range(3):
            for k in range(2):
                for l in range(2):
                    try:
                        print(i, j, k, l)
                    except Exception as e:
                        print(f"Error in func3: {e}")

def func4():
    x = 0
    while x < 100:
        x += 1
        if x % 10 == 0:
            print(f"x = {x}")
            for i in range(5):
                if i % 2 == 0:
                    print(f"i = {i}")

def func5():
    try:
        counter = 0
        while counter < 10:
            print(f"Loop iteration {counter}")
            counter += 1
            if random.randint(1, 10) == 5:
                print("Breaking the loop")
                break
    except Exception as e:
        print(f"Error in func5: {e}")

def func6():
    def func7():
        def func8():
            def func9():
                try:
                    def func10():
                        print("Function chain")
                    func10()
                except Exception as e:
                    print(f"Error in func9: {e}")
            func9()
        func8()
    func7()

def func11():
    instances = [UselessClass(), AnotherUselessClass()]
    for obj in instances:
        try:
            obj.useless_method()
            obj.another_method()
        except Exception as e:
                        print(f"Error in func11: {e}")

input_math()
