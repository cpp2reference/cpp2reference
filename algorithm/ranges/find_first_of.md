---
layout: page
title: std::ranges::find_first_of
permalink: /algorithm/ranges/find_first_of/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/find_first_of
godbolt: https://cpp2.godbolt.org/z/o1x3Pde9h
---
# std::ranges::find_first_of

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
P: @struct type = {
    x: int;
    y: int;
}

haystack: std::array == (1, 2, 3, 4);
needles:  std::array == (0, 3, 4, 3);

main: () = {
    rng: namespace == std::ranges;

    found1:== rng::find_first_of(haystack.begin(), haystack.end(),
                                 needles.begin(), needles.end());
    static_assert(std::distance(haystack.begin(), found1) == 2);

    found2:== rng::find_first_of(haystack, needles);
    static_assert(std::distance(haystack.begin(), found2) == 2);

    negatives: std::array == (-6, -3, -4, -3);
    not_found:== rng::find_first_of(haystack, negatives);
    static_assert(not_found == haystack.end());

    found3:== rng::find_first_of(haystack, negatives,
        :(x: int, y: int) x == -y); // uses a binary comparator
    static_assert(std::distance(haystack.begin(), found3) == 2);

    p1: std::array == (:P=(1, -1), :P=(2, -2), :P=(3, -3), :P=(4, -4));
    p2: std::array == (:P=(5, -5), :P=(6, -3), :P=(7, -5), :P=(8, -3));

    // Compare only P::y data members by projecting them:
    found4:= rng::find_first_of(p1, p2, rng::equal_to(), P::y&, P::y&);
    std::cout << "First equivalent element {" << found4*.x << ", " << found4*.y
              << "} was found at position " << std::distance(p1.begin(), found4)
              << ".\n";
}
```
{: .lh-0 }

## Output

```
First equivalent element {3, -3} was found at position 2.
```
{: .lh-0 }