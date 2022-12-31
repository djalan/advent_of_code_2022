# Advent of Code 2022

## Day 03
### zip
- combine multiple lists
- it is also possible to unzip
```python
# key: value
dict(zip(list1, list2))

# set of tuples
set(zip(list1, list2))

# list of tuples
list(zip(list1, list2))

# iteration with count/index
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
    # 0 Jesus 33

# iteration
for (name, age) in zip(names, ages)):
    print(name, age)
    # Jesus 33
```
### divide
```python
5 / 2  # 2.5
5 // 2 # 2
```
### islice
Read multiple lines at a time
```python
from itertools import islice

with open('input.txt') as file:
   while True:
       group_lines = list(islice(file, 3))  # 3 lines at a time
       if not group_lines:
           break
```
### intersection
#### intersection of 2 sets
`result = set1 & set2`
#### intersection of 3 sets
`result = set1.intersection(set2, set3)`


## Day 05
### readlines(): put all the lines of a file in a list
```python
lines = file.readlines()
crates = lines[:8]
moves = lines[10:]
```
### reverse a list
- reverse the current list: `my_list.reverse()`
- reverse for iteration: `for elem in reversed(my_list)`


## Day 06
### Create an empty set
```python
my_set = set()
my_list = []
my_dict = {}
```


## Day 07
### PurePath(): path that might not exist on a filesystem
- useful to call path functions such as:
    - parent
    - parents
    - basename
    - extension
    - longer_path = path / new_dir
- `sorted` a list
    - `result = sorted(list)[0]`


## Day 08
### Part 1
#### why not 2d list
- can't make slices vertically
#### why not matrix
- matrix is a subclass of ndarray
- don't need matrix for [m,n] access of elements
#### why not np.ndarray
- np.array is the preferred method to create an ndarray
- `np.array`
- `np.empty`
- `np.zeros`
#### logging warning
- do not use fstring, use %s formatting to use optimization in logging library


## Day09
### Part 1
#### problem initiating list of tuples, hashing error
```python
visited = [tuple([0,0])]
```

### Part 2
skip: need to find/guess what the correct algorithm
