---
layout: page
title: Algorithms library
permalink: /algorithm/
nav_order: 3
has_children: true
has_toc: false
cppreference: /algorithm
---

<style>
.main-content { line-height: 1.0; }
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

---
{: .my-2 }

[`find`](find.md)

[`find_if`](find.md)

[`find_if_not`](find.md)

---
{: .my-2 }

[`ranges::find`](ranges/find.md)

[`ranges::find_if`](ranges/find.md)

[`ranges::find_if_not`](ranges/find.md)

---
{: .my-2 }

[`ranges::find_last`](ranges/find_last.md)

[`ranges::find_last_if`](ranges/find_last.md)

[`ranges::find_last_if_not`](ranges/find_last.md)

---
{: .my-2 }

[`find_end`](find_end.md)

---
{: .my-2 }

[`ranges::find_end`](ranges/find_end.md)

---
{: .my-2 }

[`find_first_of`](find_first_of.md)

---
{: .my-2 }

[`ranges::find_first_of`](ranges/find_first_of.md)

---
{: .my-2 }

[`adjacent_find`](adjacent_find.md)

---
{: .my-2 }

[`ranges::adjacent_find`](ranges/adjacent_find.md)

---
{: .my-2 }

[`count`](count.md)

[`count_if`](count.md)

---
{: .my-2 }

[`ranges::count`](ranges/count.md)

[`ranges::count_if`](ranges/count.md)

---
{: .my-2 }

[`mismatch`](mismatch.md)

---
{: .my-2 }

[`ranges::mismatch`](ranges/mismatch.md)

---
{: .my-2 }

[`equal`](equal.md)

---
{: .my-2 }

[`ranges::equal`](ranges/equal.md)

---
{: .my-2 }

[`search`](search.md)

---
{: .my-2 }

[`ranges::search`](ranges/search.md)

---
{: .my-2 }

[`search_n`](search_n.md)

---
{: .my-2 }

[`ranges::search_n`](ranges/search_n.md)

---
{: .my-2 }

[`ranges::starts_with`](ranges/starts_with.md)

---
{: .my-2 }

[`ranges::ends_with`](ranges/ends_with.md)

### <a id="fold"></a> Fold operations

---
{: .my-2 }

[`ranges::fold_left`](ranges/fold_left.md)

---
{: .my-2 }

[`ranges::fold_left_first`](ranges/fold_left_first.md)

---
{: .my-2 }

[`ranges::fold_right`](ranges/fold_right.md)

---
{: .my-2 }

[`ranges::fold_right_last`](ranges/fold_right_last.md)

---
{: .my-2 }

[`ranges::fold_left_with_iter`](ranges/fold_left_with_iter.md)

---
{: .my-2 }

[`ranges::fold_left_first_with_iter`](ranges/fold_left_first_with_iter.md)

## <a id="modifyingsequence"></a> Modifying sequence operations

### <a id="copy"></a> Copy operations

---
{: .my-2 }

[`copy`](copy.md)

[`copy_if`](copy.md)

---
{: .my-2 }

[`ranges::copy`](ranges/copy.md)

[`ranges::copy_if`](ranges/copy.md)

---
{: .my-2 }

[`copy_n`](copy_n.md)

---
{: .my-2 }

[`ranges::copy_n`](ranges/copy_n.md)

---
{: .my-2 }

[`copy_backward`](copy_backward.md)

---
{: .my-2 }

[`ranges::copy_backward`](ranges/copy_backward.md)

---
{: .my-2 }

[`move`](move.md)

---
{: .my-2 }

[`ranges::move`](ranges/move.md)

---
{: .my-2 }

[`move_backward`](move_backward.md)

---
{: .my-2 }

[`ranges::move_backward`](ranges/move_backward.md)

### <a id="swap"></a> Swap operations

---
{: .my-2 }

[`swap_ranges`](swap_ranges.md)

---
{: .my-2 }

[`ranges::swap_ranges`](ranges/swap_ranges.md)

---
{: .my-2 }

[`iter_swap`](iter_swap.md)

### <a id="transform"></a> Transform operations

---
{: .my-2 }

[`transform`](transform.md)

---
{: .my-2 }

[`ranges::transform`](ranges/transform.md)

---
{: .my-2 }

[`replace`](replace.md)

[`replace_if`](replace.md)

---
{: .my-2 }

[`ranges::replace`](ranges/replace.md)

[`ranges::replace_if`](ranges/replace.md)

---
{: .my-2 }

[`replace_copy`](replace_copy.md)

[`replace_copy_if`](replace_copy.md)

---
{: .my-2 }

[`ranges::replace_copy`](ranges/replace_copy.md)

[`ranges::replace_copy_if`](ranges/replace_copy.md)

### <a id="generation"></a> Generation operations

---
{: .my-2 }

[`fill`](fill.md)

---
{: .my-2 }

[`ranges::fill`](ranges/fill.md)

---
{: .my-2 }

[`fill_n`](fill_n.md)

---
{: .my-2 }

[`ranges::fill_n`](ranges/fill_n.md)

---
{: .my-2 }

[`generate`](generate.md)

---
{: .my-2 }

[`ranges::generate`](ranges/generate.md)

---
{: .my-2 }

[`generate_n`](generate_n.md)

---
{: .my-2 }

[`ranges::generate_n`](ranges/generate_n.md)

### <a id="removing"></a> Removing operations

---
{: .my-2 }

[`remove`](remove.md)

[`remove_if`](remove.md)

---
{: .my-2 }

[`ranges::remove`](ranges/remove.md)

[`ranges::remove_if`](ranges/remove.md)

---
{: .my-2 }

[`remove_copy`](remove_copy.md)

[`remove_copy_if`](remove_copy.md)
