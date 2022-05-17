class Cookie:
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
        
cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print("cookie One is", cookie_one.get_color())
print("cookie Two is", cookie_two.get_color())

cookie_one.set_color("red")

print("\ncookie One is Now", cookie_one.get_color())
print("cookie Two is still", cookie_two.get_color())