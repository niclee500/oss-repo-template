Lab 7

[create an anchor](#Checkpoint-1)

cmake-gui:

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/9d70731955920a420e9eb12bf401d0e4.png)

Build completed:

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/341be7b72c4cbaa19297bfc57b8eff11.png)

Checkpoint 2 -

1. Under either section, you can click on a build name and find out how many tests pass/fail. In the same test bucket under "View Tests summary", you can view all of the tests to see which particular tests failed. 

2. In the test for https://open.cdash.org/test/373642113 under this build: https://open.cdash.org/build/7129590, there is a CMake error in which the copyright.txt states that it is copyrighted from 2000 - 2021 but the current version year is 2021. Hence, the test failed. This can help debug the failure because it shows you which file is wrong and where you can fix it.

3. After running, only one test had failed. This was the CMake copyright test, which is similar to the error shown above. This should not be a concerning error because it is an error in a .txt file (which should not affect build too much).

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/d8e2df665aa3805cde16283d2c595e61.png)

Checkpoint 3 - 

Current CMake copyright error:

```
CMake Error at /home/jungn/git/cmake/Tests/CMakeCopyright.cmake:9 (message):
  Copyright.txt contains

   Copyright 2000-2020 Kitware, Inc. and Contributors

  but the current version year is 2021.
```
CMake failure:

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/4917bb8f3559cf4ece52094e94dcbfec.png)

Copyright.txt fix: 

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/c8143b9fc737d47ba9b6c07e54794a85.png)

Cmake run passing on Copyright.txt:

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/d5524892fae14a8f5f48645febdc4452.png)

