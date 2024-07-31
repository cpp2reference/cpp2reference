---
layout: page
title: std::ranges::contains, std::ranges::contains_subrange
permalink: /algorithm/ranges/contains/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/contains
---
# std::ranges::contains, std::ranges::contains_subrange

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
[3, 1, 4, 1, 5] contains 4? true
[3, 1, 4, 1, 5] contains [1, 4, 1]? true
[3, 1, 4, 1, 5] contains [2, 5, 2]? false
```
{: .lh-0 }