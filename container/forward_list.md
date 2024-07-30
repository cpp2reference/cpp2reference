---
layout: page
title: std::forward_list
permalink: /container/forward_list/
parent: Containers library
cppreference: /container/forward_list
---
# std::forward_list

{% include cppreference_link.html %}

## Example

{% include godbolt/container/forward_list.html %}
{% include godbolt_example_link.html godbolt=url %}

```cpp
{% include src/container/forward_list.cpp2 %}
```
{: .lh-0 }

## Output

```
list: {1, 2, 3, 4, 5}
list: {1, -6, 2, 3, 4, 5}
list: {1, -6, -7, -7, 2, 3, 4, 5}
list: {1, -6, -7, -7, -8, -9, -10, 2, 3, 4, 5}
list: {1, -6, -7, -7, -8, -9, -10, -11, -12, -13, -14, 2, 3, 4, 5}
```
{: .lh-0 }
