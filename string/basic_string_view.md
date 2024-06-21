---
layout: page
title: std::basic_string_view
permalink: /string/basic_string_view/
parent: Strings library
cppreference: /string/basic_string_view
godbolt: https://cpp2.godbolt.org/z/jn5j3MEo8
---
# std::basic_string_view

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    using namespace std::literals;

    unicode: std::array = ("▀▄─"sv, "▄▀─"sv, "▀─▄"sv, "▄─▀"sv);
 
    (copy y:= 0, copy p:= 0uz)
    while y != 6 next y++ {
        (copy x:= 0)
        while x != 16 next x++ {
            std::cout << unicode[p];
        }
        std::cout << '\n';

        p = ((p + 1) % 4);
    }
}
```
{: .lh-0 }

## Output

```
▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─
▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─
▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄
▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀
▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─
▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─
```
{: .lh-0 }