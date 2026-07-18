input_str = 'I have a function named `function_a_b_c` and another function named `Function_A_B_C`.'

char_idx_arr = []
for i, j in enumerate(input_str):
    if j == '`':
        char_idx_arr.append(i)

print(char_idx_arr)

func_str_arr = []
for i in range(len(char_idx_arr)):
    if i % 2 == 0:
        func_str_arr.append(input_str[char_idx_arr[i] + 1:char_idx_arr[i + 1]])

print(func_str_arr)
