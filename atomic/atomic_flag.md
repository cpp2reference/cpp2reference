---
layout: page
title: std::atomic_flag
permalink: /atomic/atomic_flag/
parent: Concurrency Support Library
cppreference: /atomic/atomic_flag
godbolt: https://cpp2.godbolt.org/z/9KTWe8nsM
---
# std::atomic_flag

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
lock: std::atomic_flag = ATOMIC_FLAG_INIT;
out: int = 0;

f: (n: int) = {
    cnt: int = 0;
    do {
        while lock.test_and_set(std::memory_order_acquire) { // acquire lock
            while lock.test(std::memory_order_relaxed) // test lock
                {} // spin
        }
        ch: char = ();
        if out++ % 40 == 0 { ch = '\n'; } else { ch = ' '; }
        std::cout << n << ch;
        lock.clear(std::memory_order_release); // release lock
    } next cnt++ while cnt < 40;
}

main: () = {
    v: std::vector<std::thread> = ();
    n: int = 0;
    do {
        v.emplace_back(f, n);
    } next n++ while n < 10;
        
    for v do (inout t)
        t.join();
}
```
{: .lh-0 }

## Possible output

```
0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
```
{: .lh-0 }