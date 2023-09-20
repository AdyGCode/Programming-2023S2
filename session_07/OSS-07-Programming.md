[[OSS-06-Programming]] [[OSS-08-Programming]]
## Communications

- MS Teams
- eMail (online@screencraft.net.au)


## Useful Links
https://diigo.com/profile/ady_gould

# Questions?!

Get them questions ready!
Subject / Topic  and the question itself 😊
- ICTPRG302 / Assessments - ....
- SaaS / Project - ...

### What Week?
> Need to check, what week are we in? 😅 🤔

Session 07 aka Week 07 aka 06 September 2023 aka somewhere about 3/4 way through the year...
### Deadlines
> The extra week for online. 
> Does that apply to the due dates on the assignments themselves or just the dates on Blackboard?

Yes, in general add an extra TAFE week to the deadline for an assessment
When possible Blackboard takes priority, but if LAP says later then take the later session.
If in doubt - ask the subject lecturer via online@screencraft.net.au

All assessments and resubmissions must be completed by session 19/20.

### ICTPRG302 - Portfolio Part 1
> Question - I submitted my assignment for portfolio pt 1. I had to amend one question. I did update and email as blackboard submission wasn't available. Has everyone rec'd their grades ?
> ..
> ICTPRG302/Assessments - I also didn't have an option to re-submit part 1 of the portfolio assessment, but by the time I received the feedback I had finished the whole portfolio so I just made the adjustments to that and submitted. Is there any need to find a way to re-submit part 1 or is it fine as long as I've submitted the final portfolio?
> ...
> At the start of the unit I think I remember us being told part 1 was just like a check to make sure we were on the right track, and it's the full portfolio that we're graded on. So maybe there's no need to re-submit and we just take the feedback into account for the final submission?

1st submission - is a progress point
Feedback to be used to improve the final submission

- naming of variables
	- snake case
	- meaningful != a, i , j 
	- meaningful == letter_position

### ICTPRG302 Project
> I missed last week session, did we go through the project Wordle requirement yet? Is it due this week? thanks
### AGILE development and Projects
> could you tell us about AGILE development methodology in practice? Can I apply it in the Wordle project implementation?

To Do List
- a list of features to implement

### Recommended Command Prompt Applications
- Terminal from Laragon (free, and part of the Laragon installation)
- Windows Terminal (free)

### Python and Python Virtual Environments
Open the terminal / command prompt
Change into the folder with your python project using a command of the form:
```shell
cd FOLDER_NAME
```
> `FOLDER_NAME` is the name of the folder with the project in.

For example, if your files were in a folder `Source\Repos` in your main User Profile folder, then we can use:
```shell
cd %userprofile%
cd Source
cd Repos
```
or in one statement:
```shell
cd %userprofile%\Source\Repos
```
If you do not have a project folder then you can create it using a command of the form:
```shell
mkdir PROJECT_NAME
```
For example, `PROJECT_NAME` could be `python_venv_demo`:
```shell
mkdir python_venv_demo
```
Now move into this folder:
```shell
cd FOLDER_NAME
```
Which would be (for our example folder):
```shell
cd python_venv_demo
```

Now execute the following command to install the Python Virtual Environment package in your user packages:
```shell
pip install virtualenv
```
or
```shell
python -m pip install virtualenv
```

You are ready to create the virtual environment.
Execute the following:
```shell
python -m venv VENV_FOLDER_NAME
```
Replace the `VENV_FOLDER_NAME` with a folder name such as `venv`, `venv_home`, or similar.
```shell
python -m venv venv_home
```

You are now ready to activate the virtual environment:
```shell
.\VENV_FOLDER_NAME\Scripts\activate.bat
```
Which for our example will be:
```shell
.\venv_home\Scripts\activate.bat
```
### Python and Packages

To add a package to the virtual environment, use the `pip install` command **AFTER** activating the virtual environment.

### Python and Coloured Output






 