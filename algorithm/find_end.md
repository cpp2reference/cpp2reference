---
layout: page
title: std::find_end
permalink: /algorithm/find_end/
parent: Algorithms Library
cppreference: /algorithm/find_end
godbolt: https://cpp2.godbolt.org/z/667ezvY6c
---
# std::find_end

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print_result: (result, v) = {
    if result == v.end() {
        std::cout << "Sequence not found\n";
    }
    else {
        pos:= std::distance(v.begin(), result);
        std::cout << "Last occurrence is at: (pos)$\n";
    }
}

main: () = {
    v: const std::array = (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4);

    for (:std::array = (1, 2, 3), :std::array = (4, 5, 6)) do (x) {
        iter:= std::find_end(v.begin(), v.end(), x.begin(), x.end());
        print_result(iter, v);
    }

    for (:std::array = (-1, -2, -3), :std::array = (-4, -5, -6)) do (x) {
        iter:= std::find_end(v.begin(), v.end(),
                             x.begin(), x.end(),
                             :(x: int, y: int) std::abs(x) == std::abs(y)
                            );
        print_result(iter, v);
    }
}
```
{: .lh-0 }

## Output

```
Last occurrence is at: 8
Sequence not found
Last occurrence is at: 8
Sequence not found
```
{: .lh-0 }
