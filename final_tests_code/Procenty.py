import fractions
import itertools
import random
import re


def generate_questions() -> list[str]:
    n = 4
    percents = (
        "Przekształć procent na ułamek dziesiętny",
        "Przekształć procent na nieskracalny ułamek zwykły w postaci licznik/mianownik",
    )
    inators = tuple(itertools.product(range(10), (1, 2, 4, 5, 8, 10)))
    questions = [
        *tuple(f"""Przekształć ułamek zwykły na procent <math xmlns="http://www.w3.org/1998/Math/MathML">
          <mfrac>
            <mn>{nominator}</mn>
            <mn>{denominator}</mn>
          </mfrac>
        </math>""" for nominator, denominator in random.sample(inators, k=n)),
        *tuple(f"""Przekształć ułamek dziesiętny na procent
          {str(round(nominator / denominator, 3)).replace('.', ',')}
        """ for nominator, denominator in random.sample(inators, k=n)),
        *tuple(f"""{percent}
          {str(round(nominator / denominator * 100, 3)).replace('.', ',').replace(',0', '')}%
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
        if "Przekształć ułamek zwykły na procent" in question:
            numerator, denominator = map(int, re.findall(r'<mn>(\d+)</mn>', question))
            return round(float(answer), 9) == round(numerator / denominator * 100, 9)
        if "Przekształć ułamek dziesiętny na procent" in question:
            return round(float(re.findall(r'([\d.]+)\s', question)[0]) * 100, 5) == round(float(answer), 5)
        if "Przekształć procent na ułamek dziesiętny" in question:
            return round(float(re.findall(r'([\d.]+)%', question)[0]) / 100, 5) == round(float(answer), 5)
        if "Przekształć procent na nieskracalny ułamek zwykły w postaci licznik/mianownik" in question:
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
       '9/5',
       '40%',
       '25%',
       '0.7',
       '7/2',
       '1',
       '20%',
       '1',
       '1.8',
       '70%',
       '50%',
       '3.5',
       '75%',
       '50%',
       ]
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
