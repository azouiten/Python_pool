# **my_minipack**

**my_minipack** is a library consisting of two functions: loading and logger.

## Installation

Use the package manager pip to install foobar.

> pip install my_minipack

## Usage:

### What is **my_minipack.ft_progress** ?

It's a function that allows you to create a progress bar, simple. You feed it an iterable object, it prints out after every iteration the progress informations and yield where it's currently at.

How to use my_minipack.ft_progress :

``` import my_minipack
 import time
 
 value = 0
 for progress in my_minipack.ft_progress(range(1337)):
     value += progress
     time.sleep(0.005)
     print(value)```

### What is **my_minipack.log** ?

**my_minipack.logger.log** is a decorator function that can be used to log every called function in a specific log file. The logged message consists of the username, function name (more or less fancier) and the time of execution.

### How to use **my_minipack.log** :

> import my_minipack
> 
> @my_minipack.log
> def some_function_1():
>     ...
> 
> @my_minipack.log
> def some_function_2():
>     ...
> 
> @my_minipack.log
> def some_function_3():
>     ...
> 
> if __name__ == "__main__":
>     some_function_1()
>     some_function_2()
>     some_function_3()
>     ...

The above code will result in a file named **actions.log** that contains something likes this:

> ...
> (azouiten)Running: Some Function 1     [ exec-time = 0.003 ms ]
> (azouiten)Running: Some Function 2     [ exec-time = 0.003 ms ]
> (azouiten)Running: Some Function 3     [ exec-time = 2.043 s ]
> ...

## License
This package is licensed under **the GNU General Public License v3 GPLv3**