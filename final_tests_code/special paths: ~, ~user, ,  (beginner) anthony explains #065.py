import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What does dot represent in a path?', 'When can CD dot fail?', 'What does dot dot represent in a path?', 'What does tilde (~) refer to in a path?', 'What is the purpose of using OS path expand user in Python?', 'How does OS path expand user handle tilde with a username after it?', 'Is the tilde symbol expansion supported outside of shells in Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What does dot represent in a path?', 'When can CD dot fail?', 'What does dot dot represent in a path?', 'What does tilde (~) refer to in a path?', 'What is the purpose of using OS path expand user in Python?', 'How does OS path expand user handle tilde with a username after it?', 'Is the tilde symbol expansion supported outside of shells in Python?'], ["Dot represents the current directory that you're in.", 'CD dot can fail if the current directory is deleted.', 'Dot dot represents the directory above the current directory.', 'Tilde (~) refers to the home directory of the user.', "OS path expand user allows for the expansion of the tilde symbol (~) into a user's home directory path, making it cross-platform compatible and enabling easy access to user-specific directories.", "When tilde is followed by a username, OS path expand user resolves to that specific user's directory, providing a convenient way to access user-specific paths in Python.", 'The tilde symbol expansion is not supported outside of shells in Python, unless the program has special capabilities like OS path expand user to handle it.']))
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
