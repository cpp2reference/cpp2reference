---
layout: page
title: std::atexit
permalink: /utility/program/atexit/
parent: Program support utilities
grand_parent: Utility library
cppreference: /utility/program/atexit
godbolt: https://cpp2.godbolt.org/z/89EcvGo6x
---
# std::atexit

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
atexit_handler_1: () = {
    std::cout << "At exit #1\n";
}

atexit_handler_2: () = {
    std::cout << "At exit #2\n";
}

main: () -> int = {
    result_1: const int = std::atexit(atexit_handler_1);
    result_2: const int = std::atexit(atexit_handler_2);
 
    if result_1 || result_2 {
        std::cerr << "Registration failed!\n";
        return EXIT_FAILURE;
    }
 
    std::cout << "Returning from main...\n";
    return EXIT_SUCCESS;
}
```
{: .lh-0 }

## Output

```
Returning from main...
At exit #2
At exit #1
```
{: .lh-0 }