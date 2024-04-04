---
layout: page
title: std::unordered_multiset
permalink: /container/unordered_multiset/
parent: Containers library
cppreference: /container/unordered_multiset
godbolt: https://cpp2.godbolt.org/z/PzjhP7bh4
---
# std::unordered_multiset

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    sentence: const std::string = "cpp2reference.com";
    std::cout << "The sentence: (sentence)$\n";
 
    sequence: std::unordered_multiset<char> = ();
    for sentence do (ch: char) {
        sequence.insert(ch);
    }
 
    std::cout << "The sequence: { ";
    for sequence do (ch: char) {
        std::cout << "(ch)$ ";
    }
 
    std::cout << "}\nSymbol:Frequency: ";
    (copy it:= sequence.begin())
    while it != sequence.end() {
        (range:= sequence.equal_range(it*))
        if range.first != range.second {
            symbol:= range.first*;
            frequency:= std::distance(range.first, range.second);
            std::cout << "(symbol)$:(frequency)$  ";
            it = range.second;
        }
        else {
            it++;
        }
    }
}
```
{: .lh-0 }

## Possible output

```
The sentence: cpp2reference.com
The sequence: { m o . f 2 p p e e e e c c c n r r }
Symbol:Frequency: m:1  o:1  .:1  f:1  2:1  p:2  e:4  c:3  n:1  r:2  
```
{: .lh-0 }
