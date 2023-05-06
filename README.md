# JetBrains Academy Flashcards (Python) Project

An example of a passing solution to the final phase of the JetBrains Academy Python Flashcards (Python) project.

## Description

This project is a command line application which allows a user to build a deck of flashcards. Each flashcard has a term and a definition.

Decks of flashcards may be loaded from and saved to files. This may be done through both command line arguments and run time commands.

The application can quiz the user by presenting a term and asking for its definition.

The application tracks the number of wrong answers for each term so that it can display the hardest term.

The application records all inputs and outputs and may be commanded to save these values to a file.

## Notes

The relative directory structure was kept the same as the one used in my JetBrains Academy solution.

The `--import_from=` command line argument allows specifying a flashcard data file name which will be read during application start up.

The `--export_to=` command line argument allows specifying a flashcard data file name which will be saved to during application shut down.

Here is an example session:

(User entered items were given a '> ' prefix, which did not actually show in the console.)

```
> python flashcards.py
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The term for card:
> dog
The definition for card:
> barks
The pair ("dog":"barks") has been added.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The term for card:
> cat
The definition for card:
> meows
The pair ("cat":"meows") has been added.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The term for card:
> turkey
The definition for card:
> gobbles
The pair ("turkey":"gobbles") has been added.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> ask
How many times to ask?
> 4
Print the definition of "cat":
> meows
Correct!
Print the definition of "turkey":
> barks
Wrong. The right answer is "gobbles", but your definition is correct for "dog".
Print the definition of "cat":
> moos
Wrong. The right answer is "meows".
Print the definition of "turkey":
> gobbles
Correct!
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> export
File name:
> flashcards.json
3 cards have been saved.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
The hardest cards are "cat", "turkey". You have 1 errors answering them.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> log
File name:
> log.txt
The log has been saved.
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> exit
Bye bye!
```

For the most part, the wording was specified in the requirements and is being checked for by automated testing. There is not a lot of latitude to change the wording.
