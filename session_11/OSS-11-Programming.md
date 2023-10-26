No session conducted as Adrian at Australian Masters Hockey  Championships

[[OSS-10-Programming]] [[OSS-12-Programming]]

# Communications
- MS Teams
- eMail (online@screencraft.net.au)
# Useful Links
https://diigo.com/profile/ady_gould
https://learning.oreilly.com/search/topics/python
# WARNING ⚠️
No Warnings for this evening... other than background noise as usual.


# Session Start
6:30PM but Adrian may be available earlier...
Use the BB9 session chat...
# Questions?!
Get them questions ready!
Subject / Topic  and the question itself 😊

### SQL and Nested Queries

- [Shop DDL SQL File](../session_09/shop_ddl.sql)
- [Shop Queries File](../session_09/shop_01.sql)
### Comparing Languages

JavaScript, C#, Java from C family
Python 
Ruby 

| Structure          | Python                       | C#                                           | JavaScript                                   |
| ------------------ | ---------------------------- | -------------------------------------------- | -------------------------------------------- |
| Variable           | `total = 0`                  | `int32 total = 0;`                           | `let total = 0`                              |
| Constants          | `PI = 3.141`                 | `const float PI = 3.14;`                     | `const PI = 3.141`                           |
| Operators          |                              |                                              |                                              |
| Plus               | `+`                          |                                              |                                              |
| Minus              | `-`                          |                                              |                                              |
| Multiply           | `*`                          |                                              |                                              |
| Divide             | `/`                          |                                              |                                              |
| Remainder (Modulo) | `%`                          |                                              |                                              |
| Integer Division   | `//`                         |                                              |                                              |
| Power (Indices)    | `2**3`                       | `x = Math.Pow(2,3)`                          | `2**3`                                       |
| For                | `for number in range(0,10):` | `for (int number=0; number<10; number++) {}` | `for (let number=0; number<10; number++) {}` |
| For each           | `for item in list_of_items:` | `foreach (int item in list_of_items_ {}`     | `foreach(let item of list_of_items) {}`      |
|                    |                              |                                              | `list_of_items.forEach( ()=>{} )`            |
| Decisions (if)     | `if total > 100: `           | `if (total>100) {}`                          | `if (total>100) {}`                          |
|                    |                              |                                              |                                              |


```python
name = input('Enter Name, or \q to quit')
if name == 'Adam':
    greeting = "Croeso."
else:
    if name == 'Barbara':
        greeting = "Bonjour."
    else:
        if name == 'Charlie':
            greeting = "Hola."
        else:
            greeting = "Hello."  # the default option
      
print(greeting) 
```

```python
name = input('Enter Name, or \q to quit')

if name == 'Adam':
    greeting = "Croeso."
elif name == 'Barbara':
    greeting = "Bonjour."
elif name == 'Charlie':
    greeting = "Hola."
else:
    greeting = "Hello."  # the default option
 
print(greeting)  
```

```python
name = input('Enter Name, or \q to quit')

greeting = "Hello."  # the default option
if name == 'Adam':
    greeting = "Croeso."
elif name == 'Barbara':
    greeting = "Bonjour."
elif name == 'Charlie':
    greeting = "Hola."
 
print(greeting)      
```

Intelligent defaults

- `total = 0`
- `smallest = list_of_items[0]`
- `largest = list_of_list[0]
- `name = ""`
- `name = None`

```python

xo_board = [None, None, None, None, None, None, None, None, None]

xo_board = [None]*9

xo_board_2d = [ [None, None,None], [None,None,None],[None,None,None]]
xo_board_2d = [[None*3]*3]  ## Will not work as expected
xo_board_2d = [[None] for num in range(3)]
```

