## ALX AirBnB Project

### ALX AirBnB clone project
In this project, we implement the following:
- `BaseModel` class for instantation of AirBnB clone objects
- `User`, `State`, `City`, `Place`, `Amenity`, `Review` subclasses that inherit from `BaseModel`
- Serialization/deserialization of instances
- A storage engine for the project: `FileStorage`
- A console/command interpreter where we can instantiate, store, destroy, and update attributes of objects, as well as print out the string representation of those objects

### BaseModel Class & Subclass Instance Attributes and Methods
Each instance of all classes that inherit from BaseModel will be instantiated with the following attributes:
- id: UUID generated string
- created_at: datetime object reflecting when the instance was created
- updated_at: datetime object reflecting when the instance was updated

Methods:
- `__str__`: Overrides the default `__str__` method to print `[<class name>] (<self.id>) <self.__dict__>`
- `save(self)`: Updates `updated_at` with the current datetime
- `to_dict(self)`: Returns a dictionary containing all keys/value of the instance's `__dict__`

### FileStorage 
FileStorage has the following private class attributes:
- `__file_path`: string, path to JSON file (in our case, it is `file.json`)
- `__objects`: dictionary, stores all instances with the key `<class name>.id`

Methods:
- `all(self)`: Returns `__objects` dictionary
- `new(self, obj)`: Adds the new object to the `__objects` dictionary with `<class name>.id` key
- `save(self)`: Serializes `__objects` into the JSON file contained in `__file_path`
- `reload(self)`: Deserializes JSON file contained in `__file_path` to `__objects`. If the file does not exist, nothing will happen.

### Command Interpreter/Console
The code for the command interpreter is in `console.py`.

To start the console, type `./console.py` or `python3 console.py` in the directory `console.py` is in. This will make the command prompt `(hbnb)` appear on your terminal.

```
$ ./console.py
(hbnb) 
```

### Usage
The console accepts the following commands: `EOF (CTRL+D)`, `quit`, `create`, `show`, `destroy`, `all`, and `update`.

Command completion and command history are supported. 

Entering `<TAB>` will autocomplete or show you the options for autocompletion.

```
(hbnb) <TAB>
EOF	all	create	destroy	help	quit	show	update
```
Entering the `UP ARROW`	key will enter the previous command you typed the same way the regular bash shell will.

```
(hbnb) destroy BaseModel 5b4b2d85-263c-4b50-9b61-3241c84bf025
(hbnb) <UP ARROW> destroy BaseModel 5b4b2d85-263c-4b50-9b61-3241c84bf025 
```

#### EOF and quit
Typing CTRL+D or `quit` into the console will exit the console.

```
(hbnb) quit
$
```
```
(hbnb) ^D
$
```

#### create
Usage: `create <class name>`
Typing `create` followed by a class/subclass name will create a new instance of that class and print the id number of that new instance. However, if `create` is entered by itself or is followed by an invalid class name, an error will be printed.

```
(hbnb) create
** class name missing **
(hbnb) create NonExistentClass
** class doesn't exist **
(hbnb) create BaseModel
dd657136-df6e-4e3c-848f-6b69b429ecae
(hbnb) create User
94fe025f-d318-4cb9-92c4-daeeefebedda
(hbnb) create Amenity
1e490720-7ddf-4188-8631-f7dcdb1ff808
```

### show
Usage: `show <class name> <instance id>`
Typing `show` followed by a class name and a valid instance id will print the string representation of that instance. If just `show` is entered or is followed by an invalid class name or invalid instance id, an error will be printed.

```
(hbnb) show
** class name missing **
(hbnb) show NonExistentClass
** class doesn't exist **
(hbnb) show Amenity
** instance id missing **
(hbnb) show Amenity 600
** no instance found **
(hbnb) show Amenity 1e490720-7ddf-4188-8631-f7dcdb1ff808
[Amenity] (1e490720-7ddf-4188-8631-f7dcdb1ff808) {'id': '1e490720-7ddf-4188-8631-f7dcdb1ff808', 'updated_at': datetime.datetime(2019, 2, 19, 22, 52, 49, 631171), 'created_at': datetime.datetime(2019, 2, 19, 22, 52, 49, 631152)}
```

### destroy
Usage: `destroy <class name> <instance id>`
Typing `destroy` followed by a class name and a valid instance id will destroy that instance. If just `destroy` is entered or is followed by an invalid class name or invalid instance id, an error will be printed.

