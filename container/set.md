---
layout: page
title: std::set
permalink: /container/set/
parent: Containers library
cppreference: /container/set
godbolt: https://cpp2.godbolt.org/z/x4qjn65xf
---
# std::set

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
LightKey: @struct type = {
    x: int;

    operator<=>: (this, that)        -> std::strong_ordering;
    operator<=>: (this, rhs: FatKey) -> std::strong_ordering = {
        return x <=> rhs.x;
    }
}

FatKey: @struct type = {
    x:    int;
    data: std::array<int, 1000> = (); // a heavy blob

    operator<=>: (this, that) -> std::strong_ordering = {
        return x <=> that.x;
    }
    operator<=>: (this, rhs: LightKey) -> std::strong_ordering = {
        return x <=> rhs.x;
    }
}

main: () = {
    // Simple comparison demo.
    example: std::set<int> = (1, 2, 3, 4);
 
    (search:= example.find(2))
    if search != example.end() {
        std::cout << "Found (search*)$\n";
    }
    else {
        std::cout << "Not found\n";
    }
 
    // Transparent comparison demo.
    example2: std::set<FatKey, std::less<>> = (
        :FatKey = (1),
        :FatKey = (2),
        :FatKey = (3),
        :FatKey = (4));
 
    (lk: LightKey = (2), search:= example2.find(lk))
    if search != example2.end() {
        std::cout << "Found (search*.x)$\n";
    }
    else {
        std::cout << "Not found\n";
    }
}
```
{: .lh-0 }

## Output

```
Found 2
Found 2
```
{: .lh-0 }
