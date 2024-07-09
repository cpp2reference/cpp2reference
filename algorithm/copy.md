---
layout: page
title: std::copy, std::copy_if
permalink: /algorithm/copy/
parent: Algorithms library
cppreference: /algorithm/copy
godbolt: https://cpp2.godbolt.org/z/sfP1xqaK3
---
# std::copy, std::copy_if

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    from_vector:= std::vector<int>(10);
    std::iota(from_vector.begin(), from_vector.end(), 0);

    to_vector: std::vector<int> = ();
    std::copy(from_vector.begin(), from_vector.end(),
              std::back_inserter(to_vector));

    std::cout << "to_vector contains: ";

    std::copy(to_vector.begin(), to_vector.end(),
              std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    std::cout << "odd numbers in to_vector are: ";

    std::copy_if(to_vector.begin(), to_vector.end(),
                 std::ostream_iterator<int>(std::cout, " "),
                 :(x: int) x % 2 != 0);
    std::cout << '\n';

    std::cout << "to_vector contains these multiples of 3: ";

    to_vector.clear();
    std::copy_if(from_vector.begin(), from_vector.end(),
                 std::back_inserter(to_vector),
                 :(x: int) x % 3 == 0);

    for to_vector do (x: int) {
        std::cout << x << ' ';
    }
    std::cout << '\n';
}
```
{: .lh-0 }

## Output

```
to_vector contains: 0 1 2 3 4 5 6 7 8 9 
odd numbers in to_vector are: 1 3 5 7 9 
to_vector contains these multiples of 3: 0 3 6 9 
```
{: .lh-0 }