[Read Me](../ReadMe.md) | [Session 16](../session_16/OSS-16-Programming.md) | [Session 18](../session_18/OSS-18-Programming.md)

# Session 17 

| Delivery Mode | Date       |
|---------------|------------|
| Face-to-Face  | 2023-11-15 |
| Online        | 2023-11-22 |

We will attempt to cover items from all the stages. No guarantees... have one item to look at already...

> NB: We have moved the common details to the [ReadMe](../ReadMe.md) document.


---

## WARNING ⚠️
No Warnings for this evening... other than background noise as usual.

---

## Session Start
6:30PM but Adrian may be available earlier...
Use the BB9 session chat...

---

## Follow Ups 🦷
- A number of follow ups are in these notes already
- ...


---
## Questions?!
Get them questions ready!
Subject / Topic and the question itself 😊

---
### Quick Notes...
- Last Date for submissions
	- Week 19 (6/12/23) for any chance of feedback (By Weds midnight)
	- Week 20 (13/12/23) if not worried about result (By Weds midnight)
	- Little fixes, may have some leeway.
	- Big fixes, much much much harder

- Need a bit of "peace n quiet"
	- Don't be afraid to ask if you can come into Perth campus for study
	- Send Adrian a Teams message!

- Feedback!
	- Please let us know where you have had problems with the content / assessments
	- **To:** online@screencraft.net.au
	- **Subject:** Continuous Improvement (CLUSTER/UNIT NAME)
	- **Body:** your feedback on structure of shell content, assessments etc.



---

### Everyone

#### Code Commenting
This is a commonly asked question that really depends on the level of skill of the developer, and the complexity of the code.

Here are some guidelines for you:
- Code Documentation does not mean putting a comment for every line
- Good code is easily read and understood
- If a piece of code is complex, then add comments explaining the *BLOCK* of code, and not every line.
- Use "Doc strings" for functions  to explain what they are and how to use them.

> The basics tenets of commenting your code are simple:
> - Make them brief
> - Keep them relevant
> - Use them liberally, but not to excess
> 
> If you can keep those in mind, you’ll be doing pretty okay.
> 
> _B.J. Keeton, 2019_

Useful reference:
- (The Art of Writing Efficient Code Comments)[The-Art-of-Writing-Efficient-Code-Comments.md] 
- 

### Stage 1: ...

#### ICTPRG302 Project
- You do not need to write extra tests using Unit testing nor doc-block-tests
- Add the tests you run interactively to the documentation/journal.
- You are able to write the tests as if you were interactively testing the code, as in:
		- Test Word: bangs. 
	  Guess: Hauls. 
	  Response: -+--+
		- Test Word: bangs. 
	  Guess: Parts. 
	  Response: -+--+
		- ...

#### Introduction to Programming for Robotics and IoT (IP4RIoT)

Our IP4RIoT lecturers have added a new version of the project for those who wish to be more guided through the content of the project.

Instructions for version 2 of the project should be complete by the end of the week, with this version having about 20 pages long. 

You now have  a choice of flavours, depending on how you want to tackle the project.

BOTH versions are VALID for submission! 

You complete ONLY ONE of them.

The second version is much longer ONLY because the  the instructions are detailed and explicit.

Rafael will record an online session at 4pm on Thursday, which all are welcome to join, where he will step through the new version of the project. 

He will also be demonstrating on Wednesday afternoon to the face-to-face students - this code may be found on the NM-TAFE github repositories: https://github.com/NM-TAFE/civ-ipriot-in-class-demos

New version may be also found at: 
[https://github.com/NM-TAFE/civ-ipriot-in-class-demos/blob/2023/s2/raf/activities/carpark-prj-guided.md](https://github.com/NM-TAFE/civ-ipriot-in-class-demos/blob/2023/s2/raf/activities/carpark-prj-guided.md "https://github.com/nm-tafe/civ-ipriot-in-class-demos/blob/2023/s2/raf/activities/carpark-prj-guided.md")



### Stage 2:  C# / SQL / DDA


#### DDA/SQL

##### SQL Commenting

Basics:

```sql
-- single line comment
```
and...
```sql
/* 
    This is a 
    Multiple Line comment
    Or comment block
*/
```

This example is more of a description of the method used than what the SQL is doing. Great for beginners.

> Note that you should try to keep comments to between 72 to 90 character lines. They are much easier to read. 
> 
> Unfortunately, **not** all examples below follow this guideline.

```sql
-- Always ensure you are in the correct database/schema
USE stored_proc_tutorial;

-- if you are developing, then adding a drop procedure will help reduce problems with debugging  
DROP PROCEDURE IF EXISTS GetStudentData;
  
/* 
   Create the procedure by:
   
   - Set custom delimiter $$
   - Create the procedure (function) 
   - BEGIN the procedure code
   - Write the SQL for the procedure
   - END the procedure
   - Return delimiter to ;
*/
DELIMITER $$
CREATE PROCEDURE GetStudentData()
BEGIN
    SELECT * FROM studentMarks;
END$$
DELIMITER ;
```


##### Some useful links for SQL/DDA

- MySQL STORED PROCEDURE Tutorial With Examples: https://www.softwaretestinghelp.com/mysql-stored-procedure/ 
- How to Use MySQL Stored Procedures to Simplify Database Operations: https://www.freecodecamp.org/news/how-to-simplify-database-operations-using-mysql-stored-procedures/
- How to Create a Simple MySQL Stored Procedure (YouTube | Database Star): https://www.youtube.com/watch?v=7ReXGwNrw5g
- Learn MySQL: The Basics of MySQL Stored Procedures: https://www.sqlshack.com/learn-mysql-the-basics-of-mysql-stored-procedures/

##### dBeaver hiccup with Stored Procedure Creation

 - It has been noted that dBeaver will not work as expected when defining a Stored procedure using SQL.
	 - If you get an error such as:
		   ![SQL Error for stored procedure](../media/image-20231120150848.png)
		   
	 - Then SELECT the whole query (as shown below) and execute that 'statement' by right clicking the selection, hover over Execute and then select *Execute SQL Script*.
	   ![Execute SQL Script](../media/image-20231120150056.png)
		   
	- Alternatively, use `ALT`+`X` to execute the selected lines:
	   ![ALT X shortcut to execute script](../media/image-20231120152604.png)
		   
	- Another item you could do is to drop the procedure before creating the procedure:
	  ![Drop procedure](../media/image-20231120150818.png)
	  
	- Example code [SQL Stored Procedure Demo SQL](SQL-Stored-Procedure-Demo.sql)



### Stage 3: ...



### Stage 4: ...


#### Web Project



#### KBAs

As these two KBAs cover some common items, rather than duplicate we will list them in a Common section.

#### Common items
- Terminology
	- An internet
	- Cascading Style Sheets (CSS)
	- Certificates
	- Content Management System (CMS)
	- Cookies
	- Domain Name
	- Domain Name Service (DNS)
	- Elements
	- eXtensible Markup Language (XML)
	- Extranet
	- File Transfer Protocol (FTP)
	- File Transfer Protocol Secured (FTPS)
	- Hypertext Markup Language (HTML)
	- Hypertext Transfer Protocol (HTTP)
	- Hypertext Transfer Protocol Secure (HTTPS)
	- Intranet
	- Internet Protocol Address (IP Address)
	- Message Queuing Telemetry Transport (MQTT)
	- Network Time Protocol (NTP)
	- Ports
	- Protocol
	- Secure File Transfer Protocol (SFTP)
	- Secure Sockets Layer (SSL)
	- Semantics
	- Simple Mail Transfer Protocol (SMTP)
	- Standardised Generalised Markup Language (SGML)
	- Tags
	- The Internet
	- Transmission Control Protocol over Internet Protocol (TCP/IP)
	- Transport Layer Security (TLS)
	- Uniform Resource Locator (URL)
	- User Experience (UX)
	- User Interface (UI)
	- Virtual Reality Markup Language (VRML)
	- Web Server
	- Web sockets


##### ICTWEB452 (25 Questions)
This KBA covers:
- Past and Current standards for HTML and CSS
- HTML
	- HTML Structural elements
	- HTML Presentational elements
	- HTML Semantic elements
- Web browsers
	- HTML rendering engines
	- JavaScript Engines
- Design and Testing
	- Testing Websites
	- Responsive Design
	- Web Accessibility
		- Common accessibility issues
	- Website documentation
- Deployment of Websites
	- Web Server
	- Content
	- Data storage
	- DNS

##### ICTWEB441 (25 Questions)
This KBA covers:
- Past and Current standards for:
	- HTML and 
	- CSS
- JavaScript/ECMAScript
	- Common name
	- Formal name
	- Past and current standards
- JavaScript
	- Objects
	- Event handlers
	- Document Object Model
	- Events
	- Default behaviour
	- Forms and events
	- Understanding code
- Hypertext Transfer Protocol
	- HTTP Verbs
	- HTTP Response codes
	- URL structure
- Development Practices
	- WET Code
	- DRY Code
	- Testing
		- Manual
		- Unit
		- Regression
		- Headless
		- et al
	- Documentation
	- Good code practices
- Security
	- Cross Site Scripting
	- Cross Site Request Forgery
	- Data Validation
	- Protocols
- Server-Side Code
	- Dynamic sites
	- Data retrieval
	- Security
	- Processing
	- Content
- Open Platform Programming
	- Open standards
	- Open data
	- Data access
	- Interoperability
	- Integration


---

## References

Agrawal, D. (2022, March 14). _C++ Comments- Types, Use Cases, Examples_. Scaler Topics. https://www.scaler.com/topics/cpp/comments-in-cpp/

B.J. Keeton. (2019). _How to Comment Your Code Like a Pro: Best Practices and Good Habits_. Elegant Themes. https://www.elegantthemes.com/blog/wordpress/how-to-comment-your-code-like-a-pro-best-practices-and-good-habits

_C# Comments: How to Use Them and Why?_ (n.d.). Www.programiz.com. https://www.programiz.com/csharp-programming/comments

_C++ Programming/Code/Style Conventions/Comments - Wikibooks, open books for an open world_. (2020). Wikibooks.org. https://en.wikibooks.org/wiki/C%2B%2B_Programming/Code/Style_Conventions/Comments

‌_C++ Style Guidelines_. (n.d.). Www.cs.fsu.edu. Retrieved November 21, 2023, from https://www.cs.fsu.edu/~myers/c++/notes/style.html

‌‌_Comments in Python: Best Practices_. (n.d.). Www.youtube.com. Retrieved November 21, 2023, from https://www.youtube.com/watch?v=0NO3MJkxm2g

_Comments in Python: Why are They Important And How to Use Them_. (2021, March 26). Simplilearn.com. https://www.simplilearn.com/tutorials/python-tutorial/comments-in-python
‌
_Create Python Comments the Right Way_. (2023, January 6). Kinsta®. https://kinsta.com/blog/python-comments/

‌_How to Create a Simple MySQL Stored Procedure_. (n.d.). Www.youtube.com. Retrieved November 21, 2023, from https://www.youtube.com/watch?v=7ReXGwNrw5g

‌_How to Use MySQL Stored Procedures to Simplify Database Operations_. (2023, June 12). FreeCodeCamp.org. https://www.freecodecamp.org/news/how-to-simplify-database-operations-using-mysql-stored-procedures/

‌_How to Write PHP Comments (and best practices) - PHP 101_. (2022, January 20). PHP 101. https://php101.net/how-to/write-php-comments-and-best-practices/

Juvlier, J. (2021, December 10). _How to Make PHP Comments (And Why You Should Know)_. Blog.hubspot.com. https://blog.hubspot.com/website/php-comments

Kosourova, E. (2021, June 19). _The Art of Writing Efficient Code Comments_. Medium. https://towardsdatascience.com/the-art-of-writing-efficient-code-comments-692213ed71b1

McCallum, N. (2020, June 20). _How to Write C++ Comments_. Www.nickmccullum.com. https://www.nickmccullum.com/how-to-write-cpp-comments/

_MySQL STORED PROCEDURE Tutorial With Examples_. (n.d.). Www.softwaretestinghelp.com. https://www.softwaretestinghelp.com/mysql-stored-procedure/

‌Payne, J. (2021, July 8). _Commenting Best Practices in C#_. CodeGuru. https://www.codeguru.com/csharp/commenting-best-practices-in-c/

‌Prtenjak, M. (2023, February 24). _Different Types of Comments in C# and Should We Use Them_. Code Maze. https://code-maze.com/csharp-different-types-of-comments/
‌
Real Python. (2018, November 5). _Writing Comments in Python (Guide)_. Realpython.com; Real Python. https://realpython.com/python-comments-guide/

Schults, C. (2019, March 5). _C# Comments: A Complete Guide, Including Examples - SubMain Blog_. Software Quality Blog - SubMain Software. https://blog.submain.com/c-comments-complete-guide/

Sechrest, R. (2023, November 7). _PHP style guide with coding standards and best practices._ Gist. https://gist.github.com/ryansechrest/8138375

‌TylerMSFT. (2021, August 3). _Comments (C++)_. Learn.microsoft.com. https://learn.microsoft.com/en-us/cpp/cpp/comments-cpp?view=msvc-170

‌Upadhyay, N. (2021, January 8). _Learn MySQL: The Basics of MySQL Stored Procedures_. SQL Shack - Articles about Database Auditing, Server Performance, Data Recovery, and More. https://www.sqlshack.com/learn-mysql-the-basics-of-mysql-stored-procedures/

‌‌
‌