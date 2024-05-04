import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['How do the speaker pronounce PYP I?', 'What is the reason for pronouncing it as Pi Pi?', 'What is PYP Y?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['How do the speaker pronounce PYP I?', 'What is the reason for pronouncing it as Pi Pi?', 'What is PYP Y?'], ['Pi Pi', 'It is the Python package index', 'PYP Y is an alternative implementation of Python based on the spec of C Python, serving as a just-in-time compiler of Python']))
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
