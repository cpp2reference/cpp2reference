---
layout: page
title: std::forward_list
permalink: /container/forward_list/
parent: Containers library
cppreference: /container/forward_list
godbolt: https://cpp2.godbolt.org/z/b8vnvrKKh
---
# std::forward_list

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print: (list: std::forward_list<int>) = {
    std::cout << "list: {";
    (copy comma: std::string = ())
    for list do (i) {
        std::cout << "(comma)$(i)$";
        comma = ", ";
    }
    std::cout << "}\n";
}

main: () = {
    ints: std::forward_list = (1, 2, 3, 4, 5);
    print(ints);
 
    // insert_after (pos, value)
    beginIt:= ints.begin();
    ints.insert_after(beginIt, -6);
    print(ints);
 
    // insert_after (pos, count, value)
    anotherIt:= beginIt;
    anotherIt++;
    anotherIt = ints.insert_after(anotherIt, 2 as size_t, -7);
    print(ints);
 
    // insert_after (pos, first, last)
    v: const std::vector = (-8, -9, -10);
    anotherIt = ints.insert_after(anotherIt, v.cbegin(), v.cend());
    print(ints);
 
    // insert_after (pos, initializer_list)
    x: std::initializer_list<int> = (-11, -12, -13, -14);
    ints.insert_after(anotherIt, x);
    print(ints);
}
```
{: .lh-0 }

## Output

```
list: {1, 2, 3, 4, 5}
list: {1, -6, 2, 3, 4, 5}
list: {1, -6, -7, -7, 2, 3, 4, 5}
list: {1, -6, -7, -7, -8, -9, -10, 2, 3, 4, 5}
list: {1, -6, -7, -7, -8, -9, -10, -11, -12, -13, -14, 2, 3, 4, 5}
```
{: .lh-0 }
