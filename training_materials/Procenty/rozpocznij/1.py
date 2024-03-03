import itertools
import random
import re


def generate_questions() -> list[str]:
    n = 4
    questions = [
        *tuple(f"""{percent}%""" for percent in random.sample(range(200), k=n)),
    ]
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        question = question.replace(',', '.')
        answer = answer.strip()
        answer = answer.replace('%', '').replace(',', '.')
        numbers = re.findall(r'[\d/\s]+', answer)[0]
        if '/' in numbers:
            nominator, denominator = map(int, numbers.split('/'))
        else:
            denominator = 1
            nominator = int(numbers)
        return round(float(re.findall(r'([\d\.]+)%', question)[0]) / 100, 9) == round(nominator / denominator, 9)
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = generate_questions()
    answers = [
        '163/100',
        '28/100',
        '6/100',
        '189/100',
    ]
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
