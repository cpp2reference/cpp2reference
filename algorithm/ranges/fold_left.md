---
layout: page
title: std::ranges::fold_left
permalink: /algorithm/ranges/fold_left/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/fold_left
godbolt: https://cpp2.godbolt.org/z/819MdP9qz
---
# std::ranges::fold_left

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    ranges: namespace == std::ranges;

    v: std::vector = (1, 2, 3, 4, 5, 6, 7, 8);

    sum:= ranges::fold_left(v.begin(), v.end(), 0, std::plus<int>());
    std::cout << "sum: (sum)$\n";

    mul:= ranges::fold_left(v, 1, std::multiplies<int>());
    std::cout << "mul: (mul)$\n";

    // get the product of the std::pair::second of all pairs in the vector:
    CharFloat: type == std::pair<char, float>;
    data: std::vector = (
        :CharFloat = ('A', 2.f),
        :CharFloat = ('B', 3.f),
        :CharFloat = ('C', 3.5f));
    sec: float = ranges::fold_left
    (
        data | ranges::views::values, 2.0f, std::multiplies<>()
    );
    std::cout << "sec: (sec)$\n";

    // use a program defined function object (lambda-expression):
    str: std::string = ranges::fold_left
    (
        v, "A", :(s: std::string, x: int) s + ':' + std::to_string(x)
    );
    std::cout << "str: (str)$\n";

    CD: type == std::complex<double>;
    nums: std::vector = (
        :CD=(1, 1),
        :CD=(2, 0),
        :CD=(3, 0));
    res:= ranges::fold_left(nums, CD(7, 0), std::multiplies());
    std::cout << "res: " << res << '\n';
}
```
{: .lh-0 }

## Output

```
sum: 36
mul: 40320
sec: 42.000000
str: A:1:2:3:4:5:6:7:8
res: (42,42)
```
{: .lh-0 }