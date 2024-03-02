import itertools
import random
import re


def generate_questions() -> list[str]:
    n = 4
    questions = [
        *tuple(f"""<math xmlns="http://www.w3.org/1998/Math/MathML">
          <mfrac>
            <mn>{nominator}</mn>
            <mn>100</mn>
          </mfrac>
        </math>""" for nominator in random.sample(range(200), k=n)),
    ]
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        question = question.replace(',', '.')
        answer = answer.strip()
        if not answer.endswith('%') or answer.count('%') > 1:
            print("Answer doesn't and with percent")
            return False
        answer = answer.replace('%', '').replace(',', '.')
        nominator, denominator = map(int, re.findall(r'<mn>(\d+)</mn>', question))
        return round(float(answer), 9) == round(nominator / denominator * 100, 9)
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = generate_questions()
    answers = [
        '163%',
        ' 28%',
        '6 %',
        '189 % ',
    ]
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
