---
layout: page
title: Algorithms Library
permalink: /algorithm/
nav_order: 3
has_children: true
has_toc: false
cppreference: /algorithm
---

<style>
p {
    padding: 0px;
    margin: 0px;
}
</style>

# Algorithms library

{% include cppreference_link.html %}

## <a id="constrained"></a> [Constrained algorithms](ranges/index.md)

C++20 provides constrained versions of most algorithms in the namespace `std::ranges`.

```cpp
v: std::vector<int> = (7, 1, 4, 0, -1);
std::ranges::sort(v); // constrained algorithm
```
{: .lh-0 }

## <a id="nonmodifyingsequence"></a> Non-modifying sequence operations

### <a id="batch"></a> Batch operations

[for_each](for_each.md)
