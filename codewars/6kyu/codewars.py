# def triple_double(num1, num2):
#     s1, s2 = str(num1), str(num2)
    
#     for digit in "0123456789":
#         if (digit*3) in s1 and (digit*2) in s2:
#             return 1
        
#     return 0

# ## TEST CASES
# print(triple_double(123123123, 123123))
# print(triple_double(111, 88))
# print(triple_double(111000, 100))
# print(triple_double(111888, 1188))
# print(triple_double(451999277, 41177722899))
# print(triple_double(1222345, 12345))
# print(triple_double(12345, 12345))
# print(triple_double(666789, 12345667))
# print(triple_double(10560002, 100))
# print(triple_double(1112, 122))

# def high(x):
    # best = ""
    # best_score = 0
    # splitted = x.split()
    # for word in splitted:
    #     score = sum(ord(c) - 96 for c in word)
    #     if score > best_score:
    #         best = word
    #         best_score = score
            
    # return best

