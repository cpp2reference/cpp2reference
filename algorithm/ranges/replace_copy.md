---
layout: page
title: std::ranges::replace_copy, std::ranges::replace_copy_if
permalink: /algorithm/ranges/replace_copy/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/replace_copy
---
# std::ranges::replace_copy, std::ranges::replace_copy_if

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
p: 1 6 1 6 1 6 
o: 1 9 1 9 1 9 
q: 1 2 3 6 7 8 4 5 
o: 1 2 3 5 5 5 4 5 
r: (1,3) (2,2) (4,8) 
s: (2.2,4.8) (2,2) (4,8) 
b: (1,3) (2,2) (4,8) 
d: (4,2) (4,2) (4,8)  
```
{: .lh-0 }