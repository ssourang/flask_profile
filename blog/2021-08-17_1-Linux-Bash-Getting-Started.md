
# Linux : Command Line Basics

If you are familiar with using Windows operating system like me, then you are probably more familiar with using your mouse to copy files, delete files ... It can be easy when dealing with just 2 or 3 files. But what if you had 1000s of files and that you wanted to delete all the files of a particular extension for instance ? Well, learning how to use the command line will allow to do just that with a simple command and much more. We will be learning about some basic commands on Linux, in order to execute certain tasks.

The first command that we are going to talk about is:

```bash
  ls 
```

It basically lists the current working directory:

![](https://user-images.githubusercontent.com/55968528/130370816-8a970b54-0f52-4480-9b43-db330ee5a4e4.png)

As you can see above, my current working directory has 2 folders and 1 **.txt** file.

Now to move into a different directory, you must use the command:

```bash
  cd
```

which stands for *change directory*:

![](https://user-images.githubusercontent.com/55968528/130370913-13bdae86-34b7-4e62-84f1-1a1cea306108.png)

In this case, you can see that we are currently in the folder1 directory. If I type `ls` again, you can see that I have another folder:

![](https://user-images.githubusercontent.com/55968528/130371037-4550bba0-7f00-4f98-b83c-559cd9faa522.png)

Navigating to that folder with `cd subfolder1`  we now see that **subfolder1/** is empty:

![](https://user-images.githubusercontent.com/55968528/130370996-9b71c811-1c42-4140-a7ed-c0cac9369724.png)

Now at this point, you might wonder how can we move back a directory, or all the way to our starting point ?

Well to move back to the parent directory, you can use:

```bash
  cd ..
```

As you can see, you need to add 2 dots to `cd` because 1 dot means for the current directory and 2 means the parent directory:

![](https://user-images.githubusercontent.com/55968528/130371091-50b7b23c-44c9-430f-86b1-06058f95f429.png)

To move up 2 directories, use:

```bash
  cd ../..
```

![](https://user-images.githubusercontent.com/55968528/130371123-d394fb91-27ad-42b3-a64b-6e3994be2dd9.png)

**More on the way ...**
