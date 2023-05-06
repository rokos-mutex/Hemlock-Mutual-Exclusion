"""
Title: Hemlock Mutual Exclusion
Authors:
-   Sebastian Bobadilla
-   Suhrid Gupta
Description: A python implementation of the Hemlock mutual exclusion algorithm.
"""

from threading import Thread, current_thread, Condition


class HemlockThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.grant = None


class Lock:
    def __init__(lock):
        # Initial value: None
        lock.tail = None
        lock.condition = Condition()

    def acquire(lock):
        self = current_thread()

        # If lock is currently empty, append thread to it
        if lock.tail is None:
            lock.tail, self.grant = (self, None)

        # Otherwise, lock is currently occupied by other thread, insert thread after lock
        else:
            self.grant, lock.tail = (lock.tail, self)

            # read the grant value of its predecessor
            predecessor = self.grant
            with lock.condition:
                while predecessor.grant != lock:
                    lock.condition.wait()

            # Once predecessor's grant value is lock, it means successor has completed critical section update
            # Update predecessor's grant value to None
            with lock.condition:
                predecessor.grant = None
                lock.condition.notify_all()

            # Set its own grant value to None and return from lock to access critical section
            predecessor = None

    def release(lock):
        self = current_thread()

        # If the lock tail address is equal to itself, this is the final thread in the queue
        # Set lock tail to None and return
        if lock.tail == self:
            lock.tail = None

        # Set own grant to lock to convey ownership to successor
        else:
            with lock.condition:
                self.grant = lock
                lock.condition.notify_all()

            # Wait until its own grant value gets reset to None
            with lock.condition:
                while self.grant is not None:
                    lock.condition.wait()

            # Once the value is reset to None, it means its successor has acknowledged the unlock method, return
