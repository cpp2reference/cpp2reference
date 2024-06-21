---
layout: page
title: std::equal
permalink: /algorithm/equal/
parent: Algorithms library
cppreference: /algorithm/equal
godbolt: https://cpp2.godbolt.org/z/15G73a1fc
---
# std::equal

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
is_palindrome: (str: std::string_view) -> bool == {
    return std::equal(str.cbegin(), str.cbegin() + str.size() / 2, str.crbegin());
}

test: (str: std::string_view) = {
    text: std::string;
    if is_palindrome(str) {
        text = "is";
    }
    else {
        text = "is not";
    }
    std::cout << std::quoted(str)
              << std::format(" {} a palindrome", text)
              << "\n";
}

main: () = {
    test("radar");
    test("hello");

    static_assert(is_palindrome("civic"));
}
```
{: .lh-0 }

## Output

```
"radar" is a palindrome
"hello" is not a palindrome
```
{: .lh-0 }