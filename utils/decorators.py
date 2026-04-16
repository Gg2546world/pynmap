import time
from functools import wraps

def time_decorator(func):
    """time calculator"""

    @wraps(func)
    def wrapper(*arg,**keywords):

        start = time.time()

        result = func(*arg,**keywords)

        end = time.time()

        print (f"[+]scan finished in {end-start:.2f}s")

        return result
    
    return wrapper
