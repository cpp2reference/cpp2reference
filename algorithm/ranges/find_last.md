---
layout: page
title: std::ranges::find_last, std::ranges::find_last_if, std::ranges::find_last_if_not
permalink: /algorithm/ranges/find_last/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/find_last
godbolt: https://cpp2.godbolt.org/z/8essz4xab
---
# std::ranges::find_last, std::ranges::find_last_if, std::ranges::find_last_if_not

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
ranges: namespace == std::ranges;

v: std::array == (1, 2, 3, 1, 2, 3, 1, 2);

main: () = {
    {
        i1: == ranges::find_last(v.begin(), v.end(), 3);
        i2: == ranges::find_last(v, 3);
        static_assert(ranges::distance(v.begin(), i1.begin()) == 5);
        static_assert(ranges::distance(v.begin(), i2.begin()) == 5);
    }
    {
        i1: == ranges::find_last(v.begin(), v.end(), -3);
        i2: == ranges::find_last(v, -3);
        static_assert(i1.begin() == v.end());
        static_assert(i2.begin() == v.end());
    }

    abs:== :(x: int) -> int = {
        if x < 0 {
            return -x;
        }
        else {
            return x;
        }
    };

    {
        pred:== :(x: int) x == 3;
        i1: == ranges::find_last_if(v.begin(), v.end(), pred, abs);
        i2: == ranges::find_last_if(v, pred, abs);
        static_assert(ranges::distance(v.begin(), i1.begin()) == 5);
        static_assert(ranges::distance(v.begin(), i2.begin()) == 5);
    }
    {
        pred:== :(x: int) x == -3;
        i1: == ranges::find_last_if(v.begin(), v.end(), pred, abs);
        i2: == ranges::find_last_if(v, pred, abs);
        static_assert(i1.begin() == v.end());
        static_assert(i2.begin() == v.end());
    }

    {
        pred:== :(x: int) x == 1 || x == 2;
        i1: == ranges::find_last_if_not(v.begin(), v.end(), pred, abs);
        i2: == ranges::find_last_if_not(v, pred, abs);
        static_assert(ranges::distance(v.begin(), i1.begin()) == 5);
        static_assert(ranges::distance(v.begin(), i2.begin()) == 5);
    }
    {
        pred:== :(x: int) x == 1 || x == 2 || x == 3;
        i1: == ranges::find_last_if_not(v.begin(), v.end(), pred, abs);
        i2: == ranges::find_last_if_not(v, pred, abs);
        static_assert(i1.begin() == v.end());
        static_assert(i2.begin() == v.end());
    }

    P: type == std::pair<std::string_view, int>;
    list: std::forward_list<P> = (
        :P = ("one", 1), :P = ("two", 2), :P = ("three", 3),
        :P = ("one", 4), :P = ("two", 5), :P = ("three", 6),
    );
    cmp_one:= :(s: std::string_view) s == "one";

    // find last element that satisfies the comparator, and projecting pair::first
    subrange:= ranges::find_last_if(list, cmp_one, P::first&);

    // print the found element and the "tail" after it
    for subrange do (e: P) {
        std::cout << '{' << std::quoted(e.first) << ", " << e.second << "} ";
    }
    std::cout << '\n';

    i3:= ranges::find_last(list, :P = ("three", 3));
    i3_front:= i3.begin();
    assert(i3_front*.first == "three" && i3_front*.second == 3);

    _ = list;
}
```
{: .lh-0 }

## Output

```
{"one", 4} {"two", 5} {"three", 6} 
```
{: .lh-0 }