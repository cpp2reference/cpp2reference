---
layout: page
title: std::map
permalink: /container/map/
parent: Containers library
cppreference: /container/map
---
# std::map

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

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
