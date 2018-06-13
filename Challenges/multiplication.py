 # Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.
for x in range(100,1000):
	for y in range(10,100):
		multiplication= x * y
		if(multiplication<10000):
			multiplication_1 = x * (y%10)
			multiplication_2 = x * (y//10)*10
			r1=multiplication//1000%10+multiplication_1//1000%10+multiplication_2//1000%10
			r2=multiplication//100%10+multiplication_1//100%10+multiplication_2//100%10+x//100%10
			r3=multiplication//10%10+multiplication_1//10%10+multiplication_2//10%10+x//10%10+y//10%10
			r4=multiplication%10+multiplication_1%10+multiplication_2%10+x%10+y%10
			if(r1==r2==r3==r4):
				print(f'{x} * {y} = {multiplication}, all columns adding up to {r1}.')