---
layout: page
title: std::multimap
permalink: /container/multimap/
parent: Containers library
cppreference: /container/multimap
godbolt: https://cpp2.godbolt.org/z/7s9dfdGze
---
# std::multimap

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    example: std::multimap = (
        std::make_pair(1, 'a'),
        std::make_pair(2, 'b'));
 
    for (2, 5) do (x) {
        if example.contains(x) {
            std::cout << "(x)$: Found\n";
        }
        else {
            std::cout << "(x)$: Not found\n";
        }
    }
}
```
{: .lh-0 }

## Output

```
2: Found
5: Not found
```
{: .lh-0 }
