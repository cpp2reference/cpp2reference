---
layout: page
title: std::unordered_multimap
permalink: /container/unordered_multimap/
parent: Containers library
cppreference: /container/unordered_multimap
---
# std::unordered_multimap

{% include cppreference_link.html %}

## Example

{% include godbolt/container/unordered_multimap.html %}
{% include godbolt_example_link.html godbolt=url %}

```cpp
{% include src/container/unordered_multimap.cpp2 %}
```
{: .lh-0 }

## Possible output

```
Start: 3(c) 2(b) 1(a)
After extract and before insert: 3(c) 2(b)
End: 4(a) 3(c) 2(b)
```
{: .lh-0 }
