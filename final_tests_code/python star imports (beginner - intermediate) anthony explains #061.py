import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the video about?', 'What is a star import in Python?', 'What are some caveats of using star imports in Python?', 'How can the speaker control which names are imported with a star import in Python?', "What is the purpose of the '__all__' module constant in Python?", 'What is a common issue with using star imports in Python?', 'How can using star imports make it hard for tools to detect errors in code?', 'When might star imports be considered acceptable in Python code?', 'What is the error code mentioned in the text?', 'What does F 403 refer to?', "What does the text mention about using 'import star' in Python?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the video about?', 'What is a star import in Python?', 'What are some caveats of using star imports in Python?', 'How can the speaker control which names are imported with a star import in Python?', "What is the purpose of the '__all__' module constant in Python?", 'What is a common issue with using star imports in Python?', 'How can using star imports make it hard for tools to detect errors in code?', 'When might star imports be considered acceptable in Python code?', 'What is the error code mentioned in the text?', 'What does F 403 refer to?', "What does the text mention about using 'import star' in Python?"], ['The video is about star imports in Python and why they are discouraged for use in code.', "A star import in Python is when the speaker import all names from a module using the syntax 'from module import *'.", 'Some caveats of using star imports in Python include importing unwanted names, potential namespace collisions, and making code harder to read and maintain.', "You can control which names are imported with a star import in Python by setting the special double underscore '__all__' module constant to specify the names to be exported.", "The '__all__' module constant in Python is used to specify the names that should be exported when using a star import from a module.", 'One common issue with using star imports in Python is that it makes it difficult for tools to determine whether a name is used or not without actually importing the code. This can lead to ambiguity and potential errors, especially in cases where multiple names are imported using a star import.', 'Using star imports can make it hard for tools to detect errors in code because it obscures the origin of imported names. This can lead to confusion and ambiguity, making it challenging for tools to identify and flag potential issues such as typos or mismatched names.', 'Star imports might be considered acceptable in Python code in interactive sessions where immediate functionality is prioritized over code correctness. Additionally, in certain cases within __init__.py files where re-exporting names from sub-packages is necessary, star imports may be used. However, it is generally recommended to avoid star imports in favor of explicit imports for clarity and maintainability.', '403', 'Forbidden error code 403', 'It allows access to functions of a sub package exposed as part of the main package using dot notation.']))
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
