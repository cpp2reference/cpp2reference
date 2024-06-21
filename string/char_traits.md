---
layout: page
title: std::char_traits
permalink: /string/char_traits/
parent: Strings library
cppreference: /string/char_traits
godbolt: https://cpp2.godbolt.org/z/rnhWGbGvh
---
# std::char_traits

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
ci_char_traits: type = {
    this: std::char_traits<char>;

    to_upper: (ch: char) -> char = {
        return cpp2::unsafe_narrow<char>(std::toupper(ch as int));
    }

    eq: (c1: char, c2: char) -> bool = {
        return to_upper(c1) == to_upper(c2);
    }

    lt: (c1: char, c2: char) -> bool = {
         return to_upper(c1) < to_upper(c2);
    }

    compare: (s1: *const char, s2: *const char, n: std::size_t) -> int = {
        (sv1: std::string_view = s1,
         sv2: std::string_view = s2,
         copy i: std::size_t = 0)
        while i < n next i++ {
            if to_upper(sv1[i]) < to_upper(sv2[i]) {
                return -1;
            }
            if to_upper(sv1[i]) > to_upper(sv2[i]) {
                return 1;
            }
        }
        return 0;
    }

    find: (s: *const char, n: std::size_t, a: char) -> *const char = {
        (sv: std::string_view = s,
         ua:= to_upper(a),
         copy i: std::size_t = 0)
        while i < n next i++ {
            if to_upper(sv[i]) == ua {
                std::advance(s, i);
                return s;
            }
        }
        return nullptr;
    }
}

traits_cast: <DstTraits, CharT, SrcTraits>
    (src: std::basic_string_view<CharT, SrcTraits>)
    -> std::basic_string_view<CharT, DstTraits>
== {
    return (src.data(), src.size());
}

main: () = {
    using namespace std::literals;
 
    s1: == "Hello"sv;
    s2: == "heLLo"sv;
 
    if traits_cast<ci_char_traits>(s1) == traits_cast<ci_char_traits>(s2) {
        std::cout << "(s1)$ and (s2)$ are equal\n";
    }
}
```
{: .lh-0 }

## Output

```
Hello and heLLo are equal
```
{: .lh-0 }