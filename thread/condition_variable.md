---
layout: page
title: std::condition_variable
permalink: /thread/condition_variable/
parent: Concurrency Support Library
cppreference: /thread/condition_variable
godbolt: https://cpp2.godbolt.org/z/W5h4zozhW
---

# std::condition_variable

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
m:         std::mutex = ();
cv:        std::condition_variable = ();
data:      std::string = ();
ready:     bool = false;
processed: bool = false;

worker: () = {
    (copy lk: std::unique_lock = (m))
    {
        cv.wait(lk, :() -> bool = ready);

        std::cout << "Worker is processing data\n";
        data += " after processing";

        processed = true;
        std::cout << "Worker thread signals data processing completed\n";
    }
    cv.notify_one();
}

main: () -> int = {
    worker_thd: std::thread = (worker);

    data = "Example data";

    (copy _: std::lock_guard = (m))
    {
        ready = true;
        std::cout << "main() signals data ready for processing\n";
    }
    cv.notify_one();

    (copy lk: std::unique_lock = (m))
    {
        cv.wait(lk, :() -> bool = processed);
    }

    std::cout << "Back in main(), data = " << data << '\n';

    worker_thd.join();

    return 0;
}
```
{: .lh-0 }

## Output

```
main() signals data ready for processing
Worker is processing data
Worker thread signals data processing completed
Back in main(), data = Example data after processing
```
{: .lh-0 }