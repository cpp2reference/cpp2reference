---
layout: page
title: std::stack
permalink: /container/stack/
parent: Containers library
cppreference: /container/stack
godbolt: https://cpp2.godbolt.org/z/a484399Tn
---
# std::stack

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
reportStackSize: (s: std::stack<int>) = {
    std::cout << "(s.size())$ elements on stack\n";
}
 
reportStackTop: (s: std::stack<int>) = {
    // Leaves element on stack
    std::cout << "Top element: (s.top())$\n";
}
 
main: () = {
    s: std::stack<int> = ();
    s.push(2);
    s.push(6);
    s.push(51);
 
    reportStackSize(s);
    reportStackTop(s);
 
    reportStackSize(s);
    s.pop();
 
    reportStackSize(s);
    reportStackTop(s);
}
```
{: .lh-0 }

## Output

```
3 elements on stack
Top element: 51
3 elements on stack
2 elements on stack
Top element: 6
```
{: .lh-0 }
