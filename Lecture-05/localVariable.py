def my_function():
    local_variable = "I'm inside the function"
    print(local_variable)

# Call function
my_function()
# Accessing local_variable outside, causing an error
print(local_variable)  # NameError: name 'local_variable' is not defined
