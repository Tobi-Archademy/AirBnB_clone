# AirBnB clone - The console
![](abnb.png)

## About This Interpreter
This is a limited `Unix shell-like program` written in python (with the `cmd module`) for a specific use-case.

Basically it helps to manage the objects of our `AirBnB project`. These include but not limited to:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc
* Do operations on objects (count, compute stats, etc)
* Update attributes of an object
* Destroy an object

## Goal
By the end of the project, we get to know

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Navigate To
* [File Descriptions](#file-descriptions)
* [Environment](#environment)
* [Installation](#installation)
* [How To Use It](#how-to-use-it)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## File Descriptions
[console.py](console.py) - This is the entry point of the command interpreter.
The [console.py](console.py) currently supports:
* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

## Environment
This project was interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Installation
* Clone this repository: `git clone "https://github.com/Afonne-CID/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run `hbnb`:
* * Interactively: `./console` and enter <command>
* * Non-interactively: `echo "<command>" | ./console.py`

## How To Use It
```
$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$

```

## Testing :straight_ruler:

Unittests for the AirBnB project are defines in the [tests](./tests) directory. To run the entire test suits simultaneously, execute the following commands:

```
$ python3 -m unittest discover tests
```
```
$ python3 -m unittest discover tests/test_models
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 -m unittest tests/test_console.py
```

## Bugs
No known bugs at this time.

## Authors :black_nib:
Afonne-CID Paul Onyedikachi - [Github](https://github.com/Afonne-CID)
Oluwatobi Abass - [Github](https://github.com/Tobi-Archademy)


## License
Public Domain. No Copyright protection. # AirBnB_clone
