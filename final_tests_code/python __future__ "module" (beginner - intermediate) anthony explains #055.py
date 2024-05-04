import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the double under future module in Python?', "What does the future flag 'future import annotations' do?", 'Why is the future annotations import considered a side effect?', 'What is the purpose of future flags in Python?', 'What is the future division behavior in Python 2 and Python 3?', 'What is the difference between the print statement in Python 2 and Python 3?', 'What does the `from __future__ import unicode_literals` do in Python?', 'What is the purpose of `from __future__ import generator_stop` in Python 3.7?', 'What is the importance of the order of `__future__` imports in a Python file?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the double under future module in Python?', "What does the future flag 'future import annotations' do?", 'Why is the future annotations import considered a side effect?', 'What is the purpose of future flags in Python?', 'What is the future division behavior in Python 2 and Python 3?', 'What is the difference between the print statement in Python 2 and Python 3?', 'What does the `from __future__ import unicode_literals` do in Python?', 'What is the purpose of `from __future__ import generator_stop` in Python 3.7?', 'What is the importance of the order of `__future__` imports in a Python file?'], ['The double under future module in Python is a special module that allows the speaker to change how Python behaves by importing specific flags from it. It does not provide any useful code but is used to modify the behavior of Python modules.', "The 'future import annotations' flag changes how type annotations are evaluated in a Python module. It treats all annotations as deferred annotations, turning them into strings instead of actual names.", 'The future annotations import is considered a side effect because it changes how type annotations are evaluated in a Python module without directly providing any code or functionality. It modifies the behavior of annotations in the module.', 'Future flags in Python are used to provide feature previews for potential changes or enhancements in the language. They allow developers to opt into new features or changes before they become finalized in Python, making migration between different versions easier.', 'In Python 2, dividing integers results in integer division, while in Python 3, dividing integers results in floating-point division unless modular division is explicitly used. You can enable Python 3 division behavior in Python 2 by importing `division` from `__future__`.', 'In Python 2, `print` is a statement, while in Python 3, `print` is a function.', '`from __future__ import unicode_literals` changes the type of string literals to Unicode by default, allowing the speaker to use Unicode strings instead of byte strings.', '`from __future__ import generator_stop` changes the exception hierarchy for stopping a generator in Python 3.7. Instead of raising `StopIteration` to stop a generator, the speaker need to raise `GeneratorExit` to stop it.', '`__future__` imports must appear before any other code in the file. However, docstrings must still appear before any other code, including `__future__` imports. This is because Python uses `__future__` imports to handle the execution of the rest of the file.']))
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
