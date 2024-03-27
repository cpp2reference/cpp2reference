---
layout: page
title: std::multiset
permalink: /container/multiset/
parent: Containers library
cppreference: /container/multiset
godbolt: https://cpp2.godbolt.org/z/jMThz3e1T
---
# std::multiset

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    c: std::multiset = (1, 2, 3, 4, 1, 2, 3, 4);
 
    print:= :() = {
        std::cout << "c = { ";
        for c&$* do (n) {
            std::cout << "(n)$ ";
        }
        std::cout << "}\n";
    };
    print();
 
    std::cout << "Erase all odd numbers:\n";
    (copy it:= c.begin())
    while it != c.end() {
        if it* % 2 != 0 {
            it = c.erase(it);
        }
        else {
            it++;
        }
    }
    print();
 
    std::cout << "Erase 1, erased count: (c.erase(1))$\n";
    std::cout << "Erase 2, erased count: (c.erase(2))$\n";
    std::cout << "Erase 2, erased count: (c.erase(2))$\n";
    print();
}
```
{: .lh-0 }

## Output

```
c = { 1 1 2 2 3 3 4 4 }
Erase all odd numbers:
c = { 2 2 4 4 }
Erase 1, erased count: 0
Erase 2, erased count: 2
Erase 2, erased count: 0
c = { 4 4 }
```
{: .lh-0 }
