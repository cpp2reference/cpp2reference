---
layout: page
title: std::exit
permalink: /utility/program/exit/
parent: Program support utilities
grand_parent: Utility library
cppreference: /utility/program/exit
godbolt: https://cpp2.godbolt.org/z/ve97hT1rP
---
# std::exit

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
Static: type = {
    operator=: (move this) = {
        std::cout << "Static destructor\n";
    }
}

Local: type = {
    operator=: (move this) = {
        std::cout << "Local destructor\n";
    }
}

Static static_variable; // Destructor of this object *will* be called

atexit_handler: () = {
    std::cout << "atexit handler\n";
}

main: () -> int = {
    local_variable: Local = ();           // Destructor will *not* be called
    result:= std::atexit(atexit_handler); // Handler will be called
 
    if result != 0 {
        std::cerr << "atexit registration failed\n";
        return EXIT_FAILURE;
    }
 
    std::cout << "test\n";
    std::exit(EXIT_FAILURE);
 
    std::cout << "this line will *not* be executed\n";
}
```
{: .lh-0 }

## Output

```
test
atexit handler
Static destructor
```
{: .lh-0 }