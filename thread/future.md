---
layout: page
title: std::future
permalink: /thread/future/
parent: Concurrency Support library
cppreference: /thread/future
godbolt: https://cpp2.godbolt.org/z/7e8beYqhe
---

# std::future

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    // future from a packaged_task
    task: std::packaged_task<int()> = :() -> int = 7; // wrap the function
    f1:   std::future<int> = task.get_future(); // get a future
    t1:   std::thread = (move task); // launch on a thread
 
    // future from an async()
    f2: std::future<int> = std::async(std::launch::async, :() -> int = 8);
 
    // future from a promise
    p:  std::promise<int> = ();
    f3: std::future<int> = p.get_future();
    std::thread(:() = p&$*.set_value_at_thread_exit(9)).detach();
 
    std::cout << "Waiting..." << std::flush;
    f1.wait();
    f2.wait();
    f3.wait();
    std::cout << "Done!\nResults are: (f1.get())$ (f2.get())$ (f3.get())$\n";
    t1.join();
}
```
{: .lh-0 }

## Output

```
Waiting...Done!
Results are: 7 8 9
```
{: .lh-0 }