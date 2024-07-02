---
layout: page
title: std::ranges::fold_left_first
permalink: /algorithm/ranges/fold_left_first/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/fold_left_first
godbolt: https://cpp2.godbolt.org/z/KWTxGh8r8
---
# std::ranges::fold_left_first

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v: std::vector = (1, 2, 3, 4, 5, 6, 7, 8);

    sum:= std::ranges::fold_left_first(v.begin(), v.end(), std::plus<int>());
    std::cout << "sum: (sum.value())$\n";

    mul:= std::ranges::fold_left_first(v, std::multiplies<int>());
    std::cout << "mul: (mul.value())$\n";

    // get the product of the std::pair::second of all pairs in the vector:
    CharFloat: type == std::pair<char, float>;
    data: std::vector = (
        :CharFloat=('A', 3.f),
        :CharFloat=('B', 3.5f),
        :CharFloat=('C', 4.f));
    sec:= std::ranges::fold_left_first
    (
        data | std::ranges::views::values, std::multiplies<>()
    );
    std::cout << "sec: (sec*)$\n";

    // use a program defined function object (lambda-expression):
    val:= std::ranges::fold_left_first(v, :(x: int, y: int) x + y + 13);
    std::cout << "val: (val*)$\n";
}
```
{: .lh-0 }

## Output

```
sum: 36
mul: 40320
sec: 42.000000
val: 127
```
{: .lh-0 }