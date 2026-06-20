Feature: Placement Preparation Assistant

Scenario: Resume analysis

Given a student uploads a resume

When Resume Agent processes the file

Then personal information should be masked

And improvement suggestions should be generated

------------------------------------------------

Scenario: DSA roadmap generation

Given the student targets Software Engineering

When DSA Agent evaluates current skills

Then a 6 week roadmap should be created

------------------------------------------------

Scenario: Interview preparation

Given the student selects Backend Developer

When Interview Agent is invoked

Then role specific interview questions should be generated

------------------------------------------------

Scenario: Study scheduling

Given a roadmap exists

When Scheduler Agent runs

Then calendar events should be created

------------------------------------------------

Scenario: Progress tracking

Given tasks are completed

When Progress Agent updates records

Then readiness score should increase