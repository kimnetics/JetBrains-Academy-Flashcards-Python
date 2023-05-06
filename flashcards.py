import argparse
import json
import os
import random

from io_logger import IoLogger

io_logger = IoLogger()

terms = {}
definitions = {}
mistakes = {}


def add_flashcard():
    prompt = f'The term for card:\n'
    while True:
        term = io_logger.input(prompt)
        if term not in terms:
            break
        prompt = 'The <term/definition> already exists. Try again:\n'

    prompt = f'The definition for card:\n'
    while True:
        definition = io_logger.input(prompt)
        if definition not in definitions:
            break
        prompt = 'The <term/definition> already exists. Try again:\n'

    # Add flashcard.
    terms[term] = definition
    definitions[definition] = term
    mistakes[term] = 0

    io_logger.print(f'The pair ("{term}":"{definition}") has been added.')


def remove_flashcard():
    term = io_logger.input('Which card?\n')

    # Remove flashcard if it exists.
    if term in terms:
        del mistakes[term]
        del definitions[terms[term]]
        del terms[term]
        io_logger.print('The card has been removed.')
    else:
        io_logger.print(f'Can\'t remove "{term}": there is no such card.')


def import_flashcards(file_name=None):
    if file_name is None:
        file_name = io_logger.input('File name:\n')

    # Exit if file does not exist.
    if not os.path.exists(file_name):
        io_logger.print('File not found.')
        return

    # Read flashcards from file.
    with open(file_name, 'r') as file:
        flashcards = json.load(file)

    # Add flashcards to those already in memory.
    length = 0
    for key, value in flashcards.items():
        if key == 'terms':
            length = len(value)
            for term, definition in value.items():
                terms[term] = definition
                definitions[definition] = term
        else:
            for term, count in value.items():
                mistakes[term] = count

    io_logger.print(f'{length} cards have been loaded.')


def export_flashcards(file_name=None):
    if file_name is None:
        file_name = io_logger.input('File name:\n')

    # Convert flashcards to json.
    flashcards_json = json.dumps({
        'terms': terms,
        'mistakes': mistakes
    }, indent=2)

    # Write flashcard json to file.
    with open(file_name, 'w') as file:
        file.write(flashcards_json)

    io_logger.print(f'{len(terms)} cards have been saved.')


def ask_questions():
    number_of_questions = int(io_logger.input('How many times to ask?\n'))

    # Ask number of questions requested.
    for i in range(0, number_of_questions):
        # Choose random question.
        term, definition = random.choice(list(terms.items()))

        answer = io_logger.input(f'Print the definition of "{term}":\n')

        if answer == definition:
            io_logger.print('Correct!')
        else:
            # Increment mistake count for question.
            mistakes[term] += 1

            if answer in definitions:
                io_logger.print(
                    f'Wrong. The right answer is "{definition}", but your definition is correct for "{definitions[answer]}".')
            else:
                io_logger.print(f'Wrong. The right answer is "{definition}".')


def print_hardest():
    # Find highest mistake count.
    highest_count = 0
    for term, count in mistakes.items():
        if count > highest_count:
            highest_count = count

    if highest_count == 0:
        io_logger.print('There are no cards with errors.')
        return

    # Make list of flashcards with highest mistake count.
    hardest_flashcards_list = []
    for term, count in mistakes.items():
        if count == highest_count:
            hardest_flashcards_list.append(term)

    hardest_flashcards = ', '.join([f'"{term}"' for term in hardest_flashcards_list])
    if len(hardest_flashcards_list) > 1:
        io_logger.print(f'The hardest cards are {hardest_flashcards}. You have {highest_count} errors answering them.')
    else:
        io_logger.print(f'The hardest card is {hardest_flashcards}. You have {highest_count} errors answering it.')


def reset_stats():
    for term, count in mistakes.items():
        mistakes[term] = 0

    io_logger.print('Card statistics have been reset.')


def main():
    # Parse command line arguments.
    parser = argparse.ArgumentParser(prog='Flashcards')
    parser.add_argument('-i', '--import_from', dest='import_file')
    parser.add_argument('-e', '--export_to', dest='export_file')
    args = parser.parse_args()

    # Import flashcards if file was specified.
    if args.import_file is not None:
        import_flashcards(args.import_file)

    # Loop until user chooses exit action.
    while True:
        action = io_logger.input(
            'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
        action.strip().lower()
        if action == 'add':
            add_flashcard()
        elif action == 'remove':
            remove_flashcard()
        elif action == 'import':
            import_flashcards()
        elif action == 'export':
            export_flashcards()
        elif action == 'ask':
            ask_questions()
        elif action == 'exit':
            break
        elif action == 'log':
            io_logger.save_log()
        elif action == 'hardest card':
            print_hardest()
        elif action == 'reset stats':
            reset_stats()
        else:
            io_logger.print(f'Invalid action "{action}".')

    # Export flashcards if file was specified.
    if args.export_file is not None:
        export_flashcards(args.export_file)

    io_logger.print('Bye bye!')


main()
