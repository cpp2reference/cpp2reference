---
layout: page
title: std::mutex
permalink: /thread/mutex/
parent: Concurrency Support Library
cppreference: /thread/mutex
godbolt: https://cpp2.godbolt.org/z/ne5Y4T1ch
---
# std::mutex

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
g_pages:       std::map<std::string, std::string> = ();
g_pages_mutex: std::mutex = ();
 
save_page: (url: std::string) = {
    // simulate a long page fetch
    std::this_thread::sleep_for(std::chrono::seconds(2));
    result: const std::string = "fake content";
 
    _: std::lock_guard = (g_pages_mutex);
    g_pages[url] = result;
}
 
main: () = {
    t1: std::thread = (save_page, "http://foo");
    t2: std::thread = (save_page, "http://bar");
    t1.join();
    t2.join();
 
    // safe to access g_pages without lock now, as the threads are joined
    for g_pages do (pair)
        std::cout << "(pair.first)$ => (pair.second)$\n";
}
```
{: .lh-0 }

## Output

```
http://bar => fake content
http://foo => fake content
```
{: .lh-0 }