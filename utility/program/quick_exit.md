---
layout: page
title: std::quick_exit
permalink: /utility/program/quick_exit/
parent: Program support utilities
grand_parent: Utility library
cppreference: /utility/program/quick_exit
godbolt: https://cpp2.godbolt.org/z/8qsP8MqET
---
# std::quick_exit

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
quick_exit_handler: <N: int>() = {
    std::cout << "quick_exit handler #(N)$" << std::endl; // flush is intended
}

at_exit_handler: () = {
    std::cout << "at_exit handler\n";
}

R: type = {
    operator=: (move this) = {
        std::cout << "destructor\n";
    }
}

main: () -> int = {
    if std::at_quick_exit(quick_exit_handler<1>) ||
       std::at_quick_exit(quick_exit_handler<2>)
    {
        std::cerr << "Registration failed\n";
        return EXIT_FAILURE;
    }
 
    std::atexit(at_exit_handler); // the handler will not be called
 
    resource: R = ();             // the destructor will not be called

    std::quick_exit(EXIT_SUCCESS);
 
    std::cout << "This statement is unreachable...\n";
}
```
{: .lh-0 }

## Output

```
quick_exit handler #2
quick_exit handler #1
```
{: .lh-0 }