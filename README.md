# csort
Sort columns of a text file.

```
$ cat a.txt
USER_ID NAME    AGE
1       Sato    10
2       Suzuki  30
3       Abe     20
$ cat a.txt | csort -f 2,3
NAME    AGE
Sato    10
Suzuki  30
Abe     20
$ csort -f 2,3 a.txt
NAME    AGE
Sato    10
Suzuki  30
```

# install

```
$ pip install csort
```
