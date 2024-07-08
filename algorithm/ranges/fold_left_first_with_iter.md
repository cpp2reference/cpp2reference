---
layout: page
title: std::ranges::fold_left_first_with_iter
permalink: /algorithm/ranges/fold_left_first_with_iter/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/fold_left_first_with_iter
godbolt: https://cpp2.godbolt.org/z/dM6395b6z
---
# std::ranges::fold_left_first_with_iter

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v: std::vector = (1, 2, 3, 4, 5, 6, 7, 8);

    sum:= std::ranges::fold_left_first_with_iter
    (
        v.begin(), v.end(), std::plus<int>()
    );
    std::cout << "sum: " << sum.value.value() << '\n';
    assert(sum.in == v.end());

    mul:= std::ranges::fold_left_first_with_iter(v, std::multiplies<int>());
    std::cout << "mul: " << mul.value.value() << '\n';
    assert(mul.in == v.end());

    // get the product of the std::pair::second of all pairs in the vector:
    CharFloat: type == std::pair<char, float>;
    data: std::vector = (
        :CharFloat=('A', 2.f),
        :CharFloat=('B', 3.f),
        :CharFloat=('C', 7.f));
    sec:= std::ranges::fold_left_first_with_iter
    (
        data | std::ranges::views::values, std::multiplies<>()
    );
    std::cout << "sec: " << sec.value.value() << '\n';

    // use a program defined function object (lambda-expression):
    lambda:= :(x: int, y: int) x + y + 2;
    val:= std::ranges::fold_left_first_with_iter(v, lambda);
    std::cout << "val: " << val.value.value() << '\n';
    assert(val.in == v.end());
}
```
{: .lh-0 }

## Output

```
sum: 36
mul: 40320
sec: 42
val: 50
```
{: .lh-0 }