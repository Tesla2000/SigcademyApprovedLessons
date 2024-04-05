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
        </math></br>1) """ + "</br>2) ".join(random.sample((f"(licznik={numerator}, mianownik={denominator})", f"(licznik={denominator}, mianownik={numerator})"), k=2)))
    for _ in range(3):
        numerator, denominator = sorted(random.sample(range(1, 100), k=2), reverse=True)
        fraction = f"""<mn>{numerator // denominator}</mn>
          <mfrac>
            <mn>{numerator % denominator}</mn>
            <mn>{denominator}</mn>
          </mfrac>""" if random.random() < .5 else f"<mfrac><mn>{numerator}</mn><mn>{denominator}</mn></mfrac>"
        questions.append(f"""Określ czy ułamek jest właściwy czy niewłaściwy <math xmlns="http://www.w3.org/1998/Math/MathML">
        {fraction}
        </math></br>1) Właściwy</br>2) Niewłaściwy""")
    random.shuffle(questions)
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        if re.findall(r"=\d", question):
            numerator, denominator = map(int, re.findall(r'<mn>(\d+)</mn>', question))
            answer_numerator1, answer_denominator1, answer_numerator2, answer_denominator2 = map(int, re.findall(r'=(\d+)', question))
            is_answer_1 = answer.startswith("1")
            return (numerator, denominator) == ((answer_numerator1 if is_answer_1 else answer_numerator2), (answer_denominator1 if is_answer_1 else answer_denominator2))
        else:
            is_answer_proper = answer.startswith("1")
            is_question_proper = len(re.findall("<mn>", question)) == 3
            return not (is_answer_proper ^ is_question_proper)
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    random.seed(42)
    questions = generate_questions()
    answers = ['1', '1', '1', '1', '2', '2']
    for question, answer in itertools.zip_longest(questions, answers, fillvalue=''):
        print(question)
        assert generate_answers(question, answer, '')
