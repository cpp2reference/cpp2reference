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
| Language support library | Memory management library | [Concurrency support library](/thread/index.md){: .fs-5 } |
|  |  | [thread](/thread/thread.md){: .m-0 .p-0 .pl-4 } - [jthread](/thread/jthread.md){: .m-0 .p-0 } |
|  |  | [Mutual exclusion](/thread/index.md#mutex){: .m-0 .p-0 .pl-4 } |
|  |  | [Condition variables](/thread/index.md#condition-variables){: .m-0 .p-0 .pl-4 } - [Futures](/thread/index.md#futures){: .m-0 .p-0 } |