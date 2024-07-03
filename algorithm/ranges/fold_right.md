---
layout: page
title: std::ranges::fold_right
permalink: /algorithm/ranges/fold_right/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/fold_right
godbolt: https://cpp2.godbolt.org/z/vnv1WPa3W
---
# std::ranges::fold_right

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    using namespace std::literals;
    ranges: namespace == std::ranges;

    ai: std::array = (1, 2, 3, 4, 5, 6, 7, 8);
    vs: std::vector<std::string> = ("A", "B", "C", "D");

    r1:= ranges::fold_right(ai.begin(), ai.end(), 6, std::plus<>());
    std::cout << "r1: (r1)$\n";

    r2:= ranges::fold_right(vs, "!"s, std::plus<>());
    std::cout << "r2: (r2)$\n";

    // Use a program defined function object (lambda-expression):
    r3: std::string = ranges::fold_right
    (
        ai, "A", :(x: int, s: std::string) s + ':' + std::to_string(x)
    );
    std::cout << "r3: (r3)$\n";

    // Get the product of the std::pair::second of all pairs in the vector:
    CharFloat: type == std::pair<char, float>;
    data: std::vector = (
        :CharFloat=('A', 2.f),
        :CharFloat=('B', 3.f),
        :CharFloat=('C', 3.5f));
    r4: float = ranges::fold_right
    (
        data | ranges::views::values, 2.0f, std::multiplies<>()
    );
    std::cout << "r4: (r4)$\n";

    CD: type == std::complex<double>;
    nums: std::vector = (
        :CD=(1, 1),
        :CD=(2, 0),
        :CD=(3, 0));
    r5:= ranges::fold_right(nums, CD(7, 0), std::multiplies<>());
    std::cout << "r5: " << r5 << '\n';
}
```
{: .lh-0 }

## Output

```
r1: 42
r2: ABCD!
r3: A:8:7:6:5:4:3:2:1
r4: 42.000000
r5: (42,42)
```
{: .lh-0 }