# `Design Pattern`

### 1. Singleton Design Pattern`
A Singleton is creational design pattern that allows you to create just one instance of a class, throughout the lifetime of a program. The Singleton pattern disables all other means of creating objects of a class except for the special creation method. Use the Singleton pattern when a class in your program should have just a single instance available to all clients.

Benefits of singleton pattern :
- To limit concurrent access to a shared resource.
- To create a global point of access for a resource.
- To create just one instance of a class, throughout the lifetime of a program.

### 2. Prototype Design Pattern
A prototyoe is a creational design pattern that lets you copy  existing objects witout making the code dependent on their classes. It is needed when you need to create multiple instances with slightly different initial state. It is useful when you need to clone objects while preserving their state and you want to hide the complexities of object creation from the client.

Benefits of prototype pattern:
- To reduce complexity in object creation.
- To improve performance.
- To enhance flexibitlity and extansibility.
- To encapsulate object creation logic.