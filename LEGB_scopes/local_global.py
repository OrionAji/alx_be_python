x = 'global x'
def new_function():
    x = 'local x'
    print(x)
new_function()
print(x)