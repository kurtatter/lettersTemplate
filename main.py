import string
from pathlib import Path

import settings
from scheme import LetterData


def create_folder_for_letters(folder_name: str) -> Path:
    current_path = Path().resolve()
    letters = current_path / Path(folder_name)

    if not letters.exists():
        letters.mkdir()
    return letters


def main(letters_folder: Path):
    with open(settings.LETTER_TEMPLATE_FILENAME) as letter:
        letter_template = string.Template(letter.read())

        with open(settings.LETTER_DATA_FILENAME) as data:
            users = LetterData.parse_raw(data.read())
            for user in users.users:
                letter_text = letter_template.safe_substitute(user.dict())

                letter_name = letters_folder / ('-'.join(user.fullname.split()) + '.txt')
                with open(letter_name, 'w') as new_letter:
                    new_letter.write(letter_text)


if __name__ == '__main__':
    new_letters_folder = create_folder_for_letters(settings.LETTERS_FOLDER_NAME)
    main(new_letters_folder)
