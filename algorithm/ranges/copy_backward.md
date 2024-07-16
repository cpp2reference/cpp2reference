---
layout: page
title: std::ranges::copy_backward
permalink: /algorithm/ranges/copy_backward/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/copy_backward
godbolt: https://cpp2.godbolt.org/z/G7Md875b7
---
# std::ranges::copy_backward

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print: <Rng>(rem: std::string_view, r: Rng)
    requires (std::ranges::forward_range<Rng>)
= {
    std::cout << "(rem)$: ";
    for r do (elem) {
        std::cout << "(elem)$ ";
    }
    std::cout << '\n';
}

main: () = {
    src: std::array = (1, 2, 3, 4);
    print("src", src);

    dst:= std::vector<int>(src.size() + 2);
    std::ranges::copy_backward(src, dst.end());
    print("dst", dst);

    std::ranges::fill(dst, 0);
    res:= std::ranges::copy_backward(src.begin(), src.end() - 2, dst.end());
    print("dst", dst);

    std::cout
        << "(in - src.begin) == " << std::distance(src.begin(), res.in) << '\n'
        << "(out - dst.begin) == " << std::distance(dst.begin(), res.out) << '\n';
}
```
{: .lh-0 }

## Output

```
src: 1 2 3 4 
dst: 0 0 1 2 3 4 
dst: 0 0 0 0 1 2 
(in - src.begin) == 2
(out - dst.begin) == 4
```
{: .lh-0 }