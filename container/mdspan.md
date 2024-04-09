---
layout: page
title: std::mdspan
permalink: /container/mdspan/
parent: Containers library
cppreference: /container/mdspan
godbolt: https://cpp2.godbolt.org/z/Kf4qjdnx9
---
# std::mdspan

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v: std::vector = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
 
    // View data as contiguous memory representing 2 rows of 6 ints each
    ms2:= std::mdspan(v.data(), 2, 6);
    // View the same data as a 3D array 2 x 3 x 2
    ms3:= std::mdspan(v.data(), 2, 3, 2);
 
    // Write data using 2D view
    (copy i:= 0, extent0:= cpp2::unsafe_narrow<i32>(ms2.extent(0U)))
    while i != extent0 next i++ {
        (copy j:= 0, extent1:= cpp2::unsafe_narrow<i32>(ms2.extent(1U)))
        while j != extent1 next j++ {
            ms2[i, j] = i * 1000 + j;
        }
    }

    // Read back using 3D view
    (copy i: std::size_t = 0)
    while i != ms3.extent(0U) next i++ {
        std::println("slice @ i = {}", i);
        (copy j: std::size_t = 0)
        while j != ms3.extent(1U) next j++ {
            (copy k: std::size_t = 0)
            while k != ms3.extent(2U) next k++ {
                std::print("{} ", ms3[i, j, k]);
            }
            std::println("");
        }
    }
}
```
{: .lh-0 }

## Output

```
slice @ i = 0
0 1 
2 3 
4 5 
slice @ i = 1
1000 1001 
1002 1003 
1004 1005 
```
{: .lh-0 }
