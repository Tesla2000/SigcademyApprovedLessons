import itertools
import random
import re


def generate_questions() -> list[str]:
    n_factors = 10
    n_quotients = 0
    quotients = set()
    factors = random.sample(tuple(itertools.combinations_with_replacement(range(0, 6), 2)), n_factors)
    factors = tuple((elem1, elem2) if int(random.random()) else (elem2, elem1) for (elem1, elem2) in factors)
    while len(quotients) < n_quotients:
        quotients.add((random.randint(0, 10) * (divisor := random.randint(1, 10)), divisor))
    questions = [
        *tuple(f"""<math xmlns="http://www.w3.org/1998/Math/MathML">
              <mrow>
                <mn>{factor[0]}</mn>
                <mo>&#x22C5;</mo>
                <mn>{factor[1]}</mn>
                <mo>=</mo>
              </mrow>
            </math>""" for factor in factors),
        *tuple(f"""<math xmlns="http://www.w3.org/1998/Math/MathML">
              <mrow>
                <mn>{quotient[0]}</mn>
                <mo>:</mo>
                <mn>{quotient[1]}</mn>
                <mo>=</mo>
              </mrow>
            </math>""" for quotient in quotients),
    ]
    random.shuffle(questions)
    questions = list(itertools.starmap("{}. {}".format, enumerate(questions, 1)))
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        element1, element2 = map(int, re.findall(r'<mn>(\d+)</mn>', question))
        return element1 * element2 == int(answer)
    except Exception as e:
        print(e)
        return False
