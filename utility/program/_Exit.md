---
layout: page
title: std::_Exit
permalink: /utility/program/_Exit/
parent: Program support utilities
grand_parent: Utility library
cppreference: /utility/program/_Exit
godbolt: https://cpp2.godbolt.org/z/W9E6Mq7o4
---
# std::_Exit

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
Static: type = {
    operator=: (move this) = {
        std::cout << "Static dtor\n";
    }
}

Local: type = {
    operator=: (move this) = {
        std::cout << "Local dtor\n";
    }
}

static_variable: Static = (); // dtor of this object will *not* be called

atexit_handler: () = {
    std::cout << "atexit handler\n";
}

main: () -> int = {
    local_variable: Local = (); // dtor of this object will *not* be called
 
    // handler will *not* be called
    result:= std::atexit(atexit_handler);
 
    if result != 0 {
        std::cerr << "atexit registration failed\n";
        return EXIT_FAILURE;
    }
 
    std::cout << "test" << std::endl; // flush from std::endl
        // needs to be here, otherwise nothing will be printed
    std::_Exit(EXIT_FAILURE);
}
```
{: .lh-0 }

## Output

```
test
```
{: .lh-0 }