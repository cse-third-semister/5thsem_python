"""
 Evaluate the following expressions involving relational and logical operators:
 a. ’hi’ > ’hello’ and ’bye’ < ’Bye’
 b. ’hi’ > ’hello’ or ’bye’ < ’Bye’
 c. 7 >8or 5<6and’Iamfine>’Iamnotfine’
 d. 10 !=9 and 29 >= 29
 e. 10 !=9 and 29 >= 29 and ’hi’ > ’hello’ or ’bye’ < ’Bye’ and 7 <= 2.5
 f. 5 % 10 +10<50and29>=29
 g. 7 ** 2 <=5// 9 %3or’bye’ < ’Bye’
 h. 5 %10<8and-25>1*8//5
 i. 7 ** 2 // 4 + 5 > 8or 5!= 6
 j. 7/4 < 6 and ’I am fine > ’I am not fine’
 k. 10 + 6 * 2**2!=9//4-3 and 29 >= 29/9
 l. ’hello’ * 5 > ’hello’ or ’bye’ < ’Bye’
"""
a_result = 'hi' > 'hello' and 'bye' < 'Bye'
b_result = 'hi' > 'hello' or 'bye' < 'Bye'
c_result = 7 > 8 or 5 < 6 and 'I am fine' > 'I am not fine'
d_result = 10 != 9 and 29 >= 29
e_result = 10 != 9 and 29 >= 29 and 'hi' > 'hello' or 'bye' < 'Bye' and 7 <= 2.5
f_result = 5 % 10 + 10 < 50 and 29 >= 29
g_result = 7 ** 2 <= 5 // 9 % 3 or 'bye' < 'Bye'
h_result = 5 % 10 < 8 and -25 > 1 * 8 // 5
i_result = 7 ** 2 // 4 + 5 > 8 or 5 != 6
j_result = 7 / 4 < 6 and 'I am fine' > 'I am not fine'
k_result = 10 + 6 * 2 ** 2 != 9 // 4 - 3 and 29 >= 29 / 9
l_result = 'hello' * 5 > 'hello' or 'bye' < 'Bye'

print(a_result, b_result, c_result, d_result, e_result, f_result, g_result, h_result, i_result, j_result, k_result, l_result)

# False True False True True True False False True False True True