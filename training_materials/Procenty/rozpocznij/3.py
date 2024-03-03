import itertools
import random
import re


def generate_questions() -> list[str]:
    n = 3
    percents = (
        "Przekształć procent na ułamek dziesiętny",
    )
    inators = tuple(itertools.product(range(10), (1, 2, 4, 5, 8, 10)))
    questions = [
        *tuple(f"""Przekształć ułamek dziesiętny na procent
          {str(random.randint(0, 200) / 100).replace('.', ',')}
        """ for _ in range(n)),
        *tuple(f"""{percent}
          {str(round(nominator / denominator * 100)).replace('.', ',').replace(',0', '')}%
        """ for nominator, denominator in random.sample(inators, k=n) for percent in percents),
    ]
    random.shuffle(questions)
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        question = question.replace(',', '.')
        answer = answer.strip()
        if "na procent" in question and (not answer.endswith('%') or answer.count('%') > 1):
            print("Answer doesn't and with percent")
            return False
        answer = answer.replace('%', '').replace(',', '.')
        if "Przekształć ułamek dziesiętny na procent" in question:
            return round(float(re.findall(r'([\d.]+)\s', question)[0]) * 100, 5) == round(float(answer), 5)
        if "Przekształć procent na ułamek dziesiętny" in question:
            return round(float(re.findall(r'([\d.]+)%', question)[0]) / 100, 5) == round(float(answer), 5)
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = generate_questions()
    answers = [
        '70%',
        '0,25',
        '0%',
        '75%',
        '0.2',
        '0.5',
        '0.4',
        '50%',
        ]
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
