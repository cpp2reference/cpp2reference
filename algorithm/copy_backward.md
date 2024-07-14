---
layout: page
title: std::copy_backward
permalink: /algorithm/copy_backward/
parent: Algorithms library
cppreference: /algorithm/copy_backward
godbolt: https://cpp2.godbolt.org/z/Yjsa9Gezc
---
# std::copy_backward

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    source:= std::vector<int>(4);
    std::iota(source.begin(), source.end(), 1); // fills with 1, 2, 3, 4

    destination:= std::vector<int>(6);

    std::copy_backward(source.begin(), source.end(), destination.end());

    std::cout << "destination contains: ";
    for destination do (i) {
        std::cout << i << ' ';
    }
    std::cout << '\n';
}
```
{: .lh-0 }

## Output

```
destination contains: 0 0 1 2 3 4
```
{: .lh-0 }