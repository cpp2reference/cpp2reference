---
layout: page
title: std::for_each_n
permalink: /algorithm/for_each_n/
parent: Algorithms library
cppreference: /algorithm/for_each_n
godbolt: https://cpp2.godbolt.org/z/M7ccPsTv6
---
# std::for_each_n

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    vi: std::vector = (1, 2, 3, 4, 5);
    println(vi);
 
    std::for_each_n(vi.begin(), 3, :(inout n) = n *= 2);
    println(vi);
}

println: (v) = {
    (copy count:= v.size())
    for v do (e) {
        std::cout << e;
        count--;
        if count == 0 {
            std::cout << "\n";
        }
        else {
            std::cout << ", ";
        }
    }
}
```
{: .lh-0 }

## Output

```
1, 2, 3, 4, 5
2, 4, 6, 4, 5
```
{: .lh-0 }