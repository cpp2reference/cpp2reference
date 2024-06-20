---
layout: page
title: std::ranges::search_n
permalink: /algorithm/ranges/search_n/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/search_n
godbolt: https://cpp2.godbolt.org/z/75vYov7Ma
---
# std::ranges::search_n

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
nums: std::array == (1, 2, 2, 3, 4, 1, 2, 2, 2, 1);

main: () = {
    ranges:  namespace == std::ranges;
    count_t: type == int;
    value_t: type == int;

    count: int == 3;
    value: int == 2;

    result1:== ranges::search_n(nums.begin(), nums.end(), count, value);
    static_assert // found
    (
        result1.size() == count &&
        std::distance(nums.begin(), result1.begin()) == 6 &&
        std::distance(nums.begin(), result1.end()) == 9
    );

    result2:== ranges::search_n(nums, count, value);
    static_assert // found
    (
        result2.size() == count &&
        std::distance(nums.begin(), result2.begin()) == 6 &&
        std::distance(nums.begin(), result2.end()) == 9
    );

    result3:== ranges::search_n(nums, count, value_t(5));
    static_assert // not found
    (
        result3.size() == 0 &&
        result3.begin() == result3.end() &&
        result3.end() == nums.end()
    );

    result4:== ranges::search_n(nums, count_t(0), value_t(1));
    static_assert // not found
    (
        result4.size() == 0 &&
        result4.begin() == result4.end() &&
        result4.end() == nums.begin()
    );

    symbol: char == 'B';
    to_ascii:= :(z: int) 'A' + z - 1;
    is_equal:= :(x: char, y: char) x == y;

    std::cout << "Find a sub-sequence " << std::string(count, symbol) << " in the ";
    std::ranges::transform(nums, std::ostream_iterator<char>(std::cout, ""), to_ascii);
    std::cout << '\n';

    result5:= ranges::search_n(nums, count, symbol, is_equal, to_ascii);
    if !result5.empty() {
        std::cout << "Found at position "
                  << ranges::distance(nums.begin(), result5.begin()) << '\n';
    }

    nums2: std::vector = (
        :std::complex<double> = (4, 2),
        :std::complex<double> = (4, 2),
        :std::complex<double> = (1, 3));
    it:= ranges::search_n(nums2, 2, std::complex<double>(4, 2));
    assert(it.size() == 2);
    _ = nums2;
}
```
{: .lh-0 }

## Output

```
Find a sub-sequence BBB in the ABBCDABBBA
Found at position 6
```
{: .lh-0 }
