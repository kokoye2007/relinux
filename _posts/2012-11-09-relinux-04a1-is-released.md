---
layout: post
title: Relinux 0.4a1 is released!
author: MiJyn
root: ../../../
---
After about a year of writing, rewriting, and rebasing, relinux 0.4a1 has finally been released!
Here are a few of the new features in relinux 0.4:

 * Qt user interface
 * Thread-based, so multiple operations can run at the same time
 * Logging, so if there are any problems while relinux runs, you can easily diagnose it
 * ISO level support, so that your compressed filesystem can exceed 4GB (if needed, of course)
 * Module API, so that you can automate common tasks in making your distro

Relinux is also finally packaged in the .deb format, plus it has it's own PPA!
This means that you can just add the PPA and install :D

To install using the PPA:

    sudo add-apt-repository ppa:relinux-dev/testing
    sudo apt-get update
    sudo apt-get install relinux

Or follow a slightly better installation guide here: [https://github.com/MiJyn/relinux/wiki/Installing](https://github.com/MiJyn/relinux/wiki/Installing)

Relinux 0.4 has also been re-licensed to LGPL, so that people can now make paid distros using relinux (legally).

-- Joel Leclerc (MiJyn)
