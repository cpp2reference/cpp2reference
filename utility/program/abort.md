---
layout: page
title: std::abort
permalink: /utility/program/abort/
parent: Program support utilities
grand_parent: Utility library
cppreference: /utility/program/abort
godbolt: https://cpp2.godbolt.org/z/sffa4K8no
---
# std::abort

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
Tester: type = {
    operator= :(out this)  = { std::cout << "Tester ctor\n"; }
    operator= :(move this) = { std::cout << "Tester dtor\n"; }
}

static_tester: Tester = (); // Destructor not called

signal_handler: (signal: int) = {
    if signal == SIGABRT {
        std::cout << "SIGABRT received\n";
    }
    else {
        std::cout << "Unexpected signal (signal)$ received\n";
    }
    std::cout << std::flush;
    std::_Exit(EXIT_FAILURE);
}

main: () -> int = {
    automatic_tester: Tester = (); // Destructor not called
 
    // Setup handler
    previous_handler:= std::signal(SIGABRT, signal_handler);
    if previous_handler == SIG_ERR {
        std::cerr << "Setup failed\n";
        return EXIT_FAILURE;
    }

    std::abort(); // Raise SIGABRT
    std::cout << "This code is unreachable\n";
}
```
{: .lh-0 }

## Output

```
Tester ctor
Tester ctor
SIGABRT received
```
{: .lh-0 }