import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the path environment variable?', 'How are paths separated in Linux and Windows?', "What does the 'which' command do in Unix?", 'How does a virtual environment modify the path variable?', 'What is the purpose of setting the PATH environment variable in a Unix-like system?', 'What happens if the speaker forget to include the existing PATH entries when setting the PATH variable?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the path environment variable?', 'How are paths separated in Linux and Windows?', "What does the 'which' command do in Unix?", 'How does a virtual environment modify the path variable?', 'What is the purpose of setting the PATH environment variable in a Unix-like system?', 'What happens if the speaker forget to include the existing PATH entries when setting the PATH variable?'], ['The path environment variable is used by the system to look up executables. It is a list of paths where the system searches for executable files.', 'In Linux, paths are separated by colons, while in Windows, paths are separated by semicolons.', "The 'which' command in Unix is used to locate the executable file associated with a given command.", "A virtual environment modifies the path variable by prepending the virtual environment's bin directory to the beginning of the path. This ensures that executables in the virtual environment have precedence over other paths.", 'The purpose of setting the PATH environment variable is to specify a list of directories where executable files are located. This allows the system to locate and execute commands or programs without specifying the full path to the executable each time.', "If the speaker forget to include the existing PATH entries when setting the PATH variable, the speaker will lose access to all the other directories that were previously included in the PATH. This means the speaker won't be able to run commands or programs located in those directories unless the speaker specify the full path to the executable."]))
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
