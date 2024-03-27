---
layout: page
title: std::unordered_map
permalink: /container/unordered_map/
parent: Containers library
cppreference: /container/unordered_map
godbolt: https://cpp2.godbolt.org/z/bx8b544xo
---
# std::unordered_map

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    // Create an unordered_map of three strings (that map to strings)
    u: std::unordered_map<std::string, std::string> = (
        std::make_pair("RED",   "#FF0000"),
        std::make_pair("GREEN", "#00FF00"),
        std::make_pair("BLUE",  "#0000FF")
    );
 
    // Helper lambda function to print key-value pairs
    print_key_value:= :(key, value) = {
        std::cout << "Key:[(key)$] Value:[(value)$]\n";
    };
 
    std::cout << "Iterate and print key-value pairs of unordered_map:\n";
    for u do (n) {
        print_key_value(n.first, n.second);
    }
 
    // Add two new entries to the unordered_map
    u["BLACK"] = "#000000";
    u["WHITE"] = "#FFFFFF";
 
    std::cout << "\nOutput values by key:\n"
              << "The HEX of color RED is:[" << u["RED"] << "]\n"
              << "The HEX of color BLACK is:[" << u["BLACK"] << "]\n\n";
 
    std::cout << "Use operator[] with non-existent key to insert a new key-value pair:\n";
    print_key_value("new_key", u["new_key"]);
 
    std::cout << "\nIterate and print key-value pairs;\n"
              << "new_key is now one of the keys in the map:\n";
    for u do (n) {
        print_key_value(n.first, n.second);
    }
}
```
{: .lh-0 }

## Possible output

```
Iterate and print key-value pairs of unordered_map:
Key:[BLUE] Value:[#0000FF]
Key:[GREEN] Value:[#00FF00]
Key:[RED] Value:[#FF0000]

Output values by key:
The HEX of color RED is:[#FF0000]
The HEX of color BLACK is:[#000000]

Use operator[] with non-existent key to insert a new key-value pair:
Key:[new_key] Value:[]

Iterate and print key-value pairs;
new_key is now one of the keys in the map:
Key:[new_key] Value:[]
Key:[GREEN] Value:[#00FF00]
Key:[BLACK] Value:[#000000]
Key:[BLUE] Value:[#0000FF]
Key:[WHITE] Value:[#FFFFFF]
Key:[RED] Value:[#FF0000]
```
{: .lh-0 }
