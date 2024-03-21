---
layout: page
title: std::map
permalink: /container/map/
parent: Containers library
cppreference: /container/map
godbolt: https://cpp2.godbolt.org/z/hex6o5MYo
---
# std::map

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print_map: (comment: std::string_view, m: std::map<std::string, int>) = {
    std::cout << comment;
    for m do (item) {
        std::cout << "[(item.first)$] = (item.second)$; ";
    }
    std::cout << '\n';
}
 
main: () = {
    // Create a map of three (string, int) pairs
    m: std::map<std::string, int> = (
        std::make_pair("CPU", 10),
        std::make_pair("GPU", 15),
        std::make_pair("RAM", 20));

    print_map("1) Initial map: ", m);
 
    m["CPU"] = 25; // update an existing value
    m["SSD"] = 30; // insert a new value
    print_map("2) Updated map: ", m);
 
    // Using operator[] with non-existent key always performs an insert
    std::cout << "3) m[UPS] = " << m["UPS"] << '\n';
    print_map("4) Updated map: ", m);
 
    m.erase("GPU");
    print_map("5) After erase: ", m);
 
    std::erase_if(m, :(pair) pair.second > 25);
    print_map("6) After erase: ", m);
    std::cout << "7) m.size() = (m.size())$\n";
 
    m.clear();
    std::cout << "8) Map is empty: (m.empty())$\n";
}
```
{: .lh-0 }

## Output

```
1) Initial map: [CPU] = 10; [GPU] = 15; [RAM] = 20; 
2) Updated map: [CPU] = 25; [GPU] = 15; [RAM] = 20; [SSD] = 30; 
3) m[UPS] = 0
4) Updated map: [CPU] = 25; [GPU] = 15; [RAM] = 20; [SSD] = 30; [UPS] = 0; 
5) After erase: [CPU] = 25; [RAM] = 20; [SSD] = 30; [UPS] = 0; 
6) After erase: [CPU] = 25; [RAM] = 20; [UPS] = 0; 
7) m.size() = 3
8) Map is empty: true
```
{: .lh-0 }
