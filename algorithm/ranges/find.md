---
layout: page
title: std::ranges::find, std::ranges::find_if, std::ranges::find_if_not
permalink: /algorithm/ranges/find/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/find
godbolt: https://cpp2.godbolt.org/z/h98fPh8oG
---
# std::ranges::find, std::ranges::find_if, std::ranges::find_if_not

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
ranges: namespace == std::ranges;

folk_info: @struct type = {
    uid:      u32;
    name:     std::string;
    position: std::string;
}

projector_example :() = {
    folks: std::vector = (
        :folk_info = (0, "Ana", "dev"),
        :folk_info = (1, "Bob", "devops"),
        :folk_info = (2, "Eve", "ops")
    );

    who:= "Eve";
    it:= std::ranges::find(folks, who, folk_info::name&);
    if it != folks.end() {
        std::println("Profile:");
        std::println("    UID: {}", it*.uid);
        std::println("    Name: {}", it*.name);
        std::println("    Position: {}", it*.position);
        std::println("");
    }
}

main: () = {
    projector_example();

    n1: const int = 3;
    n2: const int = 5;
    v: std::array = (4, 1, 3, 2);

    if ranges::find(v, n1) != v.end() {
        std::println("v contains: {}", n1);
    }
    else {
        std::println("v does not contain: {}", n1);
    }

    if ranges::find(v.begin(), v.end(), n2) != v.end() {
        std::println("v contains: {}", n2);
    }
    else {
        std::println("v does not contain: {}", n2);
    }

    is_even:= :(x: int) x % 2 == 0;

    (result:= ranges::find_if(v.begin(), v.end(), is_even))
    if result != v.end() {
        std::println("First even element in v: {}", result*);
    }
    else {
        std::println("No even elements in v");
    }

    (result:= ranges::find_if_not(v, is_even))
    if result != v.end() {
        std::println("First odd element in v: {}", result*);
    }
    else {
        std::println("No odd elements in v");
    }

    divides_13:= :(x: int) x % 13 == 0;

    (result:= ranges::find_if(v, divides_13))
    if result != v.end() {
        std::println("First element divisible by 13 in v: {}", result*);
    }
    else {
        std::println("No elements in v are divisible by 13");
    }

    (result:= ranges::find_if_not(v.begin(), v.end(), divides_13))
    if result != v.end() {
        std::println("First element indivisible by 13 in v: {}", result*);
    }
    else {
        std::println("All elements in v are divisible by 13");
    }

    nums: std::vector = (:std::complex<double> = (4, 2));
    it:= ranges::find(nums, std::complex<double>(4, 2));
    assert(it == nums.begin());
}
```
{: .lh-0 }

## Output

```
Profile:
    UID: 2
    Name: Eve
    Position: ops

v contains: 3
v does not contain: 5
First even element in v: 4
First odd element in v: 1
No elements in v are divisible by 13
First element indivisible by 13 in v: 4
```
{: .lh-0 }