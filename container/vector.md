---
layout: page
title: std::vector
permalink: /container/vector/
parent: Containers library
cppreference: /container/vector
---
# std::vector

{% include cppreference_link.html %}

## Example

<div class="code-example" markdown="1">
[Run on Compiler Explorer](https://cpp2.godbolt.org/z/WTsMaWWrn){: .btn }{:target="_blank"}
</div>
{: .m-0 .p-2 }

```cpp
main: () = {
    // Create a vector containing integers
    v: std::vector = (8, 4, 5, 9);
 
    // Add two more integers to vector
    v.push_back(6);
    v.push_back(9);
 
    // Overwrite element at position 2
    v[2] = -1;
 
    // Print out the vector
    for v do (n)
        std::cout << "(n)$ ";
    std::cout << '\n';
}
```
{: .lh-0 }

## Output

```
8 4 -1 9 6 9 
```
{: .lh-0 }