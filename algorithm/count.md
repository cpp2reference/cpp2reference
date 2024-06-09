---
layout: page
title: std::count, std::count_if
permalink: /algorithm/count/
parent: Algorithms Library
cppreference: /algorithm/count
godbolt: https://cpp2.godbolt.org/z/rT5PY657d
---
# std::count, std::count_if

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v: std::array == (1, 2, 3, 4, 4, 3, 7, 8, 9, 10);
    std::cout << "v: ";
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
 
    // Determine how many integers match a target value.
    for (3, 4, 5) do (target) {
        num_items:= std::count(v.cbegin(), v.cend(), target);
        std::cout << "number: (target)$, count: (num_items)$\n";
    }
 
    // Use a lambda expression to count elements divisible by 4.
    count_div4:= std::count_if(v.begin(), v.end(), :(i: int) i % 4);
    std::cout << "numbers divisible by four: (count_div4)$\n";
 
    // A simplified version of `distance` with O(N) complexity:
    distance: == :(first, last) -> _ == {
        return std::count_if(first, last, :(_) -> _ == { return true; });
    };
    static_assert(distance(v.begin(), v.end()) == 10);
 
    nums: std::array = (
        :std::complex<double> = (4, 2),
        :std::complex<double> = (1, 3),
        :std::complex<double> = (4, 2));
    c:= std::count(nums.cbegin(), nums.cend(), std::complex<double>(4, 2));
    assert(c == 2);
}
```
{: .lh-0 }

## Output

```
v: 1 2 3 4 4 3 7 8 9 10 
number: 3, count: 2
number: 4, count: 2
number: 5, count: 0
numbers divisible by four: 7
```
{: .lh-0 }