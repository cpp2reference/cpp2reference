---
layout: page
title: std::at_quick_exit
permalink: /utility/program/at_quick_exit/
parent: Program support utilities
grand_parent: Utility library
cppreference: /utility/program/at_quick_exit
godbolt: https://cpp2.godbolt.org/z/soYMdasYj
---
# std::at_quick_exit

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
f1: () = {
    std::cout << "pushed first" << std::endl; // flush is intentional
}

extern "C" void f2()
{
    std::cout << "pushed second\n";
}

main: () = {
    f3:= :() = {
        std::cout << "pushed third\n";
    };
 
    std::at_quick_exit(f1);
    std::at_quick_exit(f2);
    std::at_quick_exit(f3);
    std::quick_exit(0);
}
```
{: .lh-0 }

## Output

```
pushed third
pushed second
pushed first
```
{: .lh-0 }