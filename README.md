Welcome to REGEX-TEXT-Search! 🎉

Hey there, regex wizard!🧙‍♂️👋 Ready to hunt down patterns in text like a pro? This Python project, search.py, is your trusty sidekick for searching text using regular expressions. It converts a regex pattern into a postfix expression, builds an NFA, converts it to a DFA, and then uses that DFA to find matches in either a file or a chunk of text. Sounds cool, right? Let’s dive into what this project does and how you can use it!
What’s This Project About? 🤔
This project is a regular expression matcher that searches for patterns in text. It’s like a super-powered "Find" tool! Here’s the magic it performs:

Regex to Postfix: Converts your regular expression into postfix notation (e.g., ab| becomes ab|).
NFA Construction: Builds a Non-deterministic Finite Automaton (NFA) from the postfix expression.
NFA to DFA: Transforms the NFA into a Deterministic Finite Automaton (DFA) for faster matching.
Text Search: Searches for matches in either a file or a string, returning the locations and matched text.

It supports basic regex operations like:

Concatenation (e.g., ab for "a followed by b")
Alternation (e.g., a|b for "a or b")
Kleene Star (e.g., a* for "zero or more a’s")

Getting Started 🚀
Prerequisites
You’ll need:

Python 3.x installed (who doesn’t have Python these days? 😄)
No external libraries required—pure Python goodness!

How to Run It

Clone or Download: Grab this repository and make sure search.py is in your working directory.
Run the Script: Open your terminal and run:python search.py


Follow the Prompts:
Choose your mode: 1 to search in a file or 2 to search in a text string.
Enter your regular expression (e.g., a|b, ab*, or (ab)*c).
If searching a file, provide the file path. If searching text, type in your text string.


See the Results: The script will show you where matches are found (line/column for files, index for text) and what matched.

Example Usage
Let’s say you want to find all instances of cat|dog in a file called pets.txt.

Run the script:python search.py


Enter:
Mode: 1
Regex: cat|dog
File path: pets.txt


If pets.txt contains:I have a cat and a dog.
Cats are cool.

You’ll see output like:Match at line 1, column 9: 'cat'
Match at line 1, column 19: 'dog'
Match at line 2, column 0: 'cat'



Try it with a text string too! For mode 2, input cat|dog and text like I love my cat and dog, and it’ll point out the matches.
Code Breakdown 🛠️
Here’s a quick peek at what’s under the hood:

Regex to Postfix: Converts regex to postfix for easier processing (e.g., ab* → ab*).
NFA Construction: Builds an NFA with states and transitions (epsilon transitions included!).
NFA to DFA: Converts the NFA to a DFA for efficient matching.
Search Logic: Uses the DFA to scan text or files and report matches.
Main Function: Ties it all together with a user-friendly interface.

The code is in search.py, and it’s all vanilla Python—no dependencies needed!
Tips for Using Regex 🧙‍♂️

Use | for "or" (e.g., a|b matches "a" or "b").
Use * for "zero or more" (e.g., a* matches "", "a", "aa", etc.).
Use parentheses for grouping (e.g., (ab)* matches "", "ab", "abab", etc.).
The script automatically adds concatenation dots (.) where needed, so ab is treated as a.b.

Limitations (Nobody’s Perfect! 😅)

Supports basic regex operations (|, *, concatenation, and parentheses). Advanced features like + or ? aren’t supported yet.
File searches assume text files (.txt) with readable content.
Matches are non-overlapping by default (e.g., in aaa with regex a*, it won’t report overlapping matches).

Want to Contribute? 🌟
Got ideas to make this even cooler? Feel free to:

Add support for more regex features (+, ?, character classes, etc.).
Improve the output format (maybe a fancier display?).
Optimize the DFA for super speedy searches.

Fork the repo, make your changes, and send a pull request! Let’s make this regex matcher the best it can be. 😎
Issues or Questions? 🐛
If something’s not working or you’re confused, open an issue on the repository, and I’ll try to help (or at least offer moral support 😄).
Happy pattern matching! 🎯
