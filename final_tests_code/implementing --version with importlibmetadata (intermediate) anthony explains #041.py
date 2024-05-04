import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["What is the purpose of the tool 'ast pretty'?", "What new module in Python 3.8 is being used in the implementation of the '--version' option for 'ast pretty'?", "How is the '--version' option being implemented in 'ast pretty'?", 'What is the issue with running the code as a main module?', "What is the output of 'Python -m ast pretty' and why is it not the desired output?", 'Why does the code currently only work in Python 3.8 and above?', 'How can the code be modified to work in Python 3.7 as well?', 'What is the conditional import block used to include the backport package for older versions of Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["What is the purpose of the tool 'ast pretty'?", "What new module in Python 3.8 is being used in the implementation of the '--version' option for 'ast pretty'?", "How is the '--version' option being implemented in 'ast pretty'?", 'What is the issue with running the code as a main module?', "What is the output of 'Python -m ast pretty' and why is it not the desired output?", 'Why does the code currently only work in Python 3.8 and above?', 'How can the code be modified to work in Python 3.7 as well?', 'What is the conditional import block used to include the backport package for older versions of Python?'], ["The purpose of 'ast pretty' is to pretty print the abstract syntax tree of a Python file, which is useful for tasks like writing a linter.", "The new module being used is 'importlib.metadata', which allows querying metadata of installed packages.", "The '--version' option is being implemented by adding an argument parser action with 'action=version' and using 'importlib.metadata' to retrieve the package version.", "When running the code as a main module, the 'double' in 'her name' will be doubled under 'main', resulting in an incorrect value.", "The output of 'Python -m ast pretty' is 'ast.pretty.PI', which is not the desired output. The desired output is 'ast.cream'. This can be fixed by using an argument parser with 'prog' set to 'yes'.", "The code currently only works in Python 3.8 and above because it uses 'importlib.metadata' which is available in Python 3.8 and above.", "To make the code work in Python 3.7 as well, the 'importlib-metadata' backport package can be used. This package provides 'importlib.metadata' to older versions of Python. An environment specifier can be used to conditionally install 'importlib-metadata' only on versions of Python that are older than 3.8.", "The conditional import block is 'if sys.version_info < (3, 8): import importlib_metadata as importlib.metadata else: import importlib.metadata'. This block ensures that the backport package is imported for older versions of Python while the standard library module is imported for newer versions."]))
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
