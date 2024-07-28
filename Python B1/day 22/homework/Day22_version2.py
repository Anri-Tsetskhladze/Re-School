#Given a logarithm base X and two values A and B, return a sum of logratihms with the base X: 
import math

def logs(x, a, b):
    sum_of_logs = math.log(a*b, x)
    return sum_of_logs

print(logs(10, 100, 10)) 
