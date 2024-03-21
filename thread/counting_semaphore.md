---
layout: page
title: std::counting_semaphore, std::binary_semaphore
permalink: /thread/counting_semaphore/
parent: Concurrency Support Library
cppreference: /thread/counting_semaphore
godbolt: https://cpp2.godbolt.org/z/aY8Gn4Pqh
---
# std::counting_semaphore, std::binary_semaphore

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
// global binary semaphore instances
// object counts are set to zero
// objects are in non-signaled state
smphSignalMainToThread: std::binary_semaphore = (0);
smphSignalThreadToMain: std::binary_semaphore = (0);
 
ThreadProc: () = {
    // wait for a signal from the main proc
    // by attempting to decrement the semaphore
    smphSignalMainToThread.acquire();
 
    // this call blocks until the semaphore's count
    // is increased from the main proc
    std::cout << "[thread] Got the signal\n"; // response message
 
    // wait for 3 seconds to imitate some work
    // being done by the thread
    using namespace std::literals;
    std::this_thread::sleep_for(3s);
 
    std::cout << "[thread] Send the signal\n"; // message
 
    // signal the main proc back
    smphSignalThreadToMain.release();
}
 
main: () = {
    // create some worker thread
    thrWorker: std::thread = (ThreadProc);
 
    std::cout << "[main] Send the signal\n"; // message
 
    // signal the worker thread to start working
    // by increasing the semaphore's count
    smphSignalMainToThread.release();
 
    // wait until the worker thread is done doing the work
    // by attempting to decrement the semaphore's count
    smphSignalThreadToMain.acquire();
 
    std::cout << "[main] Got the signal\n"; // response message
    thrWorker.join();
}
```
{: .lh-0 }

## Output

```
[main] Send the signal
[thread] Got the signal
[thread] Send the signal
[main] Got the signal
```
{: .lh-0 }