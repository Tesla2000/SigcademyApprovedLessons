import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the name of the existing package that the speaker is using as an example in the video?', 'What issue does the speaker encounter with the packaging of the project?', 'How does the speaker explain the reason behind the tests still passing despite the broken packaging?', 'What solution does the speaker propose to fix the issue with the packaging?', 'What was the initial issue with the packaging setup?', 'How was the issue resolved?', 'What is the purpose of setting up the package directory in the source layout?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the name of the existing package that the speaker is using as an example in the video?', 'What issue does the speaker encounter with the packaging of the project?', 'How does the speaker explain the reason behind the tests still passing despite the broken packaging?', 'What solution does the speaker propose to fix the issue with the packaging?', 'What was the initial issue with the packaging setup?', 'How was the issue resolved?', 'What is the purpose of setting up the package directory in the source layout?'], ['PI upgrade', 'The packaging of the project is broken, but the tests still pass without detecting the issue.', 'The tests pass because the Python interpreter searches for modules in the current working directory, which contains the source code even though the packaging is broken.', "The speaker suggests using the source layout approach by creating a 'source' directory and moving the Python file into that directory to properly package the project.", "The module not found error 'no module named PI upgrade' was occurring, causing all tests to fail.", "The issue was resolved by setting up the package directory in the setup tools by mapping the empty string to the 'source' directory.", 'Setting up the package directory in the source layout ensures that the packaging is correctly configured and prevents accidental imports from the source directory instead of the installed package.']))
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
