---
layout: page
title: std::ranges::all_of, std::ranges::any_of, std::ranges::none_of
permalink: /algorithm/ranges/all_any_none_of/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/all_any_none_of
godbolt: https://cpp2.godbolt.org/z/5P8GqYK9r
---
# std::ranges::all_of, std::ranges::any_of, std::ranges::none_of

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
ranges: namespace == std::ranges;

some_of: (move r, move pred) -> bool == // some but not all
{
    return !(ranges::all_of(r, pred) || ranges::none_of(r, pred));
}

main: () = {

    {
        r: std::array == (1, 2, 3);
        static_assert(!some_of(r, :(x: int) x < 1));
        static_assert( some_of(r, :(x: int) x < 2));
        static_assert(!some_of(r, :(x: int) x < 4));
    }

    v:= std::vector<int>(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout << "Among the numbers: ";
    ranges::copy(v, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
 
    if ranges::all_of(v.cbegin(), v.cend(), :(i: int) i % 2 == 0) {
        std::cout << "All numbers are even\n";
    }
 
    if ranges::none_of(v, std::bind(std::modulus<int>(), std::placeholders::_1, 2)) {
        std::cout << "None of them are odd\n";
    }
 
    DivisibleBy:= :(d: int) -> _ = {
        return :(m: int) m % d$ == 0;
    };
 
    if ranges::any_of(v, DivisibleBy(7)) {
        std::cout << "At least one number is divisible by 7\n";
    }
}
```
{: .lh-0 }

## Output

```
Among the numbers: 2 4 6 8 10 12 14 16 18 20 
All numbers are even
None of them are odd
At least one number is divisible by 7
```
{: .lh-0 }