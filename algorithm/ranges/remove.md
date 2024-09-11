---
layout: page
title: std::ranges::remove, std::ranges::remove_if
permalink: /algorithm/ranges/remove/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/remove
---
# std::ranges::remove, std::ranges::remove_if

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
"No - Diagnostic - Required" (v1, size: 26)
"No-Diagnostic-Requiredired" (v1 after `remove`, size: 26)
 ^^^^^^^^^^^^^^^^^^^^^^
"No-Diagnostic-Required" (v1 after `erase`, size: 22)

"Substitution Failure Is Not An Error" (v2, size: 36)
"SFINAEtution Failure Is Not An Error" (v2 after `remove_if`, size: 36)
 ^^^^^^
"SFINAE" (v2 after `erase`, size: 6)

"Small Object Optimization" => SOO
"Non-Type Template Parameter" => NTTP
```
{: .lh-0 }