---
layout: page
title: std::search
permalink: /algorithm/search/
parent: Algorithms library
cppreference: /algorithm/search
godbolt: https://cpp2.godbolt.org/z/9jxd43Gqa
---
# std::search

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
using namespace std::literals;

contains: (cont, s: std::string_view) -> bool == {
    return std::search(cont.begin(), cont.end(), s.begin(), s.end()) != cont.end();
}

main: () = {
    str:== "why waste time learning, when ignorance is instantaneous?"sv;
    static_assert(contains(str, "learning"));
    static_assert(!contains(str, "lemming"));

    vec: const _ = std::vector(str.begin(), str.end());
    assert(contains(vec, "learning"));
    assert(!contains(vec, "leaning"));

    quote:= "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"sv;

    for ("pisci"sv, "Pisci"sv) do (word) {
        std::cout << "The string " << std::quoted(word) << ' ';
        searcher: const std::boyer_moore_searcher = (word.begin(), word.end());
        it:= std::search(quote.begin(), quote.end(), searcher);
        if it == quote.end() {
            std::cout << "not found\n";
        }
        else {
            offset:= std::distance(quote.begin(), it);
            std::cout << "found at offset (offset)$\n";
        }
    }
}
```
{: .lh-0 }

## Output

```
The string "pisci" found at offset 43
The string "Pisci" not found
```
{: .lh-0 }