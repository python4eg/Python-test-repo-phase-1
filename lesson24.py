from typing import List, Any

class Queue:
    def __init__(self):
        self.__items: List[Any] = []
    
    def push(self, item: Any):
        self.__items.append(item)
    
    def pop(self) -> Any:
        return self.__items.pop(0)

class Stack:
    def __init__(self):
        self.__items: List[Any] = []
    
    def push(self, item: Any):
        self.__items.append(item)
    
    def pop(self) -> Any:
        return self.__items.pop()

class Deque:
    def __init__(self):
        self.__items: List[Any] = []
    
    def push_end(self, item: Any):
        self.__items.append(item)
    
    def push_start(self, item: Any):
        self.__items.insert(0, item)
    
    def pop_last(self) -> Any:
        return self.__items.pop()
    
    def pop_start(self) -> Any:
        return self.__items.pop(0)

