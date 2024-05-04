import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the double under import function in Python?', 'How can the speaker split a dotted string into module and attribute parts in Python?', "What is the significance of the 'from list' parameter in the double under import function?", "What is the purpose of the 'from list' in Python's import statement?", "How does the 'from list' affect the import of modules in Python?", "What is the significance of the 'from list' in Python's import statement?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the double under import function in Python?', 'How can the speaker split a dotted string into module and attribute parts in Python?', "What is the significance of the 'from list' parameter in the double under import function?", "What is the purpose of the 'from list' in Python's import statement?", "How does the 'from list' affect the import of modules in Python?", "What is the significance of the 'from list' in Python's import statement?"], ['The double under import function in Python is used to import a module using a string representation of the module name, allowing for dynamic imports based on string values.', 'You can split a dotted string into module and attribute parts in Python by using the partition method with the dot as the separator. This will separate the string into the module part and the attribute part.', "The 'from list' parameter in the double under import function is used to specify a list of names to emulate a 'from import' statement or an empty list to emulate a regular import statement. This parameter allows for more control over the import process when using the double under import function.", "The 'from list' in Python's import statement is used to specify the sub-module to import from a package. If the 'from list' is empty, it imports the package itself. If the 'from list' is not empty, it imports the specified sub-module from the package.", "If the 'from list' is empty, the import statement returns the package. If the 'from list' is not empty, it returns the specified sub-module from the package.", "The 'from list' in Python's import statement is important for specifying which sub-module to import from a package. It determines whether the package itself or a specific sub-module is imported based on the contents of the 'from list'."]))
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
