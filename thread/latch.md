---
layout: page
title: std::latch
permalink: /thread/latch/
parent: Concurrency Support library
cppreference: /thread/latch
godbolt: https://cpp2.godbolt.org/z/5KoToMb99
---
# std::latch

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
Job: @struct type = {
    name: const std::string;
    product: std::string = ("not worked");
    action: std::thread = ();
}

main: () = {
    jobs: std::array<Job, 3> = (Job("Annika"), Job("Buru"), Job("Chuck"));
 
    work_done:      std::latch = std::size(jobs);
    start_clean_up: std::latch = 1;
 
    work:= :(inout my_job: Job) = {
        my_job.product = my_job.name + " worked";
        work_done&$*.count_down();
        start_clean_up&$*.wait();
        my_job.product = my_job.name + " cleaned";
    };
 
    std::cout << "Work is starting... ";
    for jobs do (inout job)
        job.action = std::thread(work, std::ref(job));
 
    work_done.wait();
    std::cout << "done:\n";
    for jobs do (job)
        std::cout << " (job.product)$\n";
 
    std::cout << "Workers are cleaning up... ";
    start_clean_up.count_down();
    for jobs do (inout job)
        job.action.join();
 
    std::cout << "done:\n";
    for jobs do (job)
        std::cout << " (job.product)$\n";
}
```
{: .lh-0 }

## Output

```
Work is starting... done:
 Annika worked
 Buru worked
 Chuck worked
Workers are cleaning up... done:
 Annika cleaned
 Buru cleaned
 Chuck cleaned
```
{: .lh-0 }