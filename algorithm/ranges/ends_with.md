---
layout: page
title: std::ranges::ends_with
permalink: /algorithm/ranges/ends_with/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/ends_with
godbolt: https://cpp2.godbolt.org/z/dv4c144xr
---
# std::ranges::ends_with

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    static_assert(
        true
        && !std::ranges::ends_with("for",           "cast")
        &&  std::ranges::ends_with("dynamic_cast",  "cast")
        && !std::ranges::ends_with("as_const",      "cast")
        &&  std::ranges::ends_with("bit_cast",      "cast")
        && !std::ranges::ends_with("to_underlying", "cast")
        &&  std::ranges::ends_with(:std::array=(1, 2, 3, 4), :std::array=(3, 4))
        && !std::ranges::ends_with(:std::array=(1, 2, 3, 4), :std::array=(4, 5))
    );

    using namespace std::literals;

    std::cout << std::boolalpha
              << std::ranges::ends_with("Constantinopolis"sv, "polis"sv) << ' '
              << std::ranges::ends_with("Istanbul"sv,         "polis"sv) << ' '
              << std::ranges::ends_with("Metropolis"sv,       "polis"sv) << ' '
              << std::ranges::ends_with("Acropolis"sv,        "polis"sv) << '\n';
}
```
{: .lh-0 }

## Output

```
true false true true
```
{: .lh-0 }