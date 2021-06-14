def welcome_message():
  text = """
  *********************************************
  **  Welcome to Mad Libs! Mad Libs is a     **
  **  fill-in-the-blank word game. Type in   **
  **  a word satisfying the request and I    **
  **  will return a funny story for you.     **
  *********************************************
  """
  print(text)

welcome_message()

def read_file():
  with open('madlib_cli/example_text.txt') as example:
    return example.read()

content = read_file()
print(content)
