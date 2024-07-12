---
layout: page
title: std::ranges::copy_n
permalink: /algorithm/ranges/copy_n/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/copy_n
godbolt: https://cpp2.godbolt.org/z/YbTdqnbWW
---
# std::ranges::copy_n

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    src: const std::string_view = "ABCDEFGH";
    dst: std::string = ();

    std::ranges::copy_n(src.begin(), 4, std::back_inserter(dst));
    std::cout << std::quoted(dst) << '\n';

    dst = "abcdefgh";
    res:= std::ranges::copy_n(src.begin(), 5, dst.begin());
    std::cout
        << "res.in:  '" << (res.in)* << "', distance: "
        << std::distance(std::begin(src), res.in) << '\n'
        << "res.out: '" << (res.out)* << "', distance: "
        << std::distance(std::begin(dst), res.out) << '\n';

    _ = src;
    _ = dst;
}
```
{: .lh-0 }

## Output

```
"ABCD"
res.in:  'F', distance: 5
res.out: 'f', distance: 5
```
{: .lh-0 }