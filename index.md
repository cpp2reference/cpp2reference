---
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Home
permalink: /
nav_order: 1

cppf_home: https://hsutter.github.io/cppfront/
cppf_common: https://hsutter.github.io/cppfront/cpp2/common/
cppf_expr: https://hsutter.github.io/cppfront/cpp2/expressions/
cppf_decl: https://hsutter.github.io/cppfront/cpp2/declarations/
cppf_obj: https://hsutter.github.io/cppfront/cpp2/objects/
cppf_fun: https://hsutter.github.io/cppfront/cpp2/functions/
cppf_cont: https://hsutter.github.io/cppfront/cpp2/contracts/
cppf_type: https://hsutter.github.io/cppfront/cpp2/types/
---
A [Cpp2](https://github.com/hsutter/cppfront/) online reference for the C++ Standard Library.

Code samples are copied from the excellent [cppreference.com](https://cppreference.com) (under their permissive license) and translated into Cpp2.

{: .note }
This is a work in progress.

<style>
table {
    border-collapse: collapse;
}
table, th, td {
   border: none;
   padding: 0px;
   padding-left: 8px;
   padding-right: 8px;
   border-spacing: none;
}
td {
    background-color: #FAFAFA;
}
</style>
| [Language]({{ page.cppf_home }}){: .fs-5 }                               |                                                                            | [Iterators library](/iterator/index.md){: .fs-5 }   |
| [Common Concepts]({{ page.cppf_common }}){: .m-0 .p-0 .pl-4 }            |                                                                            | [Ranges library](/ranges/index.md){: .fs-5 }        |
| [Expressions]({{ page.cppf_expr }}){: .m-0 .p-0 .pl-4 } - [Declarations]({{ page.cppf_decl }}){: .m-0 .p-0 } | [Strings library](/string/index.md){: .fs-5 }                              | [Algorithms library](/algorithm/index.md){: .fs-5 } |
| [Objects]({{ page.cppf_obj }}){: .m-0 .p-0 .pl-4 } - [Functions]({{ page.cppf_fun }}){: .m-0 .p-0 }          | [basic_string](/string/basic_string.md){: .m-0 .p-0 .pl-4 } - [char_traits](/string/char_traits.md){: .m-0 .p-0 }               | [Constrained algorithms](/algorithm/ranges/index.md){: .m-0 .p-0 .pl-4 } |
| [Contracts]({{ page.cppf_cont }}){: .m-0 .p-0 .pl-4 } - [Types]({{ page.cppf_type }}){: .m-0 .p-0 }          | [basic_string_view](/string/basic_string_view.md){: .m-0 .p-0 .pl-4 }      |  |
| [Language support library](/utility/index.md#language-support){: .fs-5 } | [Containers library](/container/index.md){: .fs-5 }                        | [Concurrency support library](/thread/index.md){: .fs-5 } |
| [Program utilities](/utility/program/index.md){: .m-0 .p-0 .pl-4 }       | [vector](/container/vector.md){: .m-0 .p-0 .pl-4 } - [deque](/container/deque.md){: .m-0 .p-0 } - [array](/container/array.md){: .m-0 .p-0 } | [thread](/thread/thread.md){: .m-0 .p-0 .pl-4 } - [jthread](/thread/jthread.md){: .m-0 .p-0 } |
| [source_location](/utility/source_location.md){: .m-0 .p-0 .pl-4 }       | [list](/container/list.md){: .m-0 .p-0 .pl-4 } - [forward_list](/container/forward_list.md){: .m-0 .p-0 } | [atomic](/atomic/atomic.md){: .m-0 .p-0 .pl-4 } - [atomic_flag](/atomic/atomic_flag.md){: .m-0 .p-0 } |
|                                                                          | [map](/container/map.md){: .m-0 .p-0 .pl-4 } - [multimap](/container/multimap.md){: .m-0 .p-0 } - [set](/container/set.md){: .m-0 .p-0 } - [multiset](/container/multiset.md){: .m-0 .p-0 } | [Mutual exclusion](/thread/index.md#mutex){: .m-0 .p-0 .pl-4 } - [Semaphores](/thread/index.md#semaphores){: .m-0 .p-0 } |
|                                                                          | [unordered_map](/container/unordered_map.md){: .m-0 .p-0 .pl-4 }           | [Condition variables](/thread/index.md#condition-variables){: .m-0 .p-0 .pl-4 } - [Futures](/thread/index.md#futures){: .m-0 .p-0 } |
|                                                                          | [unordered_multimap](/container/unordered_multimap.md){: .m-0 .p-0 .pl-4 } | [latch](/thread/latch.md){: .m-0 .p-0 .pl-4 } - [barrier](/thread/barrier.md){: .m-0 .p-0 } |
|                                                                          | [unordered_set](/container/unordered_set.md){: .m-0 .p-0 .pl-4 }           |  |
|                                                                          | [unordered_multiset](/container/unordered_multiset.md){: .m-0 .p-0 .pl-4 } |  |
|                                                                          | [Container adaptors](/container/index.md#adaptors){: .m-0 .p-0 .pl-4 }     |  |
|                                                                          | [span](/container/span.md){: .m-0 .p-0 .pl-4 } - [mdspan](/container/mdspan.md){: .m-0 .p-0 } |  |
