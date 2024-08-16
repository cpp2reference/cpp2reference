---
layout: page
title: std::ranges::lexicographical_compare
permalink: /algorithm/ranges/lexicographical_compare/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/lexicographical_compare
---
# std::ranges::lexicographical_compare

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Possible output

```
a b c d >= a b c d
d a b c >= c b d a
b d a c >= a d c b
a c d b <  c d a b
```
{: .lh-0 }