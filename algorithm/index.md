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

---
{: .my-2 }

[`for_each`](for_each.md)

[`ranges::for_each`](ranges/for_each.md)

[`for_each_n`](for_each_n.md)

[`ranges::for_each_n`](ranges/for_each_n.md)

### <a id="search"></a> Search operations

---
{: .my-2 }

[`all_of`](all_any_none_of.md)

[`any_of`](all_any_none_of.md)

[`none_of`](all_any_none_of.md)

---
{: .my-2 }

[`ranges::all_of`](ranges/all_any_none_of.md)

[`ranges::any_of`](ranges/all_any_none_of.md)

[`ranges::none_of`](ranges/all_any_none_of.md)

---
{: .my-2 }

[`ranges::contains`](ranges/contains.md)

[`ranges::contains_subrange`](ranges/contains.md)
