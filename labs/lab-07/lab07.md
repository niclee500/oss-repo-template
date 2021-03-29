Lab 7

Checkpoint 1 - 

cmake-gui:

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/9d70731955920a420e9eb12bf401d0e4.png)

Build completed:

![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/341be7b72c4cbaa19297bfc57b8eff11.png)

Checkpoint 2 -

1. Under either section, you can click on a build name and find out how many tests pass/fail. In the same test bucket under "View Tests summary", you can view all of the tests to see which particular tests failed. 

2. In the test for https://open.cdash.org/test/373642113 under this build: https://open.cdash.org/build/7129590, there is a CMake error in which the copyright.txt states that it is copyrighted from 2000 - 2021 but the current version year is 2021. Hence, the test failed. This can help debug the failure because it shows you which file is wrong and where you can fix it.


![alt text](https://github.com/niclee500/oss-repo-template/blob/master/labs/lab-07/d8e2df665aa3805cde16283d2c595e61.png)

