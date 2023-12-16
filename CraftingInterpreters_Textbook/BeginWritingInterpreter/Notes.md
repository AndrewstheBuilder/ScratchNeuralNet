## High Level Overview ?
### Scanning
- the first step in any compiler or parser is the scanning portion. It takes in the raw source code and converts it into "**tokens**". These are the meaningful "words" and "punctuation" of that make up the languages grammer.
- Scanning is a good starting point for me learning as well because it isn't very hard it involves a switch statement mostly.
- Error handling happens here too. If you care about making a language that's actually useful then error handling is a big part of it.
  - Its good engineering practice to separate the code that generates the error vs. the code that reports them.
- ![Alt text](image.png)
- a **lexeme** is the smallest sequence that can still represent something.
- However the lexemes are still the raw source code when we process groping character sequences into lexemes we stumble upon other useful information. When we take the lexeme and bundle it together with that information we get **tokens**
- The core of the scanner is a loop.
- **Lexical Grammer**: the rules(regex) that determines how the raw source code gets lexemized
  - There are tools like Lex and Flex that will spit out a complete scanner for you if you throw a handful of regexes at it.
- Engineering strategy for handling comments. Keep eating characters in a while loop until you see the end of the line.
- **Important**: Everytime the scanner goes to the next character there is a postfix ++ operator so its reading the character at the current value then incrementing the counter to the next.
  - So as we are scanning the current letter there is also a way to see the next letter without incrementing the counter.
  - current is the counter that keeps track of the current **unconsumed** character
- Lox supports multiline strings. ![Alt text](image-1.png)
- **Maximal Munch**: When two lexical grammer rules can both match a chunk of code that the scanner is looking at, *whichever one matches the most characters wins*
  - Example reserved keyword **or** and variable name **orchid**
### Parsing (Expressions)
- Converting the tokens from the scanning portion into a **syntax tree**
### Evaluating Code (Expressions)
- We are going to **execute** the syntax tree itself.
- Language implementations can make a computer do what the source code commands by compiling it to machine code, transpiling it by converting it to another high-level language, or reduce it some bytecode format for a virtual machine to run.
### Representing Code
#### Context Free Grammer
- We used regular expressions to identify the lexemes in the last chapter. Now we have to use context free grammer to handle expressions which can be nested arbitrarily deep.
- How can we define a grammer with infinite variations we define a finite set of rules.
#### Rules for Grammer
- The language that you produce from the rules of the grammer are called derivations.
- Rules are called productions because they produce the things you see in the grammer.
- **Terminal**: Are the literals from the language. For example for us it would be like *if* or *1234*
- **Non-Terminal**: is a named reference to another rule in the grammer.
- All language rules are basically derivations of the BNF form from the 20th century. Not much innovation has happened in this area since then.