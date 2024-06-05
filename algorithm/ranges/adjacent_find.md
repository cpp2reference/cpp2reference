---
layout: page
title: std::ranges::adjacent_find
permalink: /algorithm/ranges/adjacent_find/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/adjacent_find
godbolt: https://cpp2.godbolt.org/z/MEeb5f8bW
---
# std::ranges::adjacent_find

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
ranges: namespace == std::ranges;

some_of: (forward r, forward pred) -> bool  // some but not all
== {
    return
        ranges::cend(r) !=
        ranges::adjacent_find(r, :(x, y) pred$(x) != pred$(y));
}

a: std::array == (0, 0, 0, 0);
b: std::array == (1, 1, 1, 0);
c: std::array == (1, 1, 1, 1);

main: () = {
    // test some_of
    is_one:= :(x) x == 1;
    static_assert(!some_of(a, is_one) && some_of(b, is_one) && !some_of(c, is_one));

    v: std::array = (0, 1, 2, 3, 40, 40, 41, 41, 5);
    
    (it:= ranges::adjacent_find(v.begin(), v.end()))
    if it == v.end() {
        std::cout << "No matching adjacent elements\n";
    }
    else {
        std::cout << "The first adjacent pair of equal elements is at ["
                  << ranges::distance(v.begin(), it) << "] == " << it* << '\n';
    }

    (it:= ranges::adjacent_find(v, ranges::greater()))
    if it == v.end() {
        std::cout << "The entire vector is sorted in ascending order\n";
    }
    else {
        std::cout << "The last element in the non-decreasing subsequence is at ["
                  << ranges::distance(v.begin(), it) << "] == " << it* << '\n';
    }
}
```
{: .lh-0 }

## Output

```
The first adjacent pair of equal elements is at [4] == 40
The last element in the non-decreasing subsequence is at [7] == 41
```
{: .lh-0 }