---
layout: page
title: std::ranges::equal
permalink: /algorithm/ranges/equal/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/equal
godbolt: https://cpp2.godbolt.org/z/YK3z4GT6n
---
# std::ranges::equal

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
is_palindrome: (s: std::string_view) -> bool == {
    views: namespace == std::views;
    forward:=  s | views::take(s.size() / 2);
    backward:= s | views::reverse | views::take(s.size() / 2);
    return std::ranges::equal(forward, backward);
}

test: (s: std::string_view) = {
    text: std::string = "is";
    if !is_palindrome(s) {
        text += " not";
    }
    std::cout << std::quoted(s)
              << std::format(" {} a palindrome", text)
              << "\n";
}

main: () = {
    test("radar");
    test("hello");
    static_assert(is_palindrome("ABBA") && !is_palindrome("AC/DC"));
}
```
{: .lh-0 }

## Output

```
"radar" is a palindrome
"hello" is not a palindrome
```
{: .lh-0 }