---
layout: page
title: std::move_backward
permalink: /algorithm/move_backward/
parent: Algorithms library
cppreference: /algorithm/move_backward
godbolt: https://cpp2.godbolt.org/z/v5bjs3aGh
---
# std::move_backward

{% include cppreference_link.html %}

## Example

{% include godbolt_example_link.html %}

```cpp
container: type == std::vector<std::string>;

print: (comment: std::string_view, src: container) = {
    print(comment, src, ());
}

print: (comment: std::string_view, src: container, dst: container) = {
    prn:= :(name: std::string_view, cont: container) = {
        std::cout << name;
        for cont do (s) {
            if s.empty() {
                std::cout << "∙ ";
            }
            else {
                std::cout << s.data() << " ";
            }
        }
        std::cout << '\n';
    };
    std::cout << comment << '\n';
    prn("src: ", src);
    if dst.empty() {
        return;
    }
    prn("dst: ", dst);
}

main: () = {
    src: container = ("foo", "bar", "baz");
    dst: container = ("qux", "quux", "quuz", "corge");
    print("Non-overlapping case; before move_backward:", src, dst);
    std::move_backward(src.begin(), src.end(), dst.end());
    print("After:", src, dst);

    src = ("snap", "crackle", "pop", "lock", "drop");
    print("Overlapping case; before move_backward:", src);
    std::move_backward(src.begin(), std::next(src.begin(), 3), src.end());
    print("After:", src);
}
```
{: .lh-0 }

## Output

```
Non-overlapping case; before move_backward:
src: foo bar baz 
dst: qux quux quuz corge 
After:
src: ∙ ∙ ∙ 
dst: qux foo bar baz 
Overlapping case; before move_backward:
src: snap crackle pop lock drop 
After:
src: ∙ ∙ snap crackle pop 
```
{: .lh-0 }