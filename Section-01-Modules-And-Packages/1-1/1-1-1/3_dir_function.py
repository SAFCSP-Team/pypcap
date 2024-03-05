# Q1: What does the `dir()` function do without any arguments?


def greet():
    name = "Alice"
    age = 30
    print("Hello, " + name + "!")

dir_list = dir()

print(dir_list)





























# Output:
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'dir_list', 'greet']
# 
#  captures the names in the current local scope, which include the built-in names (`__builtins__`), the script's special attributes (`__doc__`, `__loader__`, `__name__`, `__package__`, `__spec__`), 
# as well as the names defined within the script (`dir_list`, `greet`).























