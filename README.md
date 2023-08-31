# Questioner Quiz (p3-geographyq)
(Welcome to the Geography Quiz!)

Questioner Quiz is an interactive quiz application that challenges users with a variety of questions on different topics. The application is designed to engage users, test their knowledge, and provide an enjoyable learning experience.

**Developer:** [Anwar Dawoud]
![Questioner Quiz](/assets/images-readme/responsive.png)

![Questioner Quiz](/assets/images-readme/Run-py.png)
## Table of Contents
- [Introduction](#introduction)
- [Live Website](#live-website)
- [Project Goals](#project-goals)
- [User Goals](#user-goals)
- [Features](#features)
- [User Experience](#user-experience)
- [Target Audience](#target-audience)
- [User Requirements and Expectations](#user-requirements-and-expectations)
- [Technical Design](#technical-design)
   - [Design](#design "Design")
     - [Mock-up](#mock-up "Wireframes")
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## Introduction

Questioner Quiz is a web-based quiz application that allows users to answer a variety of questions on different subjects and topics. The application aims to provide an interactive and educational experience for users of all ages.

## Live Website

Visit the live version of the Questioner Quiz application: [Questioner Quiz](https://p3-geographyq-6840663e050c.herokuapp.com/)

[Back to top](<#table-of-contents>)

## Project Goals

The primary goal of this project is to create an engaging quiz platform that allows users to test their knowledge and learn new facts on various subjects.

## User Goals

The application users are looking to:
- Challenge themselves with a variety of questions.
- Test their knowledge in different areas.
- Have a fun and enjoyable experience while learning.

## Features

The Questioner Quiz application includes the following features:
- Randomized Questions for Each Attempt
- Real-time Feedback on Correct and Incorrect Answers
- Progress Tracking and Score Display
- User-friendly Interface for Easy Navigation

## User Experience

### Target Audience
- Students seeking to reinforce their knowledge.
- Trivia enthusiasts looking for a challenge.
- Anyone interested in learning new facts and information.

[Back to top](<#table-of-contents>)

### User Requirements and Expectations

#### User Stories
1. As a user, I want to answer a variety of questions to test my knowledge.
2. As a user, I want to receive real-time feedback on whether my answers are correct or incorrect.
3. As a user, I want to track my progress and see my overall score.
4. As a user, I want to have a user-friendly interface that is easy to navigate.

[Back to top](<#table-of-contents>)

## Technical Design
### Design
#### Mock-up:
![App functionality Wireframe](/assets/images-readme/Structure-Mockup.png)

### Flowchart
- Display Randomized Questions
- Answer Questions
- Calculate Score
- Display Results

[Back to top](<#table-of-contents>)

### Technologies Used
   #### Main Language
       Python

   #### Frameworks & Libraries
- [IDLE]  is Python's Integrated Development.

- [Codeanywhere](https://app.codeanywhere.com/) - used as the coding environment.

- [GitHub](https://github.com/) - to store the repository for submission.

- [Balsamiq](https://balsamiq.cloud/s2xhbvy/pew66um/r6E13) - to create the mock-up in preparation for the project.

- [Heroku](https://id.heroku.com/) - to deploy the live version of the terminal.

- [AmIResponsive](https://ui.dev/amiresponsive?url=https://hangmangame-pp3-python-d5764adc1207.herokuapp.com/) - the responsive preview image at the top of the README.md. 

- Random - to randomize the choices of the computer player.

- HTML, CSS (for frontend styling).

- JavaScript (for interactivity).

[Back to top](<#table-of-contents>)

#### Deployment
- Heroku (for hosting)

## Testing
### Validator Testing
* [CI PEP8 Online](https://pep8ci.herokuapp.com/). 
   * No errors were returned.
![PEP8 CI Validation](/assets/images-readme/pep8.png)

* [Python syntax checker Online](https://extendsclass.com/python-tester.html).
  *No syntax errors detected :)
![Questioner Quiz](/assets/images-readme/extendsclass.com-python-tester.png)

[Back to top](<#table-of-contents>)

### User Stories Testing
1. Answering Questions:
   - User can answer questions to test their knowledge.

2. Real-time Feedback:
   - User receives instant feedback on correct and incorrect answers.

3. Progress Tracking and Score:
   - User's progress is updated as they answer questions.
   - User's score is displayed at the end of the quiz.

4. User-friendly Interface:
   - The application provides an intuitive and easy-to-navigate interface.

[Back to top](<#table-of-contents>)

## Bugs

- Bug: [Incorrect score calculation for certain question types]
  - Fix: [Updated the scoring algorithm to correctly calculate scores based on the question type and user's response.]

- Bug: [Score not updating after completing the quiz.]
  - Fix: [Debugged the score calculation function and ensured that the final score is displayed accurately.]

### Remaining Bugs
* No bugs remaining so far.

[Back to top](<#table-of-contents>)

## Deployment

### Version Control
The version control was maintained using git within Visual Studio Code to push code to the main repository.

 * From the VS Code terminal type `"git add ."`, to make changes and/or updates to the files.

 * Type `"git commit -m (insert a short descriptive text)"`, which commits the changes and updates the files.

 * Use the `"git push"` command, which pushes the committed changes to the main repository. 

 ### Page Deployment
 The app was deployed to Heroku CLI. The steps to deploy are as follows:

 * After creating an account and logging in, click `"New"` to create a new app from the dashboard.
 * Create a unique name for the app and select my region; press `"Create app"`.
 * Go to `"Settings"` and navigate to `Config Vars`.
 * Add Config Vars. 
   * For this app was only used: `KEY` = `PORT` : `VALUE` = `8000`.
 * Add buildpacks `Python` and `NodeJS` - in this order.
 * Click the `Deploy Branch`.
 * Scroll Down to Deployment Method and select GitHub.
 * Select the repository to be deployed and connect to Heroku.
 * Scroll down to deploy: 
    * `Option 1` is selecting Automatic deploys (Will Update Automatically with every "git push"). This was chosen for this project.

 * Live deployment [Questioner Quiz](https://p3-geographyq-6840663e050c.herokuapp.com/)

[Back to top](<#table-of-contents>)
## Credits
- [Codeinstiute] (https://learn.codeinstitute.net/courses/course)

## Acknowledgments

- My mentor [Jack W] - for his guidance and feedback.
- My brother [Ahmed Dawoud] - his experience over 15 years as a developer. 
- Slack-peer-code-review [Karolis_5P & Carl Murray_5P] - for there recommendations
- My family [Larysa Dawoud & kids] - for Given me a space to work on current project. 
---
