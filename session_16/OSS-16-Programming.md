[Session 15](../session_15/OSS-15-Programming.md) | [Session 17](../session_17/OSS-17-Programming.md)

# Session 16 

| Delivery Mode | Date       |
|---------------|------------|
| Face-to-Face  | 2023-11-08 |
| Online        | 2023-11-15 |

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
## Questions?!
Get them questions ready!
Subject / Topic and the question itself 😊

---
### Tonight...
- Stage 4: Web Tech / ... 
	- ...
  
- Stage 3 Mobile Apps / Intermediate Python...
	- Thank you for your patience
    - We have lecturers attending to this cluster

- Stage 2: C# / SQL / DDA
	- The session with Aaron from last week has been published in the C# cluster
    - If you have any other questions, please feel free to send via the helpdesk.
    - If a last minute session is needed, then let us know ASAP
  
- Stage 1: Python / etc
	- Testing in Python

---

#### Stage 1: ICTPRG302 Testing
Useful links:
- https://www.browserstack.com/guide/unit-testing-python
- https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/
- https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index


##### General Steps: 
- Create a folder called tests
- In this folder create files named test_WHAT_TESTING.py
- example: `test_config_reader.py`
- These files are classes.
- At top import the unittest package
- Also import the file/class you are testing
- So in general this looks like:
- ```python
  import unittest
  from FOLDER_AND_FILE_PATH_WITH_DOTS import CLASS_NAME
  
  
  class CAMELCASE_TEST_WHAT_TESTING(unittest.TestCase):
  ```
- Here is a specific example, based on this repository:
- ```python
  import unittest
  from session_16.config.config_reader import Config


  class TestConfigParsing(unittest.TestCase):
      pass  # removes IDE errors 😁 remove from final code
  ```
  
##### Writing tests
- Write each test as a function (`def).
- Make the names meaningful
- For example (from this repository)
- ```python
    def test_parse_config_has_correct_location_and_spaces(self):
        tcr = Config()
        tcr.read_config_file('../config.toml')
        config = self.tcr.parse_config()
        parking_lot = self.config['location']
  
        # Adrian prefers to use variables to make tests more readable
        expected_name = "Moondalup City Square Parking"
        expected_free = 190
        expected_max = 192
        # the test assertions...
        self.assertEqual(parking_lot['name'],   expected_name)
        self.assertEqual(parking_lot['free_spaces'], expected_free)
        self.assertEqual(parking_lot['max_spaces'], expected_max)
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




Thanks for the evening
