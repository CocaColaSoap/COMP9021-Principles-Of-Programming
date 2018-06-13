# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# Insert your code here
min_i = 10
max_i = 76
max_j = 87
max_k = 98
for i in range(min_i,max_i+1):
    i_digits = {i // 10, i % 10}
    if len(i_digits) != 2:
        continue
    for j in range(i,max_j+1):
        i_and_j_digits = i_digits.union((j // 10, j % 10))
        if len(i_and_j_digits) != 4:
            continue
        for k in range(j,max_k+1):
            i_and_j_and_k_digits = i_and_j_digits.union((k//10,k%10))
            if len(i_and_j_and_k_digits) != 6:
                continue
            product  = i*j*k
            if product >= 1_000_000:
                break
            product_digits = set()
            for items in str(product):
                product_digits.add(int(items))
            if product_digits == i_and_j_and_k_digits:
                print(f'{i} x {j} x {k} = {product} is a solution.')