---
layout: page
title: std::unordered_multimap
permalink: /container/unordered_multimap/
parent: Containers library
cppreference: /container/unordered_multimap
godbolt: https://cpp2.godbolt.org/z/93PdzE8d4
---
# std::unordered_multimap

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print: (comment: std::string_view, data) = {
    std::cout << comment;
    for data do (pair) {
        std::cout << " (pair.first)$((pair.second)$)";
    }
    std::cout << '\n';
}

main: () = {
    cont: std::unordered_multimap<int, char> = (
        std::make_pair(1, 'a'),
        std::make_pair(2, 'b'),
        std::make_pair(3, 'c'),
    );
 
    print("Start:", cont);
 
    // Extract node handle and change key
    nh:= cont.extract(1);
    nh.key() = 4;
 
    print("After extract and before insert:", cont);
 
    // Insert node handle back
    cont.insert(move nh);
 
    print("End:", cont);
}
```
{: .lh-0 }

## Possible output

```
Start: 3(c) 2(b) 1(a)
After extract and before insert: 3(c) 2(b)
End: 4(a) 3(c) 2(b)
```
{: .lh-0 }
