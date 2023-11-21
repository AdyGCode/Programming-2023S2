## Best practices of code commenting for data science tasks

Written by Elena Kosourova
From [The Art of Writing Efficient Code Comments - Medium.com](https://towardsdatascience.com/the-art-of-writing-efficient-code-comments-692213ed71b1)

If we run `import this` in a Jupyter notebook, or simply open [this link](https://www.python.org/dev/peps/pep-0020/), we'll get _The Zen of Python_, a collection of 19 guidelines for Python's design gathered by Tim Peters. One of them says: "Readability counts", and in this article, we're going exactly to discuss one of the aspects of this principle: code comments, which are pieces of natural language text included in the code and used for its documentation. 

Indeed, code comments, together with clean code, correct naming of variables and functions, and making the code as explicit as possible, contribute significantly to the readability of our projects. 

This can be very helpful not only to the people who will read our work in the future but also for ourselves when we return to it after some time.

In this article, we’ll focus on the best practices of commenting the Python code applied to data science tasks. However, the majority of these guidelines are also valid for any other programming language or sphere.

## Syntax and Styling

In Python, there are 2 types of code comments: block and inline ones.

According to [PEP 8](https://www.python.org/dev/peps/pep-0008/#comments), **block comments** start with a hash (`#`) followed by a single space, and consist of one or more sentences, with the first word capitalized and a period at the end of each sentence. If there are several sentences, they are separated by two spaces. Block comments are separated from the code above by an empty line. They apply to the code that directly follows them (with no empty line) and have the same indentation with it.

A long line of a block comment should be spread over several lines, each starting with a hash followed by a single space. Another way of writing multi-line comments in Python is by using **multi-line strings** — those embedded in triple single or double quote marks. Technically, they were originally designed for another purpose: assigning documentation to functions, methods, or classes. However, if not used in this quality or not assigned to a variable, a multi-line string generates no code, so it can serve as an unconventional way of code commenting in Python. This approach was approved by the founder of Python Guido van Rossum in his [Twitter](https://twitter.com/gvanrossum/status/112670605505077248).

#### ✔️ Good 
```python
# Isolate the outliers with at least $3,500 spent per month except 
# for the cases when the respondent hadn't attended any bootcamp or 
# had been learning programming for a maximum 3 months before the 
# survey.
above_3500 = usa[(usa['MoneyPerMonth']>=3500)\                &(usa['AttendedBootcamp']!=0.0)\                & usa['MonthsProgramming']>3.0)]
```

#### ✔️ Good 
```python
'''Isolate the outliers with at least $3,500 spent per month except for the cases when the respondent hadn't attended any bootcamp or had been learning programming for a maximum 3 months before the survey.'''
above_3500 = usa[(usa['MoneyPerMonth']>=3500)\                &(usa['AttendedBootcamp']!=0.0)\                &(usa['MonthsProgramming']>3.0)]
```

#### ✔️ Good 
```python
"""Isolate the outliers with at least $3,500 spent per month except for the cases when the respondent hadn't attended any bootcamp or had been learning programming for a maximum 3 months before the survey."""
above_3500 = usa[(usa['MoneyPerMonth']>=3500)\                &(usa['AttendedBootcamp']!=0.0)\                &(usa['MonthsProgramming']>3.0)]
```

An **inline comment** is placed on the same line as the piece of code it comments, separated from it by at least two spaces, a hash, and a single space. Inline comments are usually shorter and should be used with caution since they tend to be visually mixed with the lines of code above and below them, and, as a consequence, become unreadable, like in this piece of code:

#### ❌ Bad
```python
ax.set_title('Book Rating Comparison', fontsize=20)  
ax.set_xlabel(None)  # remove x 
labelax.tick_params(axis='both', labelsize=15)
plt.show()
```

#### ✔️ Good 
Sometimes, though, inline comments can be indispensable:

```python
colors = [
    [213/255,94/255,0],         # vermillion
    [86/255,180/255,233/255],   # sky blue
    [230/255,159/255,0],        # orange
    [204/255,121/255,167/255]   # reddish purple
]
```

Please pay attention that in the code above, the alignment of inline comments helps to improve their readability.

Even though the guidelines on the code comment syntax are designed to make the code more readable and consistent, we should keep in mind that the language itself evolves, and so do the styling conventions. Also, a company (or a particular project) can have its own coding style approaches, and then the priority is given to those case-specific recommendations, if different from PEP 8. Hence, sometimes the official guidelines can be ignored. However, some practices should be avoided almost always:

-   Using more than one hash before a comment
-   Using one or more hashes also at the end of a comment
-   Omitting a space between a hash and a comment
-   Using all capital letters (we’ll see later an exception)
-   Omitting an empty line after a piece of code above the comment
-   Inserting an empty line between a comment and its related code
-   Ignoring the indentation of the commented code

These approaches are undesirable, because they clutter the code with unnecessary elements, decrease its readability, and make it difficult to distinguish between separate code blocks. Compare these identical pieces of code different in comment styling:

#### ❌ Bad 
```python
### REMOVE ALL THE ENTRIES RELATED TO 2021 ###
questions = questions[questions['Date'].dt.year < 2021]
### CREATE A LIST OF TAGS ###
tags_list = list(tags.keys())
```

#### ✔️ Good
```python
# Remove all the entries related to 2021.
questions = questions[questions['Date'].dt.year < 2021]
# Create a list of tags.
tags_list = list(tags.keys())
```

## Writing Meaningful Comments

If the code itself says what to do to a computer, the code comments are addressed to human beings, explaining to them what this code exactly does and especially why we need it. About the “what”, there is a widespread opinion that if our code is as explicit and plain as possible, if we used self-explanatory names for variables and functions, then we almost don’t need code comments at all. Even though I agree that writing an easily understandable code and selecting variable/function names carefully is very important, I would argue that code comments are rather useful as well.

-   They help to section the code into several logical parts making it easier to navigate.
-   They are useful for explaining the functionality of a rarely used or new method / function. Also, it’s a good idea to add code comments if we have to apply an unusual/non-evident approach to coding because maybe of some bugs / technical issues / version conflicts detected when trying to follow a more explicit way.
-   Writing a code, we should keep in mind people (e.g. our colleagues) who could read our code in the future. What is clear for one person can be not evident at all for another. Hence, we should try to take into consideration a potential gap in experience, technical and contextual knowledge of different people, and facilitate their task by using comments.
-   Code comments are valuable for adding the information on the authors, a date, and status of modifications (e.g. `# Updated by Elena Kosourova, 22.04.2021. Added an annotation of the current year on the graph.`).

Hence, code commenting is a fast and powerful approach to improve code readability and accessibility, and for writing clear and meaningful comments, it’s not enough just to be a good coder — it’s important also to be a good writer, which is almost a skill to learn per se.

Let’s consider some suggestions we should follow to apply code commenting efficiently and prevent overusing it.

## Avoid obvious code comments

Our comments shouldn’t state evident or clear from the context things. Once again, let’s remember here that the “evident” can vary from one person to another, and also the scope and target audience of our work matters (for example, if we’re writing a real-data project on data science or a manual for students). Our task here is to find the balance.

#### ❌ Bad
```python
# Import libraries.
import pandas as pd
import numpy as np
```

## Avoid inefficient code comments

For being useful at maximum, our code comments should be as precise and laconic as possible, giving all the necessary details about their piece of code and excluding any irrelevant information such as observations from the previous code, intentions for the future, or parenthesis. Also, since the code usually implies some dynamics (it _does_, _creates_, _removes_, etc.), a good practice is to use verbs rather than nouns:

#### ❌ Bad: Too vague
```python
# Select a specific type of columns.
characters = star_wars.iloc[:, 15:29]
```
#### ❌ Bad: Too wordy
```python
# Now, let's select all the columns of a radio-button type from our dataframe.
characters = star_wars.iloc[:, 15:29]
```
#### ❌ Bad: Observations from the previous code
```python
# Select radio-button type columns, as done earlier for checkbox type ones.
characters = star_wars.iloc[:, 15:29]
```
#### ❌ Bad: Using a noun instead of a verb
```python
# Selection of radio-button type columns.
characters = star_wars.iloc[:, 15:29]
```
#### ✔️ Good
```python
# Select radio-button type columns.
characters = star_wars.iloc[:, 15:29]
```

## Update code comments

It’s a tricky and very common pitfall, but we should always remember to introduce all the necessary modifications also to the code comments when the code changes. 

As [PEP 8](https://www.python.org/dev/peps/pep-0008/#comments) states, _“comments that contradict the code are worse than no comments”._ 

What’s more, sometimes we have to check not only the code comment related to the modified piece of code but also the other ones that can be indirectly influenced by such changes.

## Language to use

A common practice is to write code comments always in English. However, this is one of those rules that can be ignored in some cases: if we’re absolutely sure that our code will never be read by people who don’t speak our language (or whatever other language in common), then we’d better write the comments exactly in that language. 

In this case, the code becomes more comprehensible exactly for our particular target audience.

## Commenting out pieces of code

Sometimes, working on a project, we find it useful to test several methods for the same task or for debugging the code, and then we can decide to keep some of those tested pieces commented-out, even if we select another one at the end, just in case. 

However, this approach is good only temporarily, and in the final version of the project, it’s important to clean out such fragments.

Indeed, it can be very distracting for those people (including ourselves after some time) who will read this code in the future. The reader could start having doubts if the commented-out piece of code was somehow useful at any step, and if it should be kept in the project.

To avoid this confusion, it’s better just to remove all commented-out code.

As usual, there can be very rare exceptions from this best practice.

Let’s say, our work is about showing different ways of obtaining the same result, and one approach is more preferable to another (which is still feasible but less used). In this case, we may focus on the main approach and show the second one as a commented-out code, with a corresponding comment to it. 

Also, here we can make another exception mentioned earlier and use capital letters for the code comment, to make it a bit more visible:

```python
✔️# Create a stem plot.plt.stem(months.index, months)# # ALTERNATIVE WAY TO CREATE A STEM PLOT.# plt.vlines(x=months.index, ymin=0, ymax=months)# plt.plot(months.index, months, 'o')
```

## Conclusion

All in all, code commenting is a handy technique for communicating the approaches we used for coding and the reasons behind them to other people . It improves the overall code readability and makes it easier to navigate between different logical blocks. 

To create meaningful code comments in Python, we have to follow simple and straightforward technical guidelines, keep in mind possible local company- or project-specific conventions, make our comments as laconic and informative as possible, update them in case of code modifications, and — the last but not the least — avoid overusing them.

Thanks for reading!
