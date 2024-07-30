---
layout: page
title: std::unordered_map
permalink: /container/unordered_map/
parent: Containers library
cppreference: /container/unordered_map
---
# std::unordered_map

{% include cppreference_link.html %}

## Example

{% include godbolt/container/unordered_map.html %}
{% include godbolt_example_link.html godbolt=url %}

```cpp
{% include src/container/unordered_map.cpp2 %}
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
