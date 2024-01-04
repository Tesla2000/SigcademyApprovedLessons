import random
import re


def generate_questions() -> list[str]:
    first_zero = random.randint(1, 9)
    second_zero = random.randint(1, 9)
    multiplicator = random.randint(2, 5)
    while True:
        zero_out_of_domain = random.randint(1, 9)
        if zero_out_of_domain not in (first_zero, second_zero):
            break
    questions = [
        f"""1. Wypisz liczby poza dziedziną <!-- {first_zero},{-zero_out_of_domain} --><math xmlns="http://www.w3.org/1998/Math/MathML">
            <mfrac>
                <mrow>
                    <mo>(</mo>
                    <msup>
                        <mi>x</mi>
                        <mn>2</mn>
                    </msup>
                    <mo>-</mo>
                    <mn>{first_zero ** 2}</mn>
                    <mo>)(</mo>
                    <mi>{multiplicator}x</mi>
                    <mo>+</mo>
                    <mn>{multiplicator * second_zero}</mn>
                    <mo>)</mo>
                </mrow>
                <mrow>
                    <mo>(</mo>
                    <mi>x</mi>
                    <mo>-</mo>
                    <mn>{first_zero}</mn>
                    <mo>)(</mo>
                    <mi>x</mi>
                    <mo>+</mo>
                    <mn>{zero_out_of_domain}</mn>
                    <mo>)</mo>
                </mrow>
            </mfrac>
            <mo>= 0</mo>
        </math>""",
        f"""2. Rozwiąż równanie <!-- {-first_zero},{-second_zero} --><math xmlns="http://www.w3.org/1998/Math/MathML">
            <mfrac>
                <mrow>
                    <mo>(</mo>
                    <msup>
                        <mi>x</mi>
                        <mn>2</mn>
                    </msup>
                    <mo>-</mo>
                    <mn>{first_zero ** 2}</mn>
                    <mo>)(</mo>
                    <mi>{multiplicator}x</mi>
                    <mo>+</mo>
                    <mn>{multiplicator * second_zero}</mn>
                    <mo>)</mo>
                </mrow>
                <mrow>
                    <mo>(</mo>
                    <mi>x</mi>
                    <mo>-</mo>
                    <mn>{first_zero}</mn>
                    <mo>)(</mo>
                    <mi>x</mi>
                    <mo>+</mo>
                    <mn>{zero_out_of_domain}</mn>
                    <mo>)</mo>
                </mrow>
            </mfrac>
            <mo>= 0</mo>
        </math>""",
    ]
    squared_zero = random.randint(3, 9)
    coefficient = random.randint(3, 9)
    first_zero = -random.randint(3, 9)
    second_zero = random.randint(3, 9)
    zeros = {first_zero, second_zero, squared_zero, -squared_zero, 0}
    zero_out_of_domain = {-squared_zero, -second_zero, second_zero}
    questions.append(
        f"""3. Rozwiąż równanie <!-- {','.join(map(str, zeros - zero_out_of_domain))} --><math xmlns="http://www.w3.org/1998/Math/MathML">
      <mfrac>
        <mrow>
          <mrow>
            <mo>(</mo>
            <msup>
              <mi>x</mi>
              <mn>2</mn>
            </msup>
            <mo>-</mo>
            <mn>{squared_zero**2}</mn>
            <mo>)</mo>
          </mrow>
          <mo>&#8290;&sdot;&#8290;</mo>
          <mrow>
            <mo>(</mo>
            <mn>{coefficient}</mn>
            <msup>
              <mi>x</mi>
              <mn>2</mn>
            </msup>
            <mo>+</mo>
            <mn>{coefficient*-first_zero}</mn>
            <mi>x</mi>
            <mo>)</mo>
          </mrow>
          <mo>&#8290;&sdot;&#8290;</mo>
          <msup>
            <mrow>
              <mo>(</mo>
              <mi>x</mi>
              <mo>-</mo>
              <mn>{second_zero}</mn>
              <mo>)</mo>
            </mrow>
            <mn>2</mn>
          </msup>
        </mrow>
        <mrow>
          <mo>(</mo>
          <mrow>
            <msup>
              <mi>x</mi>
              <mn>2</mn>
            </msup>
            <mo>-</mo>
            <mn>{second_zero**2}</mn>
          </mrow>
          <mo>)</mo>
          <mo>&#8290;&sdot;&#8290;</mo>
          <mrow>
            <mo>(</mo>
            <mi>x</mi>
            <mo>+</mo>
            <mn>{squared_zero}</mn>
            <mo>)</mo>
          </mrow>
        </mrow>
      </mfrac>
    </math>=0""")
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        modified_answer = set(map(int, answer.strip().split(",")))
        if set(map(int, re.findall(r'[-\d]+,[-\d,]+', question)[0].split(','))) == modified_answer:
            return True
        return f"Your answer {answer} is incorrect."
    except:
        return f"Answers must be coma separated. Is {answer}"
