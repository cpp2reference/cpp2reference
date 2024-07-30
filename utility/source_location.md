---
layout: page
title: std::source_location
permalink: /utility/source_location/
parent: Utility library
cppreference: /utility/source_location
---
# std::source_location

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Possible output

```
file: main.cpp2(14:25) `int main()`: Hello world!
file: main.cpp2(10:12) `void fun(const auto &) [x:auto = char[12]]`: Hello Cpp2!
```
{: .lh-0 }