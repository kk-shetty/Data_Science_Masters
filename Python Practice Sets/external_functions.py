def print_series(start, end, step=1):
    for i in range(start, end+1, step):
        print(i)

def sum_of_first(number):
    result = sum(range(1, number+1))
    return result

def producer(queue, numbers):
    for number in numbers:
        queue.put(number)

def sum_of_queue(queue):
    sum = 0
    while not queue.empty():
        sum += queue.get()
    queue.put(sum)

def max_in_nested(list_of_lists, queue):
    for list in list_of_lists:
        queue.put(max(list))

def max_of_queue(queue):
    max_numbers = []
    while not queue.empty():
        max_numbers.append(queue.get())
        print(max_numbers)
    queue.put(max(max_numbers))

def square(x):
    return x**2



