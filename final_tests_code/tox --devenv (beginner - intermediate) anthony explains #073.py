import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What tool did the speaker mention using for developing on a Python package?', "What is the command to invoke the 'dev' feature in 'tox'?", "What does 'editable install' mean in the context of developing a Python package?", "How does the speaker recommend setting up a development virtual environment using 'tox'?", 'What command can be used to select a different environment in talks.ini?', 'What is the command to create a separate pre-commit environment in talks.ini?', 'What is the command to activate the pre-commit environment in talks.ini?', "What is the sneaky thing the speaker learned about 'dev' in talks.ini?", "What happens when the speaker run 'talks devem devin' in talks.ini?", 'How can the speaker run the tests after setting up the development environment in talks.ini?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What tool did the speaker mention using for developing on a Python package?', "What is the command to invoke the 'dev' feature in 'tox'?", "What does 'editable install' mean in the context of developing a Python package?", "How does the speaker recommend setting up a development virtual environment using 'tox'?", 'What command can be used to select a different environment in talks.ini?', 'What is the command to create a separate pre-commit environment in talks.ini?', 'What is the command to activate the pre-commit environment in talks.ini?', "What is the sneaky thing the speaker learned about 'dev' in talks.ini?", "What happens when the speaker run 'talks devem devin' in talks.ini?", 'How can the speaker run the tests after setting up the development environment in talks.ini?'], ["The speaker mentioned using 'tox' for developing on a Python package.", "The command to invoke the 'dev' feature in 'tox' is 'tox -e dev'.", "'Editable install' means that if the speaker edit the code, the changes will be immediately reflected in what you're working on. It allows for dynamic updates to the code during development.", "The speaker recommends using 'tox -e dev' to set up a development virtual environment. This command will install the necessary dependencies and set up an editable install of the library for development.", "You can use 'dash e' to select a different environment in talks.ini.", "The command to create a separate pre-commit environment is 'talk sashi pre-commit dash dash devon vm pc'.", "You can activate the pre-commit environment using 'pc bin activate'.", "The speaker learned that 'talks devem' works even if the library doesn't use talks at all.", "Running 'talks devem devin' creates a development environment that installs the library and its dependencies.", "You can run 'pip install pytest' and then 'pytest tests' to run the tests after setting up the development environment."]))
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
