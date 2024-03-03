import itertools
import random
import re


def generate_questions() -> list[str]:
    n = 4
    percents = (
        "Przekształć procent na ułamek dziesiętny",
        "Przekształć procent na ułamek zwykły w postaci licznik/mianownik",
    )
    inators = tuple(itertools.product(range(10), (1, 2, 4, 5, 8, 10)))
    questions = [
        *tuple(f"""Przekształć ułamek zwykły na procent <math xmlns="http://www.w3.org/1998/Math/MathML">
          <mfrac>
            <mn>{numerator}</mn>
            <mn>{denominator}</mn>
          </mfrac>
        </math>""" for numerator, denominator in random.sample(inators, k=n)),
        *tuple(f"""Przekształć ułamek dziesiętny na procent
          {str(round(numerator / denominator, 3)).replace('.', ',')}
        """ for numerator, denominator in random.sample(inators, k=n)),
        *tuple(f"""{percent}
          {str(round(numerator / denominator * 100, 3)).replace('.', ',').replace(',0', '')}%
        """ for numerator, denominator in random.sample(inators, k=n) for percent in percents),
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
        if "Przekształć procent na ułamek zwykły w postaci licznik/mianownik" in question:
            numbers = re.findall(r'[\d/\s]+', answer)[0]
            if '/' in numbers:
                numerator, denominator = map(int, numbers.split('/'))
            else:
                denominator = 1
                numerator = int(numbers)
            return round(float(re.findall(r'([\d\.]+)%', question)[0]) / 100, 9) == round(numerator / denominator, 9)
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = ['Przekształć ułamek zwykły na procent <math xmlns="http://www.w3.org/1998/Math/MathML">\n          <mfrac>\n            <mn>0</mn>\n            <mn>2</mn>\n          </mfrac>\n        </math>', 'Przekształć procent na ułamek zwykły w postaci licznik/mianownik\n          37,5%\n        ', 'Przekształć procent na ułamek zwykły w postaci licznik/mianownik\n          62,5%\n        ', 'Przekształć ułamek zwykły na procent <math xmlns="http://www.w3.org/1998/Math/MathML">\n          <mfrac>\n            <mn>9</mn>\n            <mn>2</mn>\n          </mfrac>\n        </math>', 'Przekształć ułamek zwykły na procent <math xmlns="http://www.w3.org/1998/Math/MathML">\n          <mfrac>\n            <mn>9</mn>\n            <mn>10</mn>\n          </mfrac>\n        </math>', 'Przekształć ułamek dziesiętny na procent\n          0,0\n        ', 'Przekształć procent na ułamek zwykły w postaci licznik/mianownik\n          100%\n        ', 'Przekształć ułamek dziesiętny na procent\n          1,0\n        ', 'Przekształć ułamek dziesiętny na procent\n          2,25\n        ', 'Przekształć procent na ułamek dziesiętny\n          62,5%\n        ', 'Przekształć ułamek dziesiętny na procent\n          0,8\n        ', 'Przekształć ułamek zwykły na procent <math xmlns="http://www.w3.org/1998/Math/MathML">\n          <mfrac>\n            <mn>2</mn>\n            <mn>10</mn>\n          </mfrac>\n        </math>', 'Przekształć procent na ułamek dziesiętny\n          100%\n        ', 'Przekształć procent na ułamek dziesiętny\n          37,5%\n        ', 'Przekształć procent na ułamek zwykły w postaci licznik/mianownik\n          120%\n        ', 'Przekształć procent na ułamek dziesiętny\n          120%\n        ']
    answers = ['0%', '3/8', '5/8', '450%', '90%', '0%', '1', '100%', '225%', '0,625', '80%', '20%', '1,0', '0,375', '12/10', '1.2']
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
