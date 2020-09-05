


'''
Input==================
print('A:')
a_price= float(input())
a_quant= int(input())

print('B:')
b_price= float(input())
b_quant= int(input())

print('C:')
c_price= float(input())
c_quant= int(input())

print('D:')
d_price= float(input())
d_quant= int(input())
======================
'''

(a_price, a_quant) = (11.1, 1)
(b_price, b_quant) = (22.1, 2)
(c_price, c_quant) = (33.1, 3)
(d_price, d_quant) = (44.1, 4)


print('a : %s, %s '%( str(a_price), str(a_quant)))
print('b: %s, %s '%( str(b_price), str(b_quant)))
print('c : %s, %s '%( str(c_price), str(c_quant)))
print('d: %s, %s '%( str(d_price), str(d_quant)))


def main(a_price, a_quant, b_price, b_quant, c_price, c_quant, d_price, d_quant):

    is_valid = (a_price <= 50) and (b_price <= 30) and (d_quant >= 1 ) and (a_quant + c_quant <= 5)

    total_sum = (a_price*a_quant) + (b_price*b_quant) + (c_price*c_quant) + (d_price*d_quant)

    total_quant = a_quant + b_quant + c_quant + d_quant

    avg_price = total_sum / total_quant

    valid_message = "%s, %s, %s" % (total_sum, total_quant, avg_price)

    message_dict = {True : valid_message,
           False : 'Invalid purchase'}

    print(message_dict[is_valid])


main(a_price, a_quant, b_price, b_quant, c_price, c_quant, d_price, d_quant)