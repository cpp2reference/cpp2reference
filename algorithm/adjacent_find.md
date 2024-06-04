---
layout: page
title: std::adjacent_find
permalink: /algorithm/adjacent_find/
parent: Algorithms Library
cppreference: /algorithm/adjacent_find
godbolt: https://cpp2.godbolt.org/z/7eYcxcdnT
---
# std::adjacent_find

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v1: std::vector = (0, 1, 2, 3, 40, 40, 41, 41, 5);

    i1:= std::adjacent_find(v1.begin(), v1.end());

    if i1 == v1.end() {
        std::cout << "No matching adjacent elements\n";
    }
    else {
        std::cout << "The first adjacent pair of equal elements is at "
                  << std::distance(v1.begin(), i1) << ": "
                  << i1* << '\n';
    }

    i2:= std::adjacent_find(v1.begin(), v1.end(), std::greater<int>());
    if i2 == v1.end() {
        std::cout << "The entire vector is sorted in ascending order\n";
    }
    else {
        std::cout << "The last element in the non-decreasing subsequence is at "
                  << std::distance(v1.begin(), i2) << ": " << i2* << '\n';
    }
}
```
{: .lh-0 }

## Output

```
The first adjacent pair of equal elements is at 4: 40
The last element in the non-decreasing subsequence is at 7: 41
```
{: .lh-0 }