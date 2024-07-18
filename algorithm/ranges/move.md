---
layout: page
title: std::ranges::move
permalink: /algorithm/ranges/move/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/move
godbolt: https://cpp2.godbolt.org/z/d18M5nrb7
---
# std::ranges::move

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
using namespace std::literals::chrono_literals;

f: (n: std::chrono::milliseconds) = {
    std::this_thread::sleep_for(n);
    std::cout << "thread with n=(n.count())$ ms ended" << std::endl;
}

main: () = {
    v: std::vector<std::jthread> = ();
    v.emplace_back(f, 400ms);
    v.emplace_back(f, 600ms);
    v.emplace_back(f, 800ms);
    l: std::list<std::jthread> = ();

    // std::ranges::copy() would not compile, because std::jthread is noncopyable
    std::ranges::move(v.begin(), v.end(), std::back_inserter(l));
    _ = l;
}
```
{: .lh-0 }

## Output

```
thread with n=400 ms ended
thread with n=600 ms ended
thread with n=800 ms ended
```
{: .lh-0 }