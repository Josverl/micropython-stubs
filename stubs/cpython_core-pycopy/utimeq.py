import heapq
from utime import ticks_diff


class Entry:

    def __init__(self, time, obj, userdata):
        self.time = time
        self.obj = obj
        self.userdata = userdata

    def __lt__(self, another):
        return ticks_diff(self.time, another.time) < 0


class utimeq:

    def __init__(self, sz):
        self.heap = []
        self.max_sz = sz

    def __bool__(self):
        return bool(self.heap)

    def push(self, time, obj, userdata):
        e = Entry(time, obj, userdata)
        heapq.heappush(self.heap, e)
        return id(e)

    def pop(self, arr):
        e = heapq.heappop(self.heap)
        arr[0] = e.time
        arr[1] = e.obj
        arr[2] = e.userdata

    def peektime(self):
        return self.heap[0].time

    def remove(self, id):
        raise NotImplementedError
