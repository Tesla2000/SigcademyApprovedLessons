import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What package are we releasing today?', 'What is the version number we are bumping to?', 'What is the reason for the manual release process instead of automation?', 'What command is used to tag the last argument of the previous command as v1.417 in bash?', 'What command is used to create a source distribution and wheel for the package?', 'How do the speaker upload the package to PyPI using twine?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What package are we releasing today?', 'What is the version number we are bumping to?', 'What is the reason for the manual release process instead of automation?', 'What command is used to tag the last argument of the previous command as v1.417 in bash?', 'What command is used to create a source distribution and wheel for the package?', 'How do the speaker upload the package to PyPI using twine?'], ['identify', '1.4.7teen', "The current solutions involve having a credential somewhere that needs to be rotated and updated, so it's easier to do it locally for the user.", 'get tagged bang dollar sign', 'calling setup.py with sdist and bdist_wheel', 'twine upload -r pypi dist/*']))
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
