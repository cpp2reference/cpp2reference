---
layout: page
title: std::priority_queue
permalink: /container/priority_queue/
parent: Containers library
cppreference: /container/priority_queue
godbolt: https://cpp2.godbolt.org/z/KE4EK33fq
---
# std::priority_queue

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
print_container: (name: std::string_view, cont) = {
    std::cout << "(name)$: \t";
    for cont do (n) {
        std::cout << "(n)$ ";
    }
    std::cout << '\n';
}

// C++ function template that calls Cpp2 `print_container` function
template <typename Adaptor>
    requires (std::ranges::input_range<typename Adaptor::container_type>)
void print(std::string_view name, const Adaptor& adaptor)
{
    struct Printer : Adaptor // to access protected Adaptor::Container c;
    {
        void print(std::string_view name) const { ::print_container(name, this->c); }
    };
 
    static_cast<Printer const&>(adaptor).print(name);
}

main: () = {
    data: std::vector = (1, 8, 5, 6, 3, 4, 0, 9, 7, 2);
    print_container("data", data);
 
    q1: std::priority_queue<int> = (); // Max priority queue
    for data do (n: int) {
        q1.push(n);
    }
 
    print("q1", q1);
 
    // Min priority queue
    // std::greater<int> makes the max priority queue act as a min priority queue
    minq1: std::priority_queue<int, std::vector<int>, std::greater<int>> =
        (data.begin(), data.end());
 
    print("minq1", minq1);
 
    // Second way to define a min priority queue
    minq2: std::priority_queue = (data.begin(), data.end(), std::greater<int>());
 
    print("minq2", minq2);
 
    // Using a terse, unnamed function expression (lambda) to compare elements.
    minq3: std::priority_queue = (data.begin(), data.end(), :(l, r) l > r );
 
    print("minq3", minq3);
 
    // Using a named function expression (lambda) to compare elements.
    cmp:= :(left: int, right: int) -> bool = { return (left ^ 1) < (right ^ 1); };
    q5: std::priority_queue<int, std::vector<int>, decltype(cmp)> = (cmp);
 
    for data do (n: int) {
        q5.push(n);
    }
 
    print("q5", q5);
}
```
{: .lh-0 }

## Output

```
data: 	1 8 5 6 3 4 0 9 7 2 
q1: 	9 8 5 7 3 4 0 1 6 2 
minq1: 	0 2 1 6 3 4 5 9 7 8 
minq2: 	0 2 1 6 3 4 5 9 7 8 
minq3: 	0 2 1 6 3 4 5 9 7 8 
q5: 	8 9 4 6 2 5 0 1 7 3 
```
{: .lh-0 }
