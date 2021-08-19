
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

![](https://user-images.githubusercontent.com/55968528/129979419-3030b334-713c-41df-9b76-eae3557af38c.PNG)

In this case, you can see that we are currently in the folder1 directory. If I type `ls` again, you can see that I have another folder:

![](https://user-images.githubusercontent.com/55968528/129979444-82601580-ec4e-4d50-98c6-44514cc5353a.PNG)

Navigating to that folder with `cd subfolder1`  we now see that **subfolder1/** is empty:

![](https://user-images.githubusercontent.com/55968528/129979427-68c37431-4c27-4dba-a1a6-260be9787547.PNG)

Now at this point, you might wonder how can we move back a directory, or all the way to our starting point ?

Well to move back to the parent directory, you can use:

```bash
  cd ..
```

As you can see, you need to add 2 dots to `cd` because 1 dot means for the current directory and 2 means the parent directory:

![](https://user-images.githubusercontent.com/55968528/129979450-c74cba75-480a-4a01-8193-0d2448071a70.PNG)

To move up 2 directories, use:

```bash
  cd ../..
```

![](https://user-images.githubusercontent.com/55968528/129979462-6174f323-4ade-4a3d-b657-a40fceb16afd.PNG)

**More on the way ...**
