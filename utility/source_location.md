---
layout: page
title: std::source_location
permalink: /utility/source_location/
parent: Utility library
cppreference: /utility/source_location
---
# std::source_location

{% include cppreference_link.html %}

## Example

<div class="code-example" markdown="1">
[Run on Compiler Explorer](https://cpp2.godbolt.org/z/fvrjcandc){: .btn }{:target="_blank"}
</div>
{: .m-0 .p-2 }

```cpp
log: (message: std::string_view, location: std::source_location) = {
    file_name:= location.file_name();
    line:=      location.line();
    col:=       location.column();
    func:=      location.function_name();
    std::clog << "file: (file_name)$((line)$:(col)$) `(func)$`: (message)$\n";
}
 
fun: (x) = {
    log(x, std::source_location::current());
}
 
main: () = {
    log("Hello world!", std::source_location::current());
    fun("Hello Cpp2!");
}
```
{: .lh-0 }

## Possible output

```
file: main.cpp2(14:25) `int main()`: Hello world!
file: main.cpp2(10:12) `void fun(const auto &) [x:auto = char[12]]`: Hello Cpp2!
```
{: .lh-0 }