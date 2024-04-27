
import psutil
import numpy as np

from tests import(
    test_map_pool,
    test_map_threadpool,
    test_loop,
    test_loop_pool,
)

print(
    "{} cores, {} when counting logical cores.".format(
        psutil.cpu_count(logical=False),
        psutil.cpu_count(),
    )
)

if __name__ == '__main__':
    job_list = [range(10000000)]*64
    test_map_pool(job_list, pool=4)
    test_map_threadpool(job_list, pool=4)

if __name__ == "__main__":
    values_to_compare = np.random.randint(low=0, high=20, size=[20000, 5]).tolist()
    values_compared_against = np.random.randint(low=0, high=20, size=[20000, 5]).tolist()
    out1 = test_loop(values_to_compare, values_compared_against)
    out2 = test_loop_pool(values_to_compare, values_compared_against, pool=4)
    print("Lists agree? {}".format(out1==out2))
