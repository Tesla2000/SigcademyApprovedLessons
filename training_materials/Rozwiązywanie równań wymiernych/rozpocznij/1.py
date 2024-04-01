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
        f"""<!-- {first_zero},{-zero_out_of_domain} --><math xmlns="http://www.w3.org/1998/Math/MathML" style="font-size: 24px;">
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
    return questions


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        modified_answer = set(map(int, answer.strip().split(",")))
        if set(map(int, re.findall(r'[-\d]+,[-\d,]+', question)[0].split(','))) == modified_answer:
            return True
        return f"Your answer {answer} is incorrect."
    except Exception as e:
        print(e)
        return f"Answers must be coma separated. Is {answer}"
