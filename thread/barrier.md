---
layout: page
title: std::barrier
permalink: /thread/barrier/
parent: Concurrency Support library
cppreference: /thread/barrier
godbolt: https://cpp2.godbolt.org/z/4de3Eqn39
---
# std::barrier

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
phase: std::string = "... done\nCleaning up...\n";

main: () = {
    workers: const std::array = ("Anil", "Busara", "Carl");
 
    on_completion:= :() = {
        // locking not needed here
        std::cout << phase;
        phase = "... done\n";
    };
 
    sync_point: std::barrier = (std::ssize(workers), on_completion);
 
    work:= :(name: std::string) = {
        product: std::string = "  (name)$ worked\n";
        std::osyncstream(std::cout) << product;  // ok, op<< call is atomic
        sync_point&$*.arrive_and_wait();
 
        product = "  (name)$ cleaned\n";
        std::osyncstream(std::cout) << product;
        sync_point&$*.arrive_and_wait();
    };
 
    std::cout << "Starting...\n";
    threads: std::vector<std::jthread> = ();
    threads.reserve(std::size(workers));
    for workers do (worker)
        threads.emplace_back(work, worker);
}
```
{: .lh-0 }

## Possible output

```
Starting...
  Anil worked
  Busara worked
  Carl worked
... done
Cleaning up...
  Carl cleaned
  Anil cleaned
  Busara cleaned
... done
```
{: .lh-0 }