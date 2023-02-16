
# ========= Example 1 =========
# recursively compute the summation of numbersbetween 0 and n

def recursive_sum(n):
    """_summary_

    Args:
        n (int): the input number up to which we would like to sum
    """
    # The base case
    if n==0:
        return 0
    
    # The recursive case
    else:
        return n + recursive_sum(n-1)
    
print(recursive_sum(10))

#======= Example 2=========
# Recursively compute the factorial n!

def recursive_factorial(n):
    """_summary_

    Args:
        n (int): the input number 

    Returns:
        int: the computed factorial n!
    """
    # Base case
    if n==0:
        return 1
    else:
        return n*recursive_factorial(n-1)
    
#====== Example 3========
# The Fibonnacci sequence

# Use a dict to store already computed values
# This enables optimizing memeory and performance

fibonacci_dict = {0:0, 1:1}

def fibonacci(n):
    """Computes the Fibonnacci sequence value at given int n

    Args:
        n (int): the input number for which we would like to
        compute the Fibonacci sequence

    Returns:
        int: Fibonacci sequence value at input integer n
    """

    if n in fibonacci_dict:
        return fibonacci_dict[n]
    else:
        fibonacci_dict[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci_dict[n]
    
print(fibonacci(20))

print(fibonacci_dict)

# ======== Example 4 =======
# sum recursion lists
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def recursive_list_sum(liste):
    """recusively computes the sum of all elements in possibly nested lists

    Args:
        liste (list): the input list of elements

    Returns:
        int: the computed sum
    """
    s = 0
    for ele in liste:
        if isinstance(ele, list):
            s += recursive_list_sum(ele)
        else:
            s += ele
    return s

print("recursive_list_sum :", recursive_list_sum([1, 2, [3,4], [5,6]]))
print("recursive_list_sum :", recursive_list_sum([1, 2, [3,4,[7,8]], [5,6]]))