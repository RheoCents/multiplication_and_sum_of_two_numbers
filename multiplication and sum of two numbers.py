#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
user_input_1 = input('Can you please give me a number ')
user_input_2 = input('And another one ')
user_input_product = float(user_input_1)*float(user_input_2)

if user_input_product <= 1000: 
    print ('The product ', {user_input_product})
else:
    print ('The sum is ',(float(user_input_1) + float(user_input_2)))