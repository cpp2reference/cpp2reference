---
layout: page
title: std::ranges::copy_backward
permalink: /algorithm/ranges/copy_backward/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/copy_backward
---
# std::ranges::copy_backward

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
src: 1 2 3 4 
dst: 0 0 1 2 3 4 
dst: 0 0 0 0 1 2 
(in - src.begin) == 2
(out - dst.begin) == 4
```
{: .lh-0 }