import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    global curent_time
    def start_timing():
        function()
    time_taken = time.time() - current_time

    print (f"{function.__name__} run speed: {time_taken}")
    return function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
@speed_calc_decorator        
def slow_function():
    for i in range(1000000000000000000):
        i * i


