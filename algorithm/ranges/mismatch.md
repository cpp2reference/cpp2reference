---
layout: page
title: std::ranges::mismatch
permalink: /algorithm/ranges/mismatch/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/mismatch
godbolt: https://cpp2.godbolt.org/z/GTo1Won18
---
# std::ranges::mismatch

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
mirror_ends: (str: std::string_view) -> std::string_view == {
    end:= std::ranges::mismatch(str, str | std::views::reverse).in1;
    return (str.cbegin(), end);
    _ = end;
}

main: () = {
    std::cout << mirror_ends("abXYZba") << '\n'
              << mirror_ends("abca") << '\n'
              << mirror_ends("ABBA") << '\n'
              << mirror_ends("level") << '\n';

    using namespace std::literals::string_view_literals;

    static_assert("123"sv == mirror_ends("123!@#321"));
    static_assert("radar"sv == mirror_ends("radar"));
}
```
{: .lh-0 }

## Output

```
ab
a
ABBA
level
```
{: .lh-0 }