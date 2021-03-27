# given values of A and B , we have to return the value of the expression pow(A,B) % C. using recursion
# the idea is simple 
# if the B value is even i.e 2^4 = 2^2 * 2^2 = 4 * 4 = 16
# if the B value is odd i.e 2 ^ 5 = 2 ^ 2 * 2 ^ 2 * 2 = 4 * 4 * 2 = 32
def pow_expression(A,B):
    # base condition
    if A == 0:
        return 0
    if B == 0:
        return 1
    if B % 2 == 0: # if the B value is Even
        return pow_expression(A,B//2) * pow_expression(A,B//2)
    else:
        return pow_expression(A,B//2) * pow_expression(A,B//2) * B 

# test case

A = 2
B = 3
r = pow_expression(A,B)
print(r)