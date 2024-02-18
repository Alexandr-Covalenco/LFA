Formal Languages & Finite Automata Coursework
Introduction to Formal Languages, Regular Grammars, and Finite Automata
Course: Formal Languages & Finite Automata
Authors: Cretu Dumitru with acknowledgments to Vasile Drumea and Irina Cojuhari
Overview
A formal language is a medium or format used to convey information from a sender to a receiver. The primary components of a language include:

The Alphabet: A set of valid characters.
The Vocabulary: A set of valid words.
The Grammar: A set of rules or constraints governing the language.
These components can be configured in an infinite number of ways, meaning that the design of a language's components should be tailored to its intended use case. This diversity in design preferences has led to the development of numerous natural, programming, and markup languages, each suited for similar or distinct purposes.

Objectives
Understand what constitutes a language and what is required for it to be considered a formal language.
Set up an initial project for ongoing coursework. This project can be approached as a series of separate tasks or lab works, each demonstrating understanding of specific topics. Alternatively, lab works can be stages in the development of a larger, cohesive project.
Getting Started
Create a GitHub repository to manage and update your project.
Select a programming language best suited for the tasks at hand, focusing on solving the core problem rather than peripheral issues (such as project setup and execution).
Organize reports to simplify the verification of your work.
Coursework Instructions
Based on your variant number, you will receive a grammar definition. Your tasks are as follows:

Implement a class/type for your grammar.
Develop a function to generate 5 valid strings from the language defined by your grammar.
Implement functionality to convert an object of type Grammar into one of type Finite Automaton.
For the Finite Automaton, add a method to check if an input string can be obtained via state transitions.
Implementation Details
This project includes Python code that defines a grammar and a finite automaton. The grammar is designed to generate strings that adhere to a specific pattern, and the finite automaton is used to verify if a given string can be derived from the grammar through state transitions.

Grammar Class: Contains methods for string generation based on the defined grammar rules.
Finite Automaton Class: Utilizes a regular expression matching the grammar to check if strings comply with the language.
