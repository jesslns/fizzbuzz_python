## FizzBuzz TDD with Python

### Objectives
Complete FizzBuzz kata using a new language using the TDD approach. <br>
In this exercise, FizzBuzz is written in Python and tested using pytest.

#### Setting Up in Mac OS

- Install python with the syntax `brew install python3`.

- To check the file pathway of python3, type `which python3` in the terminal.

- Type `python --version` to check which python version was installed.

- If you have python2 on your machine and want to change your default version to python3, add python3 pathway to your bash_profile:
```
$ which python
/usr/local/bin/python3
```
```
$ vi ~/.bash_profile  
alias python='/usr/local/bin/python3'
```
and reopen terminal.

- Next, install pip
```
$ sudo easy_install pip
$ sudo pip install --upgrade pip
```
- Then, install pytest with `brew install pytest`.

- If you have python2 on your machine, pytest may want to be installed within python2 by default. In this case, you need to force pytest to installed in python 3. Since python3.7.2 was installed, the syntax is:
```
$ pip3.7 install pytest
```
