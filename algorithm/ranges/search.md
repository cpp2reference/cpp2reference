---
layout: page
title: std::ranges::search
permalink: /algorithm/ranges/search/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/search
---
# std::ranges::search

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
1) search("abcd abcd", "bcd"); found: "bcd"; subrange: {1, 4}
2) search("abcd abcd", "bcd"); found: "bcd"; subrange: {1, 4}
3) search("abcd abcd", ""); not found; subrange: {0, 0}
4) search("abcd abcd", "efg"); not found; subrange: {9, 9}
5) search("abcd abcd", "234"); found: "bcd"; subrange: {1, 4}
```
{: .lh-0 }