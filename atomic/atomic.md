---
layout: page
title: std::atomic
permalink: /atomic/atomic/
parent: Concurrency Support Library
cppreference: /atomic/atomic
godbolt: https://cpp2.godbolt.org/z/caxPaPxe5
---
# std::atomic

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
acnt: std::atomic_int = ();
cnt: int = 0;
 
f: () = {
    n:=0;
    do {
        acnt++;
        cnt++;
        // Note: for this example, relaxed memory order
        // is sufficient, e.g. acnt.fetch_add(1, std::memory_order_relaxed);
    } next n++ while n < 10000;
}

main: () = {
    {
        pool: std::vector<std::jthread> = ();
        n:=0;
        do {
            pool.emplace_back(f);
        } next n++ while n < 10;
    }
 
    std::cout << "The atomic counter is (acnt)$\n"
              << "The non-atomic counter is (cnt)$\n";
}
```
{: .lh-0 }

## Possible output

```
The atomic counter is 100000
The non-atomic counter is 95929
```
{: .lh-0 }