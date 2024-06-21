---
layout: page
title: std::ranges::find_end
permalink: /algorithm/ranges/find_end/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/find_end
godbolt: https://cpp2.godbolt.org/z/oP36q4T83
---
# std::ranges::find_end

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print_result: (haystack, needle) = {
    pos:= std::distance(haystack.begin(), needle.begin());
    std::cout << "In \"";
    for haystack do (c) {
        std::cout << c;
    }
    std::cout << "\" found \"";
    for needle do (c) {
        std::cout << c;
    }
    p:= pos as std::size_t;
    std::println("\" at position [{}..{})", p, p + needle.size());
    std::println("{}{}", std::string(4 + p, ' '), std::string(needle.size(), '^'));
}

main: () = {
    using namespace std::literals;
    secret:== "password password word..."sv;
    wanted:== "password"sv;

    found1:== std::ranges::find_end(
        secret.cbegin(), secret.cend(),
        wanted.cbegin(), wanted.cend());
    print_result(secret, found1);

    found2:== std::ranges::find_end(secret, "word"sv);
    print_result(secret, found2);

    found3:= std::ranges::find_end(secret, "ORD"sv,
        :(x: char, y: char) -> bool = { // uses a binary predicate
            return std::tolower(x) == std::tolower(y);
        });
    print_result(secret, found3);

    found4:= std::ranges::find_end(secret, "SWORD"sv,
        std::ranges::equal_to(),
        std::identity(),             // projects the 1st range
        :(c: char) std::tolower(c)); // projects the 2nd range
    print_result(secret, found4);

    static_assert(std::ranges::find_end(secret, "PASS"sv).empty()); // => not found
}
```
{: .lh-0 }

## Output

```
In "password password word..." found "password" at position [9..17)
             ^^^^^^^^
In "password password word..." found "word" at position [18..22)
                      ^^^^
In "password password word..." found "ord" at position [19..22)
                       ^^^
In "password password word..." found "sword" at position [12..17)
                ^^^^^
```
{: .lh-0 }