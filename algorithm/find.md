---
layout: page
title: std::find, std::find_if, std::find_if_not
permalink: /algorithm/find/
parent: Algorithms library
cppreference: /algorithm/find
godbolt: https://cpp2.godbolt.org/z/Gzd4Phxqv
---
# std::find, std::find_if, std::find_if_not

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    v: std::array = (1, 2, 3, 4);
 
    for (3, 5) do (n: int) {
        find_it:= std::find(v.begin(), v.end(), n);
        if find_it == std::end(v) {
            std::cout << "v does not contain (n)$\n";
        }
        else {
            std::cout << "v contains (n)$\n";
        }
    }
 
    is_even:= :(i: int) i % 2 == 0;
 
    for (:std::array = (3, 1, 4), :std::array = (1, 3, 5)) do (w) {
        find_it:= std::find_if(begin(w), end(w), is_even);
        if find_it != std::end(w) {
            std::print("{} contains an even number {}\n", w, find_it*);
        }
        else {
            std::print("{} does not contain even numbers\n", w);
        }
    }
 
    nums: std::vector = (:std::complex<double> = (4, 2));
    it:= std::find(nums.begin(), nums.end(), std::complex<double>(4, 2));
    assert(it == nums.begin());   
}
```
{: .lh-0 }

## Output

```
v contains 3
v does not contain 5
[3, 1, 4] contains an even number 4
[1, 3, 5] does not contain even numbers
```
{: .lh-0 }