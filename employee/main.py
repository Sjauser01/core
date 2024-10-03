def increment_alphabet_recursive(char):
    if char.islower():  # Lowercase 'a-z'
        if char == 'z':
            return 'a', True
        else:
            return chr(ord(char) + 1), False
    elif char.isupper():  # Uppercase 'A-Z'
        if char == 'Z':
            return 'A', True
        else:
            return chr(ord(char) + 1), False
    return char, False

def increment_number_recursive(number_str):
    length = len(number_str)
    number = int(number_str)
    
    if number == 10 ** length - 1:  # If it's the max number like 9999
        return '0' * length, True   # Roll over to 0000
    else:
        return str(number + 1).zfill(length), False

def recursive_increment(s_list, index):
    # If index is out of bounds, return without cascading further
    if index < 0:
        return s_list
    
    char = s_list[index]
    
    # If it's a digit, handle numeric increment
    if char.isdigit():
        num_start = index
        while num_start >= 0 and s_list[num_start].isdigit():
            num_start -= 1
        
        num_start += 1
        numeric_part = ''.join(s_list[num_start:index + 1])
        new_number, carry = increment_number_recursive(numeric_part)
        s_list[num_start:index + 1] = list(new_number)
        
        if carry:
            return recursive_increment(s_list, num_start - 1)
    
    # If it's an alphabet, handle alphabet increment
    elif char.isalpha():
        new_char, carry = increment_alphabet_recursive(char)
        s_list[index] = new_char
        
        if carry:
            return recursive_increment(s_list, index - 1)  

    return s_list

def increment_string_recursive(s, times):
    # Convert the string into a list for in-place modification
    s_list = list(s)

    for _ in range(times):
        # Start from the last position and recursively increment
        s_list = recursive_increment(s_list, len(s_list) - 1)
        print(''.join(s_list))

# Test case
increment_string_recursive('c1212zz9999x', 10000000)
