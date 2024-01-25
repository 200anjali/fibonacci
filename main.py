import redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
def fibonacci(n:int):
    if n <= 1:
        result = n
    if redis_client.exists(n):
        return int(redis_client.get(n))
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        redis_client.set(n, result)
        cache_size_limit = 10
        if redis_client.dbsize() > cache_size_limit:
            oldest_key = min(redis_client.scan_iter(), key=lambda x: x.decode('utf-8'))
            redis_client.delete(oldest_key)
    return result
n = int(input())
result = fibonacci(n)
print("The {n}th Fibonacci is: {result}")

