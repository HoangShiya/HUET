import re
import time

"""
Handle_file
Input: Telex.
Output: Telex (Vietnamese without accents, lower and replace spaces with dashes)

EX:
Input: Việt Nam.
Output: viet-nam

@ Ideal:
STEP 1: Remove punctuation marks at the end of sentences
STEP 2: Convert Vietnamese with accents to unsigned
STEP 3: Convert uppercase to lowercase
STEP 4: Replace spaces with dashes
"""


def remove_punctuation_marks_at_the_end_of_sentences(st):
    new_st = st[:-1]
    return new_st

# The accents are in vowels: A, E, O, I, U, Y and special case are "đ" and "Đ" to "d" and "D"
def convert_Vietnamese_with_accents_to_unsigned(st):
    st = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', st)
    st = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', st)
    st = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', st)
    st = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', st)
    st = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', st)
    st = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', st)
    st = re.sub(r'[ìíịỉĩ]', 'i', st)
    st = re.sub(r'[ÌÍỊỈĨ]', 'I', st)
    st = re.sub(r'[ùúụủũưừứựửữ]', 'u', st)
    st = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', st)
    st = re.sub(r'[ỳýỵỷỹ]', 'y', st)
    st = re.sub(r'[ỲÝỴỶỸ]', 'Y', st)
    st = re.sub(r'[Đ]', 'D', st)
    st = re.sub(r'[đ]', 'd', st)
    return st

def convert_uppercase_to_lowercase(st):
    new_st = st.lower()
    return new_st

def replace_spaces_with_dashes(st):
    new_st = st.replace(" ", "-")
    return new_st

def handle_string(st):
    step_1 = remove_punctuation_marks_at_the_end_of_sentences(st)
    step_2 = convert_Vietnamese_with_accents_to_unsigned(step_1)
    step_3 = convert_uppercase_to_lowercase(step_2)
    step_4 = replace_spaces_with_dashes(step_3)
    new_st = step_4
    return new_st


def main():
    value_input = input("Mời bạn nhập chuỗi (Mode: Telex.): ")
    time.sleep(0.5)
    print("Đang tiến hành xử lí chuỗi...")
    time.sleep(1)

    # Initialize variable for handle string
    value_handle = handle_string(value_input)

    print("-----CHUỖI ĐÃ XỬ LÍ XONG-----")
    time.sleep(0.5)
    print(f"Chuỗi ban đầu: {value_input}")
    print(f"Chuỗi sau khi được xử lí: {value_handle}")


if __name__ == "__main__":
    main()


