# Lab section 3
def mysplit(strng):
    if strng == '':
        return []
    else:
        begin = 0
        end = 0
        my_list = []
        for i in range(len(strng)):
            if strng[i] in ' \n\t':
                end = i
                if begin != end: # Contiguous whitespaces
                    my_list.append(strng[begin:end])
                begin = i + 1 # Preparing for the next word
        if begin != len(strng): # If the string does not end with a space
            my_list.append(strng[begin:])
        return my_list
            

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
