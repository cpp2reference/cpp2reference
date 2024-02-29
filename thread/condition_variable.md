---
layout: page
title: std::condition_variable
permalink: /thread/condition_variable/
parent: Concurrency Support Library
---
# std::condition_variable

[cppreference.com](https://en.cppreference.com/w/cpp/thread/condition_variable)

## Example

[Run on Compiler Explorer](https://cpp2.godbolt.org/z/q3W6oYMWh)

```cpp
m: std::mutex = ();
cv: std::condition_variable = ();
data: std::string = ();
ready: bool = false;
processed : bool = false;

worker: () = {
    (copy lk: std::unique_lock = (m))
    {
        cv.wait(lk, :() -> bool = ready);

        std::cout << "Worker is processing data\n";
        data += " after processing";

        processed = true;
        std::cout << "Worker thread signals data processing completed\n";

        _ = lk.mutex();  // Temp workaround for cppfront bug
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

        _ = lk.mutex();  // Temp workaround for cppfront bug
    }

    std::cout << "Back in main(), data = " << data << '\n';

    worker_thd.join();

    _ = m.native_handle();  // Temp workaround for cppfront bug
    _ = cv.native_handle();  // Temp workaround for cppfront bug

    return 0;
}
```

## Output

```
main() signals data ready for processing
Worker is processing data
Worker thread signals data processing completed
Back in main(), data = Example data after processing
```