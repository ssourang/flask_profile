
# Linux : Command Line Basics

If you are familiar with using Windows operating system like me, then you are probably more familiar with using your mouse to copy files, delete files ... It can be easy when dealing with just 2 or 3 files. But what if you had 1000s of files and that you wanted to delete all the files of a particular extension for instance ? Well, learning how to use the command line will allow to do just that with a simple command and much more. We will be learning about some basic commands on Linux, in order to execute certain tasks.

The first command that we are going to talk about is:

```bash
  ls 
```

It basically lists the current working directory:

![](https://user-images.githubusercontent.com/55968528/129979403-e2a9d69e-d46e-4310-89ee-850fd7927f97.png)

As you can see above, my current working directory has 2 folders and 1 **.txt** file.

Now to move into a different directory, you must use the command:

```bash
  cd
```

which stands for *change directory*:

![](https://user-images.githubusercontent.com/55968528/130364976-41f12944-8ba9-4479-8ec5-bcbd6df745b5.png)

In this case, you can see that we are currently in the folder1 directory. If I type `ls` again, you can see that I have another folder:

![](https://user-images.githubusercontent.com/55968528/130364431-11cf06dd-7dcd-40a4-9c2a-870f43a82d87.png)

Navigating to that folder with `cd subfolder1`  we now see that **subfolder1/** is empty:

![](https://user-images.githubusercontent.com/55968528/130364366-c8d5465b-8029-44d2-92e5-531873e2a709.png)

Now at this point, you might wonder how can we move back a directory, or all the way to our starting point ?

Well to move back to the parent directory, you can use:

```bash
  cd ..
```

As you can see, you need to add 2 dots to `cd` because 1 dot means for the current directory and 2 means the parent directory:

![](https://user-images.githubusercontent.com/55968528/130364839-e2ea8e2e-7aed-4b44-ba0b-648a82a6ba15.png)

To move up 2 directories, use:

```bash
  cd ../..
```

![](https://user-images.githubusercontent.com/55968528/130364900-4e2cacc2-5363-4351-8f2f-0652249e6385.png)

**More on the way ...**
