
# PyWordle

Popular wordle game made with python for terminal. Available in English and Spanish Languages. Word input comprogation with rae (Spanish) and dictionary.com (English).

## Run Locally

- Clone the project

    Using HTTPS:
    ```bash
    git clone https://github.com/mmedir00/PassManager.git
    ```
    Using SSH:
    ```bash
    git clone git@github.com:mmedir00/PassManager.git
    ```
- Go to the project directory

    ```bash
    cd PassManager
    ```
- Install python libraries
    ```bash
    pip3 install beautifulsoup4
    ```
- Start PyWordle

    ```bash
    python3 main.py
    ```

## Used technologies

 - [Python 3.10.12](https://www.python.org/downloads/release/python-31012/)
 - [random](https://docs.python.org/es/3.10/library/random.html)
 - [os](https://docs.python.org/3.10/library/os.html)
 - [requests](https://pypi.org/project/requests/)
## How to use

Is a basic text GUI, first ypu select the language, then you have to write down a 5 letter word which exist in the language you are playing with. You have 5 tries to guess the word. a letter in green means the letter is in right place, yellow means the letter is in the word but not in the correct place, grey means the word does not contain that letter.
Example (the word is ""):
![Use Example](https://raw.githubusercontent.com/mmedir00/PyWordle/main/etc/Example.png)