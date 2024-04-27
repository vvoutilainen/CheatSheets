
import time
import multiprocessing
from multiprocessing.pool import ThreadPool

def test_map_pool(job_list, pool):
    """https://stackoverflow.com/q/70700809/7037299"""
    print("-" * 60)
    print("Pool map")
    start = time.time()
    p = multiprocessing.Pool(pool)
    _ = sum(p.map(sum, job_list))
    print("Time: {:.2f}".format(time.time() - start))
    print("-" * 60)

def test_map_threadpool(job_list, pool):
    """https://stackoverflow.com/q/70700809/7037299"""
    print("-" * 60)
    print("ThreadPool map")
    start = time.time()
    p = ThreadPool(pool)
    _ = sum(p.map(sum, job_list))
    print("Time: {:.2f}".format(time.time() - start))
    print("-" * 60)

def test_loop(values_to_compare, values_compared_against):
    print("-" * 60)
    print("test_loop")
    start = time.time()
    values_out = []
    for vec in values_to_compare:
        if vec in values_compared_against:
            values_out.append(vec)
    print("Time: {:.2f}".format(time.time() - start))
    print("-" * 60)
    return values_out

def _is_in_compared(vec, values_compared_against):
    return vec if vec in values_compared_against else None

def test_loop_pool(values_to_compare, values_compared_against, pool):
    print("-" * 60)
    print("test_loop_pool")
    start = time.time()
    with multiprocessing.Pool(pool) as mpool:
        results = mpool.starmap(
            _is_in_compared,
            [(vec, values_compared_against) for vec in values_to_compare]
        )
    values_out = [result for result in results if result is not None]
    print("Time: {:.2f}".format(time.time() - start))
    print("-" * 60)
    return values_out
