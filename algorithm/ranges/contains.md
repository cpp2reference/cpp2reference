---
layout: page
title: std::ranges::contains, std::ranges::contains_subrange
permalink: /algorithm/ranges/contains/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/contains
godbolt: https://cpp2.godbolt.org/z/h6dGfdxeP
---
# std::ranges::contains, std::ranges::contains_subrange

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
ranges: namespace == std::ranges;

main: () = {
    haystack: std::array == (3, 1, 4, 1, 5);
    needle:   std::array == (1, 4, 1);
    bodkin:   std::array == (2, 5, 2);
 
    static_assert(
        ranges::contains(haystack, 4) &&
       !ranges::contains(haystack, 6) &&
        ranges::contains_subrange(haystack, needle) &&
       !ranges::contains_subrange(haystack, bodkin)
    );
 
    nums: std::array == (
        :std::complex<double> = (1, 2),
        :std::complex<double> = (3, 4),
        :std::complex<double> = (5, 6));
    static_assert(ranges::contains(nums, std::complex<double>(3, 4)));

    std::print("{} contains 4? {}\n",  haystack, ranges::contains(haystack, 4));
    std::print("{} contains {}? {}\n", haystack, needle, ranges::contains_subrange(haystack, needle));
    std::print("{} contains {}? {}\n", haystack, bodkin, ranges::contains_subrange(haystack, bodkin));
}
```
{: .lh-0 }

## Output

```
[3, 1, 4, 1, 5] contains 4? true
[3, 1, 4, 1, 5] contains [1, 4, 1]? true
[3, 1, 4, 1, 5] contains [2, 5, 2]? false
```
{: .lh-0 }