
# Hemlock: Compact and Scalable Mutual Exclusion

A python implementation of the Hemlock algorithm, which offers a compact and scalable solution for mutual exclusion.
The original paper for this implementation can be found [here](https://dl.acm.org/doi/10.1145/3409964.3461805)

# Example

```py
from hemlock import HemlockThread, Lock
mutex = Lock()

def critical_section():
  mutex.lock()
  # Access critical section
  mutex.unlock()
  
t1 = HemlockThread(target=critical_section)
t2 = HemlockThread(target=critical_section)
t1.start()
t2.start()
t1.join()
t2.join()
  
```
