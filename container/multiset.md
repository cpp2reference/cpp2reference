---
layout: page
title: std::multiset
permalink: /container/multiset/
parent: Containers library
cppreference: /container/multiset
---
# std::multiset

{% include cppreference_link.html %}

## Example

{% include godbolt/container/multiset.html %}
{% include godbolt_example_link.html godbolt=url %}

```cpp
{% include src/container/multiset.cpp2 %}
```
{: .lh-0 }

## Output

```
c = { 1 1 2 2 3 3 4 4 }
Erase all odd numbers:
c = { 2 2 4 4 }
Erase 1, erased count: 0
Erase 2, erased count: 2
Erase 2, erased count: 0
c = { 4 4 }
```
{: .lh-0 }
