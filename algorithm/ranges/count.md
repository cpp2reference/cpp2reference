---
layout: page
title: std::ranges::count, std::ranges::count_if
permalink: /algorithm/ranges/count/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/count
godbolt: https://cpp2.godbolt.org/z/PvxcEEnc5
---
# std::ranges::count, std::ranges::count_if

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v: std::vector = (1, 2, 3, 4, 4, 3, 7, 8, 9, 10);
 
    ranges: namespace == std::ranges;
 
    // determine how many integers in a std::vector match a target value.
    target1: int = 3;
    target2: int = 5;
    num_items1:= ranges::count(v.begin(), v.end(), target1);
    num_items2:= ranges::count(v, target2);
    std::cout << "number: (target1)$ count: (num_items1)$\n";
    std::cout << "number: (target2)$ count: (num_items2)$\n";
 
    // use a lambda expression to count elements divisible by 3.
    num_items3:= ranges::count_if(v.begin(), v.end(), :(i: int) i % 3 == 0);
    std::cout << "number divisible by three: (num_items3)$\n";
 
    // use a lambda expression to count elements divisible by 11.
    num_items11:= ranges::count_if(v, :(i: int) i % 11 == 0);
    std::cout << "number divisible by eleven: (num_items11)$\n";
 
    nums: std::vector = (
        :std::complex<double> = (4, 2),
        :std::complex<double> = (1, 3),
        :std::complex<double> = (4, 2));
    c:= ranges::count(nums, std::complex<double>(4, 2));
    assert(c == 2);
}
```
{: .lh-0 }

## Output

```
number: 3 count: 2
number: 5 count: 0
number divisible by three: 3
number divisible by eleven: 0
```
{: .lh-0 }