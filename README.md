# PythonTaskManager
This is my intro to Python, its a school project :/ first time ever using python hopefully last time too.
Now it supports a consise GET/POST/PUT/DELETE API using a REST endpoing with Flask.

## About
PythonTaskManager is a command line interface that will be able to serve as a Task Manger for your daily-weekly-montly-yearly-etc tasks.
Will write to a file all the tasks for persistency and be able to add and remove tasks dynamically.

## Installation 

clone the repo
```git clone https://github.com/theargcoder/PythonTaskManager```

## Usage 

```cd /path/where/you/cloned/PythonTaskManager```
### Running testbench
```python3 -m test.test```

#### list saved events
```python3 -m src.Cli --list```

#### add event
```python3 -m src.Cli --add <DATE> <EVENT>```
example:
```python3 -m src.Cli --add 2026-02-21 Sleep```

#### mark event as completed
```python3 -m src.Cli --completed <DATE> <EVENT>```
example:
```python3 -m src.Cli --completed 2026-02-21 Sleep```

#### clear all events 
```python3 -m src.Cli --clear```
