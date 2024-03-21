---
layout: page
title: std::deque
permalink: /container/deque/
parent: Containers library
cppreference: /container/deque
godbolt: https://cpp2.godbolt.org/z/55v3Ev3qE
---
# std::deque

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    // Create a deque containing integers
    d: std::deque = (7, 5, 16, 8);
 
    // Add an integer to the beginning and end of the deque
    d.push_front(13);
    d.push_back(25);
 
    // Iterate and print values of deque
    for d do (n)
        std::cout << "(n)$ ";
    std::cout << '\n';
}
```
{: .lh-0 }

## Output

```
13 7 5 16 8 25 
```
{: .lh-0 }