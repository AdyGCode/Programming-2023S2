[Session 15](../session_15/OSS-15-Programming.md) | [Session 17](../session_17/OSS-17-Programming.md)

# Session 16 

| Delivery Mode | Date       |
|---------------|------------|
| Face-to-Face  | 2023-11-08 |
| Online        | 2023-11-15 |

We will attempt to cover items from all the stages. No guarantees... have one item to look at already...

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

## WARNING ⚠️
No Warnings for this evening... other than background noise as usual.

---

## Session Start
6:30PM but Adrian may be available earlier...
Use the BB9 session chat...

---

## Follow Ups 🦷
- ...

---
## Communications
- MS Teams
- eMail (online@screencraft.net.au)

See below for eMail based help.
---
## Requests for Assistance

Asking for assistance is an important skill.

When asking in class, make sure you explain the problem clearly. Doing this often will help you solve your own problems.

This is part of what is known as **Rubber Duck Debugging**.

This then applies to when you are seeking assistance via eMail or via Teams chat.

### Help Desk

The Help Desk is one of the ways we provide 
assistance to all students.

- https://help.screencraft.net.au

Our help desk system has a ticketing component where you email your queries, and a FAQ (Frequently Asked Questions) section for commonly requested items.

The links below will take you to the FAQs and a 
method to log in to the Help Desk to view your 
tickets.

- FAQs: https://help.screencraft.net.au/hc/1990208628
- Your Tickets: https://help.screencraft.net.au/help/2561559896/auth

### How to Request Assistance
To make it easier for the lecturers to respond when 
asking for help via the Help Desk, make sure you 
follow the guidelines below.

> When sending the email it **MUST** come from your 
> TAFE email address. All others are rejected.

The email Address depends on the study mode you are in:

| Study Mode                | eMail Address             |
|:--------------------------|:--------------------------|
| **Fully** Online Students | online@screencraft.net.au |
| Face to Face Students     | f2f@screencraft.net.au    |

Make sure you include the following details:

| Item          | What to include                                         |
|:-------------:|---------------------------------------------------------|
| Subject       | CLUSTER/UNIT NAME, Item asking about                    |
| Body of eMail | Course name                                             |
| -"-           | Cluster Name or Unit Number                             |
| -"-           | Session or Assessment being asked about                 |
| -"-           | Details of the problem                                  |
| Attachments   | Include screen shots and Zipped source code as required |

---
## Useful Links
- GitHub Repository of Code and Notes
	- [AdyGCode/Programming-2023S2 (github.com)](https://github.com/AdyGCode/Programming-2023S2)
	  https://github.com/AdyGCode/Programming-2023S2
- Adrian's Diigo Account 
  - https://diigo.com/profile/ady_gould

### eLibrary
NMTAFE provides access for Students to the O'Reilly bookshelf. Within this bookshelf we have identified some searches you may find useful.

Details on how to access the Online Bookshelf for free  are shown here: https://northmetrotafe.libanswers.com/faq/271042 and the O'Reilly Library is available here: https://www.oreilly.com/library-access/

- O'Reilly Books/Videos etc (via TAFE Library)
    - python -  https://learning.oreilly.com/search/?q=python&type=*&rows=100
    - sql -  https://learning.oreilly.com/search/?q=sql&type=*&rows=100
    - mysql -  https://learning.oreilly.com/search/?q=mysql&type=*&rows=100
    - wpf -  https://learning.oreilly.com/search/?q=wpf&type=*&rows=100
    - html -  https://learning.oreilly.com/search/?q=html&type=*&rows=100
    - javascript -  https://learning.oreilly.com/search/?q=javascript&type=*&rows=100
    - C# -  https://learning.oreilly.com/search/?q=C%23&type=*&rows=100

---


#### Stage 1: ICTPRG302 Testing
Useful links:
- https://www.browserstack.com/guide/unit-testing-python
- https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/
- https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index


##### General Steps: 
- Create a folder called `tests`
  ![[Pasted image 20231115191610.png]]
- In this folder create files named `test_WHAT_TESTING.py`
- example: `test_config_reader.py`
- These files are classes.
- At top import the `unittest` package
- Also import the file/class you are testing
- So in general this looks like:
- ```python
  import unittest
  from FOLDER_AND_FILE_PATH_WITH_DOTS import CLASS_NAME
  
  
  class PASCALCASE_TEST_WHAT_TESTING(unittest.TestCase):
  ```
- Here is a specific example, based on this repository:
- ```python
  import unittest
  from session_16.config.config_reader import Config


  class TestConfigParsing(unittest.TestCase):
      pass  # removes IDE errors 😁 remove from final code
  ```
  
##### Writing tests
- Write each test as a function (`def`).
- Make the names meaningful
- For example (from this repository)
- ```python
    def test_parse_config_has_correct_location_and_spaces(self):
        tcr = Config()  # tcr = TOML Config Reader
        tcr.read_config_file('../config.toml')
        config = tcr.parse_config()
        parking_lot = config['location']
  
        # Adrian prefers to use variables to make tests more readable
        expected_name = "Moondalup City Square Parking"
        expected_free = 190
        expected_max = 192
  
        # the test assertions...
   		self.assertEqual("Moondalup City Square Parking", "Name is not correct", parking_lot['name'])
        self.assertEqual(122, parking_lot['free_spaces'])
        self.assertEqual(192, parking_lot['max_spaces'])
  ```
##### Test Assertions
There are many assertions that may be made. Often you use the "postive" assertions as they are easier to read.

The links at the start of this section contain details on the possible assertions including `assertEqual`, `assertTrue`, `assertLessEqual` and more.

##### Repeated code?
- If you are repeating code to define variables or perform common actions then use the `setUp` method.
- Example from this repository:
- ```python 
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
- ```python
  def test_read_location_free_spaces(self):
    expected_spaces = 15
    location = 'CAR'
    # tcr is instantiated as part of the setUp method
    actual_spaces = self.tcr.read_free_spaces(location)
    self.assertEqual(expected_spaces, actual_spaces)
  ```



## Web Tech 

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
- [[Test-driven-development-in-Python-Moez-Ali-Medium]]
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

## Stage 2 - C-Sharp

Test Driven Development tutes
- https://www.c-sharpcorner.com/article/test-driven-development-tdd-part-one/
- https://carlosschults.net/en/csharp-unit-testing-intro-tdd/
- https://methodpoet.com/tdd/
- https://www.coscreen.co/blog/tdd-in-c-guide/
- 

O'Reilly books - remember to go to the Library Web Site and sign in!
- https://www.oreilly.com/library/view/practical-test-driven-development/9781788398787/
- https://www.oreilly.com/library/view/pragmatic-test-driven-development/9781803230191/B18370_03.xhtml
- https://www.oreilly.com/library/view/introducing-test-driven/9781788292092/
- 