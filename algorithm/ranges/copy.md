---
layout: page
title: std::ranges::copy, std::ranges::copy_if
permalink: /algorithm/ranges/copy/
parent: Constrained algorithms
grand_parent: Algorithms library
cppreference: /algorithm/ranges/copy
godbolt: https://cpp2.godbolt.org/z/9Wjo94Woa
---
# std::ranges::copy, std::ranges::copy_if

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    source:= std::vector<int>(10);
    std::iota(source.begin(), source.end(), 0);

    destination: std::vector<int> = ();

    std::ranges::copy(source.begin(), source.end(),
                      std::back_inserter(destination));
 
    std::cout << "destination contains: ";

    std::ranges::copy(destination, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    std::cout << "odd numbers in destination are: ";

    std::ranges::copy_if(destination, std::ostream_iterator<int>(std::cout, " "),
                         :(x: int) (x % 2) == 1);
    std::cout << '\n';
}
```
{: .lh-0 }

## Output

```
destination contains: 0 1 2 3 4 5 6 7 8 9 
odd numbers in destination are: 1 3 5 7 9 
```
{: .lh-0 }