import fractions
import itertools
import random
import re


def generate_questions() -> list[str]:
    n = 6
    questions = [
        f"""<math xmlns="http://www.w3.org/1998/Math/MathML">
          <mfrac>
            <mn>{(2 ** random.randint(0, 2)) * (3 ** random.randint(0, 2)) * (5 ** random.randint(0, 2)) * random.randint(0, 10)}</mn>
            <mn>{(2 ** random.randint(0, 2)) * (3 ** random.randint(0, 2)) * (5 ** random.randint(0, 2)) * random.randint(1, 10)}</mn>
          </mfrac>
        </math>""" for _ in range(n)
    ]
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        numbers = re.findall(r'[\d/\s]+', answer)[0]
        if '/' in numbers:
            numerator, denominator = map(int, numbers.split('/'))
        else:
            denominator = 1
            numerator = int(numbers)
        question_fraction = fractions.Fraction(*tuple(map(int, re.findall(r'<mn>(\d+)</mn>', question))))
        return question_fraction.numerator == numerator and question_fraction.denominator == denominator
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = generate_questions()
    answers = [
        '8',
        '75',
        '1/50',
        '72',
        '1/2',
        '2/25',
    ]
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
