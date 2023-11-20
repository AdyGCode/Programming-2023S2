[Read Me](../ReadMe.md) | [Session 15](../session_15/OSS-15-Programming.md) | [Session 17](../session_17/OSS-17-Programming.md)

# Session 16 

| Delivery Mode | Date       |
|---------------|------------|
| Face-to-Face  | 2023-11-08 |
| Online        | 2023-11-15 |

We will attempt to cover items from all the stages. No guarantees... have one item to look at already...

> NB: We have moved the common details to the [[ReadMe]] document.


---

## WARNING ⚠️
No Warnings for this evening... other than background noise as usual.

---

## Session Start
6:30PM but Adrian may be available earlier...
Use the BB9 session chat...

---

## Follow Ups 🦷
- Libraries in Python (Stage 3, Intermediate Programming - Python) 
	- see [[#Stage 3 - Python]]


---
## Questions?!
Get them questions ready!
Subject / Topic and the question itself 😊

---
### Tonight...
- Last Date for submissions
	- Week 19 (6/12/23) for any chance of feedback (By Weds midnight)
	- Week 20 (13/12/23) if not worried about result (By Weds midnight)
	- Little fixes, may have some leeway.
	- Big fixes, much much much harder

- Things are a changing!
	- All face to face lecturers will be involved in online support
	- Dedicated support session(s) for each unit/cluster
	- Day/Time to be determined by lecturer in consultation with students
	- Open to online and face to face

- Need a bit of "peace n quiet"
	- Don't be afraid to ask if you can come into Perth campus for study
	- Send Adrian a Teams message!

- Feedback!
	- Please let us know where you have had problems with the content / assessments
	- **To:** online@screencraft.net.au
	- **Subject:** Continuous Improvement (CLUSTER/UNIT NAME)
	- **Body:** your feedback on structure of shell content, assessments etc.

- Stage 4: Web Tech / ... 
	- ...
	
  - Stage 3 Mobile Apps / Intermediate Python...
	- Thank you for your patience
	- We have lecturers attending to this cluster (Inter Py)

- Stage 2: C# / SQL / DDA
	- The session with Aaron from last week has been published in the C# cluster
	- If you have any other questions, please feel free to send via the helpdesk.
	- If a last minute session is needed, then let us know ASAP
  
- Stage 1: Python / etc
	- Testing in Python

---



### Stage 1: ICTPRG302 Testing
##### Useful links:
- https://www.browserstack.com/guide/unit-testing-python
- https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/
- https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index


##### General Steps: 
- Create a folder called `tests`
  ![Create tests folder](../media/image-20231115191610.png)
- In this folder create files named `test_WHAT_TESTING.py`.  For example: `test_config_reader.py`
- These files are classes.
- At top import the `unittest` package
- Also import the file/class you are testing
- So in general this looks like:
```python
  import unittest
  from FOLDER_AND_FILE_PATH_WITH_DOTS import CLASS_NAME
  
  
  class PASCALCASE_TEST_WHAT_TESTING(unittest.TestCase):
```
- Here is a specific example, based on this repository:
```python
  import unittest
  from session_16.config.config_reader import Config


  class TestConfigReader(unittest.TestCase):
      pass  # removes IDE errors 😁 remove from final code
```
  
##### Writing tests
- Write each test as a function (`def`).
- Make the test method names meaningful
- For example (from this repository)
```python
    def test_parse_config_has_correct_location_and_spaces(self):
        tcr = Config()  # tcr = TOML Config Reader
        tcr.read_config_file('../config.toml')
        config = tcr.parse_config()
        parking_lot = config['location']
  
        # Adrian prefers to use variables to make tests more readable
        expected_name = "Moondalup City Square Parking"
        expected_free = 190
        expected_max = 192
  
        # The test assertions... 
        # expected first, actual second, optional message last
   		self.assertEqual(expected_name, parking_lot['name'], "Name is not correct")
        self.assertEqual(expected_free, parking_lot['free_spaces'])
        self.assertEqual(expected_max, parking_lot['max_spaces'])
```

##### Test Assertions

There are many assertions that may be made. Often you use the "postive" assertions as they are easier to read.

The links at the start of this section contain details on the possible assertions including `assertEqual`, `assertTrue`, `assertLessEqual` and more.

##### Repeated code?
- If you are repeating code to define variables or perform common actions then use the `setUp` method.
- Remember this is helping to DRY (_Don't Repeat Yourself_) out your code. Even tests get WET (_Write Everything Twice*_) issues.
- Example from this repository:
```python 
  import unittest
  from session_16.config.config_reader import Config

  class TestConfigParsing(unittest.TestCase):
    def setUp(self):
      """ Configure the standard testing data
          This is because we remove the need for repeated code
      """
      self.tcr = Config()
      self.tcr.read_config_file('../config.toml')
      self.config = self.tcr.parse_config()
      self.parking_lot = self.config['location']
```

- If you want to use the details from the variables in the setUp method then refer to them with `self.VARIABLE_NAME` 
- Here is an example of doing that (again from this repository):
```python
  def test_read_location_free_spaces(self):
    expected_spaces = 15
    location = 'CAR'
    # tcr is instantiated as part of the setUp method
    actual_spaces = self.tcr.read_free_spaces(location)
    self.assertEqual(expected_spaces, actual_spaces)
```

#### Test Driven Development

1. Write the test
2. Run the test (fail)
3. Write code to fix the fail
4. Run the test (pass)
5. If feature complete then go to step 8
6. Update the test (add next bit of the feature test)
7. Back to step 2
8. All done... start next feature


O'Reilly books - remember to go to the Library Web Site and sign in!
- https://www.oreilly.com/library/view/test-driven-development-with/9781491958698/
- More links bookmarked on Diigo!
	- https://www.diigo.com/profile/ady_gould?query=TDD
	- https://www.diigo.com/profile/ady_gould?query=TDD+Python
	- ...

Article from Medium:
- [Test-driven-development-in-Python-Moez-Ali-Medium](Test-driven-development-in-Python-Moez-Ali-Medium.md)
### Stage 3 - Python

> Versions of python? 

- Suggestion (strong) - Add to the documentation which version of python you used when creating your application
- Always do a `pip freeze > requirements.txt` so the versions of the packages (libraries) is fixed for testing by a lecturer

> Libraries for stage 3 python? 
> 
> I was playing around with using a UI based on textual, because it makes it easy to display messages while the user is typing.
> 
> Using textual takes away from the normal way of doing stuff using the terminal; the style of doing things is more like a modern GUI.
> 
> Simply, is using libraries like this ok?

@Ady please verify this is ok with @Raf
@Ady - impression is this would be ok

### Stage 2 - C-Sharp

Test Driven Development tutes
- https://www.c-sharpcorner.com/article/test-driven-development-tdd-part-one/
- https://carlosschults.net/en/csharp-unit-testing-intro-tdd/
- https://methodpoet.com/tdd/
- https://www.coscreen.co/blog/tdd-in-c-guide/
- ...

O'Reilly books - remember to go to the Library Web Site and sign in!
- https://www.oreilly.com/library/view/practical-test-driven-development/9781788398787/
- https://www.oreilly.com/library/view/pragmatic-test-driven-development/9781803230191/B18370_03.xhtml
- https://www.oreilly.com/library/view/introducing-test-driven/9781788292092/
- ...

### Web Tech 
- Nothing asked for this evening
- ...


---
