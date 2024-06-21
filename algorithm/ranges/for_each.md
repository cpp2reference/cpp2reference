---
layout: page
title: std::ranges::for_each
permalink: /algorithm/ranges/for_each/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/for_each
godbolt: https://cpp2.godbolt.org/z/Wcnxxj1vM
---
# std::ranges::for_each

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
Sum: @struct type = {
    operator(): (inout this, n: int) = { sum += n; }
    sum: int = 0;
}

main: () = {
    nums: std::vector = (3, 4, 2, 8, 15, 267);
 
    print:= :(n) = { std::cout << " (n)$"; };
 
    ranges: namespace == std::ranges;
    std::cout << "before:";
    ranges::for_each(std::as_const(nums), print);
    print('\n');
 
    ranges::for_each(nums, :(inout n: int) = n++);
 
    // calls Sum::operator() for each number
    res:= ranges::for_each(nums.begin(), nums.end(), Sum());
    assert(res.in == nums.end());
 
    std::cout << "after: ";
    ranges::for_each(nums.cbegin(), nums.cend(), print);
 
    std::cout << "\nsum: (res.fun.sum)$\n";
 
    pair: type == std::pair<int, std::string>; 
    pairs: std::vector = (:pair=(1,"one"), :pair=(2,"two"), :pair=(3,"three"));
 
    std::cout << "project the pair::first: ";
    ranges::for_each(pairs, print, :(p: pair) -> int = { return p.first; });
 
    std::cout << "\nproject the pair::second:";
    ranges::for_each(pairs, print, pair::second&);
    print('\n');
}
```
{: .lh-0 }

## Output

```
before: 3 4 2 8 15 267 
after:  4 5 3 9 16 268
sum: 305
project the pair::first:  1 2 3
project the pair::second: one two three 
```
{: .lh-0 }