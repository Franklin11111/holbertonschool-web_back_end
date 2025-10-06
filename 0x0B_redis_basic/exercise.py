#!/usr/bin/env python3
"""
Module for managing Redis cache
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count  the number of calls.

    Args:
        method: The method to decorate

    Returns:
        Callable: Decorated method with calls counter
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper that increments counter before calling the method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that saves calls of a method.

    Args:
        method: Method do decorate

    Returns:
        Callable: Decorated method with records of calls
    """
    @wraps(method)
    def wrapper(self, *args):
        """
        Wrapper that saves entries and outputs of the method.
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Arguments of entries
        self._redis.rpush(inputs_key, str(args))

        # Execution of original method
        output = method(self, *args)

        # Outputs
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Display calls of the method.

    Args:
        method: The method that has calls to display
    """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    # Collection of entries and outputs
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    # Display the number of calls
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    # Display entries and outputs
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> "
              f"{output_data.decode('utf-8')}")


class Cache:
    """
    Class Cache that manages the instance of Redis for saving the data.
    This class allows saving of data of different types in Redis
    and manage the unique keys for each entry.
    """

    def __init__(self):
        """
        Initialize new instance Cache.
        Create new Redis connection and clean the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Keep the data in Redis with one general key.

        Args:
            data: Data to save

        Returns:
            str: The key under which the data is stored

        Example:
            >>> cache = Cache()
            >>> key = cache.store("hello")
            >>> print(cache._redis.get(key))
            b'hello'
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Collect the data stored in Redis and convert if necessary.

        Args:
            key: The key to collect the data
            fn: Optional function for converting the data

        Returns:
            The data converted according to the provided function
            or raw data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Collect the chain of characters stored in Redis.

        Args:
            key: The key to collect the data

        Returns:
            str: The chain of decoded characters
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Collect data saved in Redis.

        Args:
            key: The key collecting the data

        Returns:
            int: The value converted.
        """
        return self.get(key, fn=int)
