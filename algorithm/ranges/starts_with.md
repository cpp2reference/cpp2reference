---
layout: page
title: std::ranges::starts_with
permalink: /algorithm/ranges/starts_with/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/starts_with
godbolt: https://cpp2.godbolt.org/z/hhMrf9x6b
---
# std::ranges::starts_with

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    using namespace std::literals;

    ascii_upper:== :(c: char) -> char == {
        if 'a' <= c && c <= 'z' {
            return cpp2::unsafe_narrow<char>(c + 'A' - 'a');
        }
        else {
            return c;
        }
    };

    cmp_ignore_case:== :(x: char, y: char) -> bool == {
        return ascii_upper$(x) == ascii_upper$(y);
    };

    static_assert( std::ranges::starts_with("const_cast", "const"sv));
    static_assert( std::ranges::starts_with("constexpr",  "const"sv));
    static_assert(!std::ranges::starts_with("volatile",   "const"sv));

    std::cout << std::boolalpha
              << std::ranges::starts_with("Constantinopolis", "constant"sv,
                                          (), ascii_upper, ascii_upper) << ' '
              << std::ranges::starts_with("Istanbul", "constant"sv,
                                          (), ascii_upper, ascii_upper) << ' '
              << std::ranges::starts_with("Metropolis", "metro"sv,
                                          cmp_ignore_case) << ' '
              << std::ranges::starts_with("Acropolis", "metro"sv,
                                          cmp_ignore_case) << '\n';

    v: std::array == (1, 3, 5, 7, 9);
    odd:== :(x: int) -> bool == x % 2;
    static_assert(std::ranges::starts_with(v, std::views::iota(1)
                                            | std::views::filter(odd)
                                            | std::views::take(3)));
}
```
{: .lh-0 }

## Output

```
true false true false
```
{: .lh-0 }