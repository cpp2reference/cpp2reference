---
layout: page
title: std::ranges::fold_right_last
permalink: /algorithm/ranges/fold_right_last/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/fold_right_last
godbolt: https://cpp2.godbolt.org/z/KEbPjfKE5
---
# std::ranges::fold_right_last

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    ai: std::array = (1, 2, 3, 4, 5, 6, 7, 8);
    vs: std::vector<std::string> = ("A", "B", "C", "D");

    r1:= std::ranges::fold_right_last(ai.begin(), ai.end(), std::plus<>());
    std::cout << "r1: (r1*)$\n";

    r2:= std::ranges::fold_right_last(vs, std::plus<>());
    std::cout << "r2: (r2*)$\n";

    // Use a program defined function object (lambda-expression):
    r3:= std::ranges::fold_right_last(ai, :(x: int, y: int) x + y + 99);
    std::cout << "r3: (r3*)$\n";

    // Get the product of the std::pair::second of all pairs in the vector:
    CharFloat: type == std::pair<char, float>;
    data: std::vector = (
        :CharFloat=('A', 3.f),
        :CharFloat=('B', 3.5f),
        :CharFloat=('C', 4.f));
    r4:= std::ranges::fold_right_last
    (
        data | std::ranges::views::values, std::multiplies<>()
    );
    std::cout << "r4: (r4*)$\n";
}
```
{: .lh-0 }

## Output

```
r1: 36
r2: ABCD
r3: 729
r4: 42.000000
```
{: .lh-0 }