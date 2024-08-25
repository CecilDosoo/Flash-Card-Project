# Flash Card Project

This project is an online version of flashcards designed to help users learn French vocabulary. The flashcards display a French word on the front, and when flipped, reveal the English translation on the back. Users can interact with the flashcards through a graphical interface, marking words as known or unknown.

## Features

- **Interactive Learning**: Users can mark whether they know the word by pressing the "check" button or the "wrong" button. 
- **Progress Tracking**: Words marked as known will be removed from the list of words to learn, ensuring that only unknown words are repeated.
- **Automatic Flipping**: The flashcards automatically flip after 3 seconds to show the English translation.

## Technologies Used

- **Python**: Core logic for the application.
- **Tkinter**: Provides the graphical user interface (GUI), including the screen, labels, and buttons for user interaction.
- **Pandas**: Handles reading and manipulating the CSV data files containing the vocabulary words.

## How It Works

### Main Functionalities

1. **is_known() Function**:
   - Removes the current word pair from the `to_learn` list when the user knows the word.
   - Saves the updated list to `words_to_learn.csv`.
   - Displays the next flashcard.

2. **flip_card() Function**:
   - Flips the card to reveal the English translation after 3 seconds.
   - Changes the text color to white and updates the displayed text to English.

3. **next_card() Function**:
   - Selects the next random word pair from the `to_learn` list.
   - Updates the card display to show the French word.
   - Resets the timer to flip the card after 3 seconds.

### GUI Setup

- **Window Configuration**:
  - Creates the main application window with a specific title, padding, and background color.
  
- **Image and Button Setup**:
  - Loads the front and back card images, as well as the right and wrong buttons.
  - Configures a canvas to display the flashcards, with a text area for the language and the word.
  - Adds "wrong" and "right" buttons, which trigger `next_card()` and `is_known()` respectively.
