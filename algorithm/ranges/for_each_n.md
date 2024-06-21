---
layout: page
title: std::ranges::for_each_n
permalink: /algorithm/ranges/for_each_n/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/for_each_n
godbolt: https://cpp2.godbolt.org/z/njcMq9crK
---
# std::ranges::for_each_n

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
P: @struct type = {
    first:  int  = 0;
    second: char = '\0';
    operator<<: (inout os: std::ostream, p: P) -> forward std::ostream = {
        os << '{' << p.first << ",'" << p.second << "'}";
        return os;
    }
}

print: (name: std::string_view, v) = {
    std::cout << "(name)$: ";
    (copy n:= v.ssize())
    for v do (e) {
        std::cout << e;
        n--;
        if n > 0 {
            std::cout << ", ";
        }
        else {
            std::cout << "\n";
        }
    }
}

main: () = {
    a: std::array = (1, 2, 3, 4, 5);
    print("a", a);

    // Negate first three numbers:
    std::ranges::for_each_n(a.begin(), 3, :(inout n) = n *= -1);
    print("a", a);
 
    s: std::array = (:P=(1,'a'), :P=(2, 'b'), :P=(3, 'c'), :P=(4, 'd') );
    print("s", s);

    // Negate data members 'P::first' using projection:
    std::ranges::for_each_n(s.begin(), 2, :(inout x) = x *= -1, P::first&);
    print("s", s);

    // Capitalize data members 'P::second' using projection:
    std::ranges::for_each_n(s.begin(), 3, :(inout c) = c -= 'a'-'A', P::second&);
    print("s", s);
}
```
{: .lh-0 }

## Output

```
a: 1, 2, 3, 4, 5
a: -1, -2, -3, 4, 5
s: {1,'a'}, {2,'b'}, {3,'c'}, {4,'d'}
s: {-1,'a'}, {-2,'b'}, {3,'c'}, {4,'d'}
s: {-1,'A'}, {-2,'B'}, {3,'C'}, {4,'d'}
```
{: .lh-0 }