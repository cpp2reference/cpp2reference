---
layout: page
title: std::condition_variable
permalink: /thread/condition_variable/
parent: Concurrency Support library
cppreference: /thread/condition_variable
---

# std::condition_variable

{% include cppreference_link.html %}

## Example

{% include cpp2_example.html %}

## Output

```
main() signals data ready for processing
Worker is processing data
Worker thread signals data processing completed
Back in main(), data = Example data after processing
```
{: .lh-0 }