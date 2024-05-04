import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the first use of underscore in Python mentioned in the video?', 'How is underscore used in unpacking in Python?', 'Why is double underscore used in function arguments in Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the first use of underscore in Python mentioned in the video?', 'How is underscore used in unpacking in Python?', 'Why is double underscore used in function arguments in Python?'], ['In an interactive prompt, underscore is a magic variable set to the previous value of an expression that was run.', "In unpacking, underscore is used to ignore specific values. It can be used to ignore a single value or multiple values by using '_, *_, or **_' respectively.", "Double underscore is used in function arguments to ensure uniqueness of argument names. It allows functions to ignore all passed arguments and perform a specific action, such as printing 'hi' in the example provided."]))
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
