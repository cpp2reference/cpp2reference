---
layout: page
title: std::mdspan
permalink: /container/mdspan/
parent: Containers library
cppreference: /container/mdspan
---
# std::mdspan

{% include cppreference_link.html %}

## Example

{% include godbolt/container/mdspan.html %}
{% include godbolt_example_link.html godbolt=url %}

```cpp
{% include src/container/mdspan.cpp2 %}
```
{: .lh-0 }

## Output

```
slice @ i = 0
0 1 
2 3 
4 5 
slice @ i = 1
1000 1001 
1002 1003 
1004 1005 
```
{: .lh-0 }
