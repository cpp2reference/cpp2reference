---
layout: page
title: std::copy_n
permalink: /algorithm/copy_n/
parent: Algorithms library
cppreference: /algorithm/copy_n
godbolt: https://cpp2.godbolt.org/z/Eeds7qEbT
---
# std::copy_n

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
main: () = {
    in: std::string = "1234567890";
    out: std::string = ();

    std::copy_n(in.begin(), 4, std::back_inserter(out));
    std::cout << out << '\n';

    v_in:= std::vector<int>(128);
    std::iota(v_in.begin(), v_in.end(), 1);
    v_out:= std::vector<int>(v_in.size());

    std::copy_n(v_in.cbegin(), 100, v_out.begin());
    std::cout << std::accumulate(v_out.begin(), v_out.end(), 0) << '\n';
}
```
{: .lh-0 }

## Output

```
1234
5050
```
{: .lh-0 }