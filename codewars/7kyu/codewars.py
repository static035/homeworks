# def add_binary(a,b):
#     return bin(a+b)[2:]

# ## TEST CASES
# print(add_binary(0,1))
# print(add_binary(1,0))
# print(add_binary(2,2))
# print(add_binary(51,12))

# def validate_pin(pin):
#     if not pin.isdigit():
#         return False
    
#     if len(pin) == 4 or len(pin) == 6:
#         return True
    
#     return False

# ## TEST CASES
# print(validate_pin("1"))
# print(validate_pin("12"))
# print(validate_pin("123"))
# print(validate_pin("12345"))
# print(validate_pin("1234567"))
# print(validate_pin("-123434'"))
# print(validate_pin("-12345345"))
# print(validate_pin("1.234"))
# print(validate_pin("00000000"))

# def binary_array_to_number(arr):
#     stringifiedArr = []
#     for i in arr:
#         stringifiedArr.append(str(i))

#     stringed = "".join(stringifiedArr)
#     return int(stringed, 2)

# ## TEST CASES
# print(binary_array_to_number([0,0,0,1]))
# print(binary_array_to_number([0,0,1,0]))
# print(binary_array_to_number([1,1,1,1]))
# print(binary_array_to_number([0,1,1,0]))