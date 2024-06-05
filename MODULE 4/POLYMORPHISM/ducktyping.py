'''
Duck Typing in Polymorphism

**Duck Typing** is a concept in object-oriented programming (OOP) that emphasizes the behavior of an object over its class. It's based on the proverb "If it walks like a duck and quacks like a duck, then it must be a duck." In the context of programming, it means that if an object has the necessary methods or attributes to be used in a particular context, then it can be used, regardless of its actual class.

**Key Points:**

- **Focus on Behavior:** Duck typing focuses on whether an object has the required functionalities, not its inheritance hierarchy.
- **Flexibility:** It allows for using objects from different classes as long as they provide the necessary interface (methods and attributes).
- **Dynamic Languages:** Duck typing is more common in dynamic languages like Python, where object types are determined at runtime.

**Example:**

Imagine you have a function `make_sound` that expects an object with a `speak` method. Here's how duck typing works:
'''
class Duck:
  def speak(self):
    return "Quack!"

class Dog:
  def bark(self):
    return "Woof!"

def make_sound(obj):
  obj.speak()

# Duck can speak
d = Duck()
make_sound(d)  # Output: Quack!

# Dog doesn't have a speak method but can be used with a little twist
dog = Dog()
make_sound(dog)  # Output: This object doesn't have a speak method.

# We can still use the dog's bark method directly
print(dog.bark())  # Output: Woof!

'''
**Duck Typing vs. Static Typing:**

- **Duck Typing (Dynamic):** Type checking happens at runtime, allowing for flexibility.
- **Static Typing:** Type checking happens at compile time, ensuring type safety but potentially less flexible.

**When to Use Duck Typing:**

- When working with code from different sources or frameworks where you might not know the exact classes beforehand.
- When creating lightweight interfaces based on behavior needs.

**Be Cautious:**

- While duck typing offers flexibility, it can lead to unexpected behavior if objects don't implement the expected methods correctly.
- Consider using type hints or documentation to clarify expected behavior, even in dynamic languages.

**Conclusion:**

Duck typing is a powerful concept in polymorphism that allows for code reusability and flexibility. However, it's essential to be aware of its potential pitfalls and use it judiciously. 
'''