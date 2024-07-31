---
layout: page
title: std::move_backward
permalink: /algorithm/move_backward/
parent: Algorithms library
cppreference: /algorithm/move_backward
---
# std::move_backward

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
Non-overlapping case; before move_backward:
src: foo bar baz 
dst: qux quux quuz corge 
After:
src: ∙ ∙ ∙ 
dst: qux foo bar baz 
Overlapping case; before move_backward:
src: snap crackle pop lock drop 
After:
src: ∙ ∙ snap crackle pop 
```
{: .lh-0 }