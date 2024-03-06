# AirBnB clone

A project to create a simple clone of the [AirBnB website](https://airbnb.com).
Not all the components will be implement.

## console

This is the first part.
Manipulation of objects are done at this point.

The following objects are manipulated:

	- Create a new object (ex: a new User or a new Place)
	- Retrieve an object from a file, a database etc…
	- Do operations on objects (count, compute stats, etc…)
	- Update attributes of an object
	- Destroy an object

A parent `class` called `BaseModel` is created here.
This will take care of the initialization, serialization and deserialization.

A simple flow of data will be created at this point.

Some of the classes that will be created at this point is:

	- User
	- State
	- City
	- Place
	- e.t.c

Create a file storage type of thing and create unittests (some of them are from the community).

### How to start the command interpreter
To start the interpreter we run our script containing the class which inherits from the ```cmd.Cmd``` class ```python3 script_name```
The file is created in the steps below:

- We first need to import the module cmd.
- Then create a class that inherits from the ```cmd.Cmd``` class and add all the methods within this class.
- At the bottom of the file we add:

>if __name__ == "__main__":
>	name_of_class().cmdloop()

- This ensures our class is not executated when imported and that our interpreter is in interactive mode until we quit.

## How to use the command interpreter
- To use the interpreter, we pass our function name with its parameters (*if it has any*) after the prompt and press ```Enter```
- The methods within our child class inheriting from the Cmd class must start with ```do_``` then our function e.g ```do_add```
***Note***: We pass our function names without the ```do_```.
- To obtain information about the methods contained we use ```help```
- By default our prompt is ```(Cmd)```, we can change this by using a variabe ```prompt = custom_prompt```. We can also change it using the ```do_prompt``` method by accessing the declared variable through ```self.prompt```.
- To run our interpreter in non interactive mode add code above our ```cmdloop()``` that checks if the number of arguments is more than 1; if it is we execute it in non interactive mode by passing all our arguments as one string into our interpreter without adding the ```cmdloop()```
