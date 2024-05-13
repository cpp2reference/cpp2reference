---
layout: page
title: std::for_each
permalink: /algorithm/for_each/
parent: Algorithms Library
cppreference: /algorithm/for_each
godbolt: https://cpp2.godbolt.org/z/Ebe8Mjas9
---
# std::for_each

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
Sum: @struct type = {
    operator(): (inout this, n: int) = { sum += n; }
    sum: int = 0;
}

main: () = {
    v: std::vector = (3, -4, 2, -8, 15, 267);
 
    print:= :(n: int) = { std::cout << "(n)$ "; };
 
    std::cout << "before:\t";
    std::for_each(v.cbegin(), v.cend(), print);
    std::cout << '\n';
 
    // increment elements in-place
    std::for_each(v.begin(), v.end(), :(inout n) = n++);
 
    std::cout << "after:\t";
    std::for_each(v.cbegin(), v.cend(), print);
    std::cout << '\n';
 
    // invoke Sum::operator() for each element
    s: Sum = std::for_each(v.cbegin(), v.cend(), Sum());    
    std::cout << "sum:\t(s.sum)$\n";
}
```
{: .lh-0 }

## Output

```
before:	3 -4 2 -8 15 267 
after:	4 -3 3 -7 16 268 
sum:	281
```
{: .lh-0 }