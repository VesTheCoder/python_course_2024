#Task 1
user_text = input("Input your text: ")
while '  ' in user_text:
    user_text = user_text.replace('  ', ' ')
print(f"Corrected text: {user_text}")

#Task 2
import string
user_text = input("Input your text: ")
while string.punctuation in user_text:
    user_text = user_text.replace(string.punctuation, " ")
user_text_list = user_text.split()
print(f"words: {len(user_text_list)}")