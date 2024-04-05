import fractions
import itertools
import random
import re


def generate_questions() -> list[str]:
    questions = []
    for _ in range(3):
        numerator, denominator = map(str, random.sample(range(1, 100), k=2))
        questions.append(f"""Wskaż poprawną parę licznika i mianownika <math xmlns="http://www.w3.org/1998/Math/MathML">
          <mrow>
            <mfrac>
              <mrow>
                <mn>{numerator}</mn>
              </mrow>
              <mrow>
                <mn>{denominator}</mn>
              </mrow>
            </mfrac>
          </mrow>
        </math>""" + ",".join(random.sample((f"1) (licznik={numerator}, mianownik={denominator})", f"2) (licznik={denominator}, mianownik={numerator})"), k=2)))
    for _ in range(3):
        numerator, denominator = map(str, sorted(random.sample(range(1, 100), k=2), reverse=True))
        questions.append(f"""Określ czy ułamek jest właściwy czy niewłaściwy <math xmlns="http://www.w3.org/1998/Math/MathML">
          <mrow>
            <mfrac>
              <mrow>
                <mn>{numerator}</mn>
              </mrow>
              <mrow>
                <mn>{denominator}</mn>
              </mrow>
            </mfrac>
          </mrow>
        </math>""" + ",".join(random.sample(("1) Właściwy", "2) Niewłaściwy"), k=2)))
    return question


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
