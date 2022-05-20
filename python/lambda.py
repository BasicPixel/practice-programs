# Some lambda examples
sum_lambda = lambda x, y: x + y
mult_lambda = lambda x, y: x * y

absolute_value_lambda = lambda x: x if x > 0 else x / -1

print(sum_lambda(2, 5))
print(mult_lambda(2, 5))
print(absolute_value_lambda(2), absolute_value_lambda(-1))
