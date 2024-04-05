import fractions
import itertools
import random
import re


def generate_questions() -> list[str]:
    return [f"""<math xmlns="http://www.w3.org/1998/Math/MathML">
      <mrow>
        <mfrac>
          <mrow>
            <mn>{2 ** random.randint(0, 2) * 3 ** random.randint(0, 2) * 5 ** random.randint(0, 2) * 7 ** random.randint(0, 1) * 11 ** random.randint(0, 1)}</mn>
          </mrow>
          <mrow>
            <mn>{2 ** random.randint(0, 2) * 3 ** random.randint(0, 2) * 5 ** random.randint(0, 2) * 7 ** random.randint(0, 1) * 11 ** random.randint(0, 1)}</mn>
          </mrow>
        </mfrac>
      </mrow>
    </math>"""]


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        numerator, denominator = map(int, re.findall(r'<mn>(\d+)</mn>', question))
        if '/' in answer:
            answer_numerator, answer_denominator = map(int, answer.split('/'))
        else:
            answer_numerator = int(answer)
            answer_denominator = 1
        correct_answer = fractions.Fraction(numerator, denominator)
        return correct_answer.numerator == answer_numerator and correct_answer.denominator == answer_denominator
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(69)
    questions = generate_questions()
    answers = ['1/1155']
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
