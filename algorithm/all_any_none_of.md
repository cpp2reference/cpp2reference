---
layout: page
title: std::all_of, std::any_of, std::none_of
permalink: /algorithm/all_any_none_of/
parent: Algorithms Library
cppreference: /algorithm/all_any_none_of
godbolt: https://cpp2.godbolt.org/z/565jqjPa6
---
# std::all_of, std::any_of, std::none_of

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
DivisibleBy: @struct type = {
    d: const int;
    operator() :(this, n: int) -> bool = {
        return n % d == 0;
    }
}

main: () = {
    v:= std::vector(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout << "Among the numbers: ";
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
 
    if std::all_of(v.cbegin(), v.cend(), :(i: int) i % 2 == 0) {
        std::cout << "All numbers are even\n";
    }
 
    if std::none_of(v.cbegin(), v.cend(), std::bind(std::modulus<>(),
                                                    std::placeholders::_1, 2)) {
        std::cout << "None of them are odd\n";
    }
 
    if std::any_of(v.cbegin(), v.cend(), DivisibleBy(7)) {
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