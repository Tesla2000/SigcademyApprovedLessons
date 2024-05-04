import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["Why don't the speaker have to type the first argument of methods in mypy?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["Why don't the speaker have to type the first argument of methods in mypy?"], ["You don't have to type annotate the 'self' argument in methods because mypy can infer the type based on the class. It is not necessary to explicitly annotate 'self' as 'c' in the method signature, as mypy can determine the type from the class definition. Additionally, using 'from __future__ import annotations' or quoting the annotations can help resolve forward reference issues in type annotations."]))
    chat = langchain_openai.ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
    chat_answer = chat.invoke(
        [
            langchain_core.messages.SystemMessage(content="You will be given question, reference answer pair and users answer. "
                                  'You have to decide if the answer is correct. '
                                  'If it is respond with a single work "Correct" otherwise return a hint about the answer. '),
            langchain_core.messages.SystemMessage(content='The question: ' + question + '\n'
                                  'The reference answer: ' + reference_answers[question]),
            langchain_core.messages.HumanMessage(
                content=answer
            )
        ]
    ).content
    if chat_answer.startswith("Correct"):
        return True
    return chat_answer
