---
layout: page
title: std::array
permalink: /container/array/
parent: Containers library
cppreference: /container/array
godbolt: https://cpp2.godbolt.org/z/5ze614vx9
---
# std::array

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    a1: std::array          = (1, 2, 3);  // Construct with CTAD
    a2: std::array<int, 3>  = (1, 2, 3);
 
    // Container operations are supported
    std::sort(a1.begin(), a1.end());
    std::ranges::reverse_copy(a2, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
 
    // Ranged for loop is supported
    a3: std::array<std::string, 2> = ("E", "\u018E");
    for a3 do (s)
        std::cout << "(s)$ ";
    std::cout << '\n';
 
    // Behavior of unspecified elements is the same as with built-in arrays
    _: std::array<int, 2> = ();  // List init, both elements are value
                                 // initialized, a6[0] = a6[1] = 0
    _: std::array<int, 2> = (1); // List init, unspecified element is value
                                 // initialized, a7[0] = 1, a7[1] = 0
}
```
{: .lh-0 }

## Output

```
3 2 1 
E Ǝ 
```
{: .lh-0 }
