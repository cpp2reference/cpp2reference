---
layout: page
title: std::ranges::fold_left_with_iter
permalink: /algorithm/ranges/fold_left_with_iter/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/fold_left_with_iter
godbolt: https://cpp2.godbolt.org/z/Erfnv9Mvz
---
# std::ranges::fold_left_with_iter

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    ranges: namespace == std::ranges;

    v: std::vector = (1, 2, 3, 4, 5, 6, 7, 8);

    sum:= ranges::fold_left_with_iter(v.begin(), v.end(), 6, std::plus<int>());
    std::cout << "sum: (sum.value)$\n";
    assert(sum.value == 42);
    assert(sum.in == v.end());

    mul:= ranges::fold_left_with_iter(v, 0X69, std::multiplies<int>());
    std::cout << "mul: (mul.value)$\n";
    assert(mul.value == 4233600);
    assert(mul.in == v.end());

    // Get the product of the std::pair::second of all pairs in the vector:
    CharFloat: type == std::pair<char, float>;
    data: std::vector = (
        :CharFloat=('A', 2.f),
        :CharFloat=('B', 3.f),
        :CharFloat=('C', 3.5f));
    sec:= ranges::fold_left_with_iter
    (
        data | ranges::views::values, 2.0f, std::multiplies<>()
    );
    assert(sec.value == 42);

    // Use a program defined function object (lambda-expression):
    lambda:= :(x: int, y: int) x + 0B110 + y;
    val:= ranges::fold_left_with_iter(v, -42, lambda);
    assert(val.value == 42);
    assert(val.in == v.end());

    CD: type == std::complex<double>;
    nums: std::vector = (
        :CD=(1, 1),
        :CD=(2, 0),
        :CD=(3, 0));
    res:= ranges::fold_left_with_iter(nums, CD(7, 0), std::multiplies<>());
    assert(res.value == CD(42, 42));
}
```
{: .lh-0 }

## Output

```
sum: 42
mul: 4233600
```
{: .lh-0 }