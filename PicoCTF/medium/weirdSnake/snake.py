input_list = (4, 54, 41, 0, 112, 32, 25, 49, 33,
        3, 0, 0, 57, 32, 108, 23, 48, 4, 9,\
        70, 7, 110, 36, 8, 108, 7, 49, 10, \
        4, 86, 43, 102, 126, 92, 0, 16, 58,\
        41, 89, 78)
#this generates optimized assembly but 
#assembly of the same purpose 

key_str = 'J'
key_str = '_' + key_str
key_str = key_str + 'o'
key_str = key_str + '3'
key_str = 't' + key_str 
#this generated BINARY_OP(+) instead of binary_add
#but that is because of the mismatch in python version

#this next part creates a list comprehension
#and if we check out the dissasembly of the 
#list comprehension its something like
key_list = [ord(char) for char in key_str]
#turns all of these into their ascii representations

#this part pads up our key_list
#its interesting how python handles
#control flow with POP_TOP and POP_JUMP_...
#its like reting instead of jumping in asm
#which makes sense since python doesnt even have goto's
while len(key_list) < len(input_list):
    key_list.extend(key_list)

#here comes the next list comprehension
#nice introduction for the zip function
result = [a ^ b for a,b in zip(input_list,key_list)]

#nice introduction for mapping to me
#very similar to how C++ handles fpointers
result_text = ''.join(map(chr,result))

#lets see the result
print(result_text)