```
(hbnb) destroy
** class name missing **
(hbnb) destroy NonExistentClass
** class doesn't exist **
(hbnb) destroy Place
** instance id missing **
(hbnb) destroy Place 710
** no instance found **
(hbnb) show Place f498136c-76eb-4716-802e-87c9b5427d69
[Place] (f498136c-76eb-4716-802e-87c9b5427d69) {'id': 'e263b68e-e70c-4a61-a4fe-4c58f097a5f7', 'updated_at': datetime.datetime(2019, 2, 19, 20, 44, 26, 967981), 'created_at': datetime.datetime(2019, 2, 19, 20, 44, 26, 967955)}
(hbnb) destroy Place f498136c-76eb-4716-802e-87c9b5427d69
(hbnb) show Place f498136c-76eb-4716-802e-87c9b5427d69
** no instance found **
```

### all
Usage: `all` or `all <class name>`
Typing `all` into the console will print the string representation of all existing instances. If `all` is followed by a class name, the string representation of all existing instances of that class will be printed. If the class name or id is invalid, an error message will be printed.

```
(hbnb) all
["[Review] (f1941050-9e2c-47db-a13c-17ea81a78a3c) {'id': 'f1941050-9e2c-47db-a13c-17ea81a78a3c', 'updated_at': datetime.datetime(2019, 2, 19, 20, 48, 32, 606662), 'created_at': datetime.datetime(2019, 2, 19, 20, 48, 32, 606622)}", "[City] (79cec983-a8d1-4ca8-ad8f-9b6638e70184) {'id': '79cec983-a8d1-4ca8-ad8f-9b6638e70184', 'updated_at': datetime.datetime(2019, 2, 19, 20, 35, 59, 869135), 'created_at': datetime.datetime(2019, 2, 19, 20, 35, 59, 869097)}", "[Amenity] (bf75ecd4-3dfc-4390-9165-5b8229960fde) {'id': 'bf75ecd4-3dfc-4390-9165-5b8229960fde', 'updated_at': datetime.datetime(2019, 2, 19, 20, 37, 10, 805186), 'created_at': datetime.datetime(2019, 2, 19, 20, 37, 10, 805160)}", "[Place] (9ad1f688-ca26-46c3-9f2d-651584c67ae2) {'id': '9ad1f688-ca26-46c3-9f2d-651584c67ae2', 'updated_at': datetime.datetime(2019, 2, 19, 20, 45, 53, 340386), 'created_at': datetime.datetime(2019, 2, 19, 20, 45, 53, 340324)}", "[State] (34696c94-e1fc-4085-864c-388cfbe2db82) {'id': '34696c94-e1fc-4085-864c-388cfbe2db82', 'updated_at': datetime.datetime(2019, 2, 19, 20, 43, 53, 386865), 'created_at': datetime.datetime(2019, 2, 19, 20, 43, 53, 386814)}"]
(hbnb) all Review
["[Review] (f1941050-9e2c-47db-a13c-17ea81a78a3c) {'id': 'f1941050-9e2c-47db-a13c-17ea81a78a3c'    , 'updated_at': datetime.datetime(2019, 2, 19, 20, 48, 32, 606662), 'created_at': datetime.date    time(2019, 2, 19, 20, 48, 32, 606622)}"]
all NonExistent Clas
** class doesn't exist **
```

### update
Usage: `update <class name> <instance id> <attribute name> "<attribute value>"`
Typing `update` with all the required arguments will update that instance attribute (4th argument) with the value (5th argument). If any of the arguments after update are invalid or missing, an error message will be printed. Anything after the 5th argument will not be used. However, `id`, `created_at`, and `updated_at` cannot be updated, and only string/integer/float arguments can be updated.

```
(hbnb) update
** class name missing **
(hbnb) update NonExistentClass
** class doesn't exist **
(hbnb) update City
** instance id missing **
(hbnb) update City 710
** no instance found **
(hbnb) update City 79cec983-a8d1-4ca8-ad8f-9b6638e70184
** attribute name missing **
(hbnb) update City 79cec983-a8d1-4ca8-ad8f-9b6638e70184 name
** value missing **
(hbnb) show City 79cec983-a8d1-4ca8-ad8f-9b6638e70184
[City] (79cec983-a8d1-4ca8-ad8f-9b6638e70184) {'id': '79cec983-a8d1-4ca8-ad8f-9b6638e70184', 'updated_at': datetime.datetime(2019, 2, 19, 20, 35, 59, 869135), 'created_at': datetime.datetime(2019, 2, 19, 20, 35, 59, 869097)}
(hbnb) update City 79cec983-a8d1-4ca8-ad8f-9b6638e70184 name "San Francisco"
(hbnb) show City 79cec983-a8d1-4ca8-ad8f-9b6638e70184
[City] (79cec983-a8d1-4ca8-ad8f-9b6638e70184) {'id': '79cec983-a8d1-4ca8-ad8f-9b6638e70184', 'created_at': datetime.datetime(2019, 2, 19, 20, 35, 59, 869097), 'updated_at': datetime.datetime(2019, 2, 19, 20, 35, 59, 869135), 'name': 'San Francisco'}
```
