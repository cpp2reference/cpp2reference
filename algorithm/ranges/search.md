---
layout: page
title: std::ranges::search
permalink: /algorithm/ranges/search/
parent: Constrained algorithms
grand_parent: Algorithms Library
cppreference: /algorithm/ranges/search
godbolt: https://cpp2.godbolt.org/z/4c99Y34MM
---
# std::ranges::search

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
using namespace std::literals;

print: (id: int, haystack, needle, found) = {
    std::cout << "(id)$) search(\"(haystack)$\", \"(needle)$\"); ";
    first:= std::distance(haystack.begin(), found.begin());
    last:=  std::distance(haystack.begin(), found.end());
    if found.empty() {
        std::cout << "not found;";
    }
    else {
        std::cout << "found: \"";
        for found do (x) {
            std::cout << x;
        }
        std::cout << "\";";
    }
    std::cout << " subrange: {(first)$, (last)$}\n";
}

main: () = {
    haystack: == "abcd abcd"sv;
    needle:   == "bcd"sv;

    // the search uses iterator pairs begin()/end():
    found1:== std::ranges::search(
        haystack.begin(), haystack.end(),
        needle.begin(), needle.end());
    static_assert(found1.begin() != haystack.begin());
    print(1, haystack, needle, found1);

    // the search uses ranges r1, r2:
    found2:== std::ranges::search(haystack, needle);
    static_assert(found2.begin() != haystack.begin());
    print(2, haystack, needle, found2);

    // 'needle' range is empty:
    none:== ""sv;
    found3:== std::ranges::search(haystack, none);
    static_assert(found3.empty());
    print(3, haystack, none, found3);

    // 'needle' will not be found:
    awl:== "efg"sv;
    found4:== std::ranges::search(haystack, awl);
    static_assert(found4.empty());
    print(4, haystack, awl, found4);

    // the search uses custom comparator and projections:
    bodkin:== "234"sv;
    found5:= std::ranges::search(haystack, bodkin,
        :(x: int, y: int) x == y,  // pred
        :(x: int) std::toupper(x), // proj1
        :(y: int) y + 'A' - '1');  // proj2
    print(5, haystack, bodkin, found5);
}
```
{: .lh-0 }

## Output

```
1) search("abcd abcd", "bcd"); found: "bcd"; subrange: {1, 4}
2) search("abcd abcd", "bcd"); found: "bcd"; subrange: {1, 4}
3) search("abcd abcd", ""); not found; subrange: {0, 0}
4) search("abcd abcd", "efg"); not found; subrange: {9, 9}
5) search("abcd abcd", "234"); found: "bcd"; subrange: {1, 4}
```
{: .lh-0 }