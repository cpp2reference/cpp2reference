---
layout: page
title: std::find_first_of
permalink: /algorithm/find_first_of/
parent: Algorithms library
cppreference: /algorithm/find_first_of
godbolt: https://cpp2.godbolt.org/z/56nWfr4Mc
---
# std::find_first_of

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print_sequence: (id: std::string_view, seq) = {
    print_sequence(id, seq, -1);
}

print_sequence: <T>(id: std::string_view, seq, pos: T) = {
    std::cout << "(id)${ ";
    (copy i: T = 0)
    for seq do (e) {
        mark:= i == pos;
        if i {
            std::cout << ", ";
        }
        i++;
        if mark {
            std::cout << "[ ";
        }
        std::cout << e;
        if mark {
            std::cout << " ]";
        }
    }
    std::cout << " }\n";
}

main: () = {
    v:  std::vector = (0, 2, 3, 25, 5);
    t1: std::array  = (19, 10, 3, 4);
    t2: std::array  = (1, 6, 7, 9);

    find_any_of:= :(v, t) = {
        result:= std::find_first_of(v.begin(), v.end(),
                                    t.begin(), t.end());
        if result == v.end() {
            std::cout << "No elements of v are equal to any element of ";
            print_sequence("t = ", t);
            print_sequence("v = ", v);
        }
        else {
            pos:= std::distance(v.begin(), result);
            std::cout << "Found a match ((result*)$) at position (pos)$";
            print_sequence(", where t = ", t);
            print_sequence("v = ", v, pos);
        }
    };

    find_any_of(v, t1);
    find_any_of(v, t2);
}
```
{: .lh-0 }

## Output

```
Found a match (3) at position 2, where t = { 19, 10, 3, 4 }
v = { 0, 2, [ 3 ], 25, 5 }
No elements of v are equal to any element of t = { 1, 6, 7, 9 }
v = { 0, 2, 3, 25, 5 }
```
{: .lh-0 }
