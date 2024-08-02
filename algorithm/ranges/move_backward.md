---
layout: page
title: std::ranges::move_backward
permalink: /algorithm/ranges/move_backward/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/move_backward
---
# std::ranges::move_backward

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
Before move:
a[8]: 
▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 
b[8]: 
· · · · · · · · 

Move a >> b:
a[8]: 
· · · · · · · · 
b[8]: 
▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 

Move b >> a:
a[8]: 
▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 
b[8]: 
· · · · · · · · 

Overlapping move a[0, 3) >> a[5, 8):
a[8]: 
· · · ▄ ▅ ▁ ▂ ▃ 
```
{: .lh-0 }