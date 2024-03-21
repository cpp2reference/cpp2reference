---
layout: page
title: std::thread
permalink: /thread/thread/
parent: Concurrency Support Library
cppreference: /thread/thread
godbolt: https://cpp2.godbolt.org/z/PMxY4Ms5o
---
# std::thread

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
foo: () = {
    // simulate expensive operation
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
 
bar: () = {
    // simulate expensive operation
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
 
main: () = {
    std::cout << "starting first helper...\n";
    helper1: std::thread = (foo);
 
    std::cout << "starting second helper...\n";
    helper2: std::thread = (bar);
 
    std::cout << "waiting for helpers to finish..." << std::endl;
    helper1.join();
    helper2.join();
 
    std::cout << "done!\n";
}
```
{: .lh-0 }

## Output

```
starting first helper...
starting second helper...
waiting for helpers to finish...
done!
```
{: .lh-0 }