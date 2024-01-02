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

    return [
        f"""
        1. Wypisz elementy dziedziny <!-- Komentarz -->
    <math xmlns="http://www.w3.org/1998/Math/MathML">
            <mfrac>
                <mrow>
                    <mo>(</mo>
                    <msup>
                        <mi>x</mi>
                        <mn>2</mn>
                    </msup>
                    <mo>-</mo>
                    <mn>{first_zero**2}</mn>
                    <mo>)(</mo>
                    <mi>{multiplicator}x</mi>
                    <mo>+</mo>
                    <mn>{multiplicator*second_zero}</mn>
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
        </math>"""
        f"""
        2. Rozwiąż równanie <!-- Komentarz -->
    <math xmlns="http://www.w3.org/1998/Math/MathML">
            <mfrac>
                <mrow>
                    <mo>(</mo>
                    <msup>
                        <mi>x</mi>
                        <mn>2</mn>
                    </msup>
                    <mo>-</mo>
                    <mn>{first_zero**2}</mn>
                    <mo>)(</mo>
                    <mi>{multiplicator}x</mi>
                    <mo>+</mo>
                    <mn>{multiplicator*second_zero}</mn>
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
        </math>"""
    ]


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    try:
        modified_answer = set(map(int, answer.strip().split(",")))
    except ValueError:
        return f"Answers must be coma separated. Is {answer}"
    question = re.sub(r"\s+", "", question)
    question = question.replace(
        re.sub(
            r"\s+",
            "",
            (
                """<math xmlns="http://www.w3.org/1998/Math/MathML">
            <mfrac>
                <mrow>
                    <mo>(</mo>
                    <msup>
                        <mi>x</mi>
                        <mn>2</mn>
                    </msup>
                    <mo>-</mo>
                    <mn>"""
            ),
        ),
        "",
    )
    first_zero, _, question = question.partition("</mn><mo>)(</mo><mi>")
    multiplicator, _, question = question.partition("x</mi><mo>+</mo><mn>")
    second_zero, _, _ = question.partition("</mn>")
    if modified_answer == {
        -int(int(first_zero) ** 0.5),
        -int(int(second_zero) / int(multiplicator)),
    }:
        return True
    return f"Your answer {answer} is incorrect."
