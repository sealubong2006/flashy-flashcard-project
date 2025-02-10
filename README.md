# Flashy - A French-English Flashcard App

## Overview

Flashy is a simple flashcard application built using Python and Tkinter. It helps users learn French words by displaying flashcards with a French word and its English translation after a delay. Users can mark words they already know, and these words will be removed from the learning deck.

## Features

- Displays French words and their English translations
- Auto-flip mechanism to show English translation after 3 seconds
- Users can mark words they know to remove them from the deck
- Saves progress by storing unknown words in a separate CSV file

## Installation

### Prerequisites

Ensure you have Python installed on your system. You also need the following Python libraries:

- `tkinter`
- `pandas`
- `random`

### Setup

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/flashy.git
   cd flashy
   ```
2. Install required dependencies:
   ```sh
   pip install pandas
   ```
3. Ensure you have the necessary dataset:
   - `french_words.csv` (located in `../flash-card-project-start/data/`)
   - If `words_to_learn.csv` exists, it will be used to track progress

## Usage

Run the script:

```sh
python main.py
```

### Controls

- ✅ (Checkmark) Button: Marks the word as known and removes it from the deck
- ❌ (Cross) Button: Keeps the word in the deck for future practice

## File Structure

- `flashcard.py` - Main program logic
- `french_words.csv` - Original dataset containing French-English words
- `words_to_learn.csv` - Progress tracking file (automatically created)
- `images/` - Contains UI images for flashcards and buttons

## Known Issues

- Ensure the image paths are correctly set based on your directory structure
- If `words_to_learn.csv` is missing, the app will start fresh with all words

## License

This project is open-source.

---

Feel free to contribute, improve, or customize the project to fit your needs!


https://github.com/user-attachments/assets/55d4d859-26a7-4878-9bbb-c225d3c38269




