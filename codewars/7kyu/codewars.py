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

# def number(bus_stops):
#     total = 0
#     for stops in bus_stops:
#         get_in=stops[0]
#         get_out=stops[1]
#         total += get_in
#         total -= get_out
#     return total

# ## TEST CASES
# print(number([[10,0],[3,5],[5,8]]))
# print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
# print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))

# def reverse_words(text):
#     split_t = text.split(" ")
#     result = ""
#     for word in range(len(split_t)):
#         result += split_t[word][::-1]
#         if word < len(split_t) - 1:
#             result += " "
#     return result

# ## TEST CASES 
# print(reverse_words('The quick brown fox jumps over the lazy dog.'))
# print(reverse_words('apple'))
# print(reverse_words('a b c d'))
# print(reverse_words('  double  spaced  words  '))

# def remove_smallest(numbers):
#     if len(numbers) == 0:
#         return []
#     min_val = numbers[0]
#     smallest_i = 0
#     for i in range(len(numbers)):
#         if numbers[i] < min_val:
#             min_val = numbers[i]
#             smallest_i = i
    
#     newList = []
#     for i in range(len(numbers)):
#         if i != smallest_i:
#             newList.append(numbers[i])
            
#     return newList

# ## TEST CASES
# print(remove_smallest([1, 2, 3, 4, 5]))
# print(remove_smallest([5, 3, 2, 1, 4]))
# print(remove_smallest([1, 2, 3, 1, 1]))
# print(remove_smallest([]))
