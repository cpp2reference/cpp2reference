---
layout: page
title: std::basic_string
permalink: /string/basic_string/
parent: Strings library
cppreference: /string/basic_string
godbolt: https://cpp2.godbolt.org/z/qvYTv1ahG
---
# std::basic_string

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    using namespace std::literals;
 
    // Creating a string from const char*
    str1: std::string = "hello";
 
    // Creating a string using string literal
    str2:= "world"s;
 
    // Concatenating strings
    str3: std::string = str1 + " " + str2;
 
    // Print out the result
    std::cout << str3 << '\n';
 
    pos:= str3.find(" ");
    str1 = str3.substr(pos + 1u); // the part after the space
    str2 = str3.substr(0u, pos);  // the part till the space
 
    std::cout << "(str1)$ (str2)$\n";
 
    // Accessing an element using subscript operator[]
    std::cout << str1[0] << '\n';
    str1[0] = 'W';
    std::cout << str1 << '\n';
}
```
{: .lh-0 }

## Output

```
hello world
world hello
w
World
```
{: .lh-0 }