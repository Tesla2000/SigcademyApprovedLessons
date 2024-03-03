import itertools
import random
import re
import fractions


def generate_questions() -> list[str]:
    n = 6
    inators = tuple(itertools.product(range(10), (1, 2, 4, 5, 8, 10)))
    questions = [
        *tuple(f"""
          {str(round(nominator / denominator * 100)).replace('.', ',').replace(',0', '')}%
        """ for nominator, denominator in random.sample(inators, k=n)),
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
        question_fraction = fractions.Fraction(int(re.findall(r'(\d+)%', question)[0]), 100)
        return question_fraction.numerator == numerator and question_fraction.denominator == denominator
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = generate_questions()
    answers = [
        "3/4",
        "1/2",
        "0",
        "7/10",
        "2/10",
        "4/10",
    ]
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
