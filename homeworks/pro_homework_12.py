# Task 1
# Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, 
# за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
import re
def find_rb(text: str) -> str:
    """
    Function searches for "rbr" pattern in the text and returns it if is found.
    Only one "r" at the start and at the end is taken into account. Any abount of "b" is taken into account.
    Cases of the letters doesn't metter.
    """
    return re.findall(r"[Rr][Bb]+[Rr]", text)
#Если хотим находить только отдельные слова, то можно написать так: "\b[Rr][Bb]+[Rr]\b". И пробелы убрать отдельно...

# Task 2
# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re
def cc_number_validator(cc_number: str) -> bool:
    """
    Function performes a basic check of a bank card number validity.
    The number must start from 2, 3, 4, 5 and must contain from 13 to 19 digits overall.
    If valid, returns True. If not, returns False.
    """
    if re.match(r"^[2345]\d{12,18}$", cc_number):
        return True
    else:
        return False
#Т.к. банк карта может состоять из 13-19 цифр, я лично предпочел убрать дефисы. 
#Но, для большего соответствия заданию можно написать "^[2345]\d{3}-\d{4}-\d{4}-\d{4}$" 

# Task 3
# Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.
import re
def email_address_validator(email: str) -> bool:
    """
    Function checks if the email address matches the desired pattern. If yes, returns True. If not, returns False.
    Pattern:
    -letters (A-Z, a-z)
    -numbers (0-9)
    -underscore (_) only before "@"
    -dash (-) only before "@" and only ones
    -at (@)
    -dot (.) only in the domain part
    """
    email_pattern = r"^\w+([-]?\w+)*@[a-zA-Z0-9-]+\.[a-zA-Z]+$"
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Task 4
# Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.
import re
def login_correctness_validator(login: str) -> bool:
    """
    Function checks if the login matches the desired pattern. If yes, returns True. If not, returns False.
    Pattern:
    - letters (A-Z, a-z)
    - numbers (0-9)
    - overall length from 2 to 10 symbols
    """
    if re.match(r"^[a-zA-Z0-9]{2,10}$", login):
        return True
    else:
        return False