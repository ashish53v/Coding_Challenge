# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()

for i in range(0, int(n)):
    credit_card_number = input();
    flag = False
    prev_char = 'z'
    min_length, max_length, prev_char_count = 20, 0, 0
    
    parts = credit_card_number.split('-')
    if len(parts) != 1 and len(parts) != 4:
        flag = True
        
    if not credit_card_number[0].isdigit():
        flag = True
    else:
        first_num = int(credit_card_number[0])
        if first_num < 4 or first_num > 6:
            flag = True
    
    for part in parts:
        if flag:
            break
        if not part.isdigit():
            flag = True
            break
        
        if len(part) < min_length:
            min_length = len(part)
        
        if len(part) > max_length:
            max_length = len(part)
    
        for c in part:
            if c != prev_char:
                prev_char = c
                prev_char_count = 1
            elif c == prev_char:
                prev_char_count = prev_char_count + 1
            
            if prev_char_count >= 4:
                flag = True
                break
        if min_length != max_length:
            flag = True
    
    if min_length == max_length and min_length != 4 and min_length != 16:
        flag = True
            
    
    if flag:
        print("Invalid ")
    else:
        print("Valid")
    