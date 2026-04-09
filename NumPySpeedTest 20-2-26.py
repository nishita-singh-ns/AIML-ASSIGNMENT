
    import time
    import numpy as np
    size = 1000000
    start = time.time()
    list1 = list(range(size))
    list2 = list(range(size))
    result_list = []
    for i in range(size):
        result_list.append(list1[i] + list2[i])
    end = time.time()
    print("Python List Time:", end - start)
    start = time.time()
    array1 = np.arange(size)
    array2 = np.arange(size)
    result_array = array1 + array2
    end = time.time()
    print("NumPy Array Time:", end - start)

output:

    Python List Time: 0.7971441745758057
    NumPy Array Time: 0.021925687789916992
