# Common-mode
factory pattern
---
The factory pattern is a design pattern used to create objects in software development.When the program runs into a "type", the corresponding object needs to be created.That's the factory model.In this case, the implementation code is based on the factory pattern and can be scalable, maintainable code.When a new type is added, there is no need to modify the existing classes, only to add subclasses that generate new types.

builder pattern
---
Builder pattern: the construction of a complex object is separated from his presentation, allowing the same build process to create different representations.

#### The basic idea
The construction of a certain type of product consists of many complex components.
Some of the details in these components are different, and the product representations are slightly different;
Step by step the product creation step by step by a commander;
When you need to create different products, you only need to derive a specific builder and override the corresponding component build method.
