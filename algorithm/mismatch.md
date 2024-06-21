---
layout: page
title: std::mismatch
permalink: /algorithm/mismatch/
parent: Algorithms library
cppreference: /algorithm/mismatch
godbolt: https://cpp2.godbolt.org/z/bTsn9fY3T
---
# std::mismatch

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
mirror_ends: (str: std::string) -> std::string = {
    return std::string(str.begin(),
                       std::mismatch(str.begin(), str.end(), str.rbegin()).first);
}

main: () = {
    std::cout << mirror_ends("abXYZba") << '\n'
              << mirror_ends("abca") << '\n'
              << mirror_ends("aba") << '\n';
}
```
{: .lh-0 }

## Output

```
ab
a
aba
```
{: .lh-0 }