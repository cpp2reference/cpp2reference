---
layout: page
title: std::search_n
permalink: /algorithm/search_n/
parent: Algorithms Library
cppreference: /algorithm/search_n
godbolt: https://cpp2.godbolt.org/z/fsYcaGTj1
---
# std::search_n

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
consecutive_values: (c, count, v) -> bool == {
    return std::search_n(std::begin(c), std::end(c), count, v) != std::end(c);
}

main: () = {
    sequence: std::string_view == ".0_0.000.0_0.";

    static_assert(consecutive_values(sequence, 3, '0'));

    for (4, 3, 2) do (n: int) {
        std::cout << std::boolalpha
                  << "Has (n)$ consecutive zeros: "
                  << consecutive_values(sequence, n, '0') << '\n';
    }

    nums: std::vector = (
        :std::complex<double> = (4, 2),
        :std::complex<double> = (4, 2),
        :std::complex<double> = (1, 3));
    it:= std::search_n(nums.cbegin(), nums.cend(), 2, std::complex<double>(4, 2));
    assert(it == nums.begin());
}
```
{: .lh-0 }

## Output

```
Has 4 consecutive zeros: false
Has 3 consecutive zeros: true
Has 2 consecutive zeros: true
```
{: .lh-0 }