---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Home
permalink: /
nav_order: 1
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
</style>
| [Language support library](/utility/index.md#language-support){: .fs-5 } | [Containers library](/container/index.md){: .fs-5 } | [Concurrency support library](/thread/index.md){: .fs-5 } |
| [source_location](/utility/source_location.md){: .m-0 .p-0 .pl-4 } | [vector](/container/vector.md){: .m-0 .p-0 .pl-4 } - [deque](/container/deque.md){: .m-0 .p-0 } - [array](/container/array.md){: .m-0 .p-0 } | [thread](/thread/thread.md){: .m-0 .p-0 .pl-4 } - [jthread](/thread/jthread.md){: .m-0 .p-0 } |
|  | [list](/container/list.md){: .m-0 .p-0 .pl-4 } - [forward_list](/container/forward_list.md){: .m-0 .p-0 } | [atomic](/atomic/atomic.md){: .m-0 .p-0 .pl-4 } - [atomic_flag](/atomic/atomic_flag.md){: .m-0 .p-0 } |
|  | [map](/container/map.md){: .m-0 .p-0 .pl-4 } - [multimap](/container/multimap.md){: .m-0 .p-0 } - [set](/container/set.md){: .m-0 .p-0 } - [multiset](/container/multiset.md){: .m-0 .p-0 } | [Mutual exclusion](/thread/index.md#mutex){: .m-0 .p-0 .pl-4 } - [Semaphores](/thread/index.md#semaphores){: .m-0 .p-0 } |
|  | [unordered_map](/container/unordered_map.md){: .m-0 .p-0 .pl-4 } | [Condition variables](/thread/index.md#condition-variables){: .m-0 .p-0 .pl-4 } - [Futures](/thread/index.md#futures){: .m-0 .p-0 } |
|  | [unordered_multimap](/container/unordered_multimap.md){: .m-0 .p-0 .pl-4 } | [latch](/thread/latch.md){: .m-0 .p-0 .pl-4 } - [barrier](/thread/barrier.md){: .m-0 .p-0 } |
|  | [unordered_set](/container/unordered_set.md){: .m-0 .p-0 .pl-4 } | |