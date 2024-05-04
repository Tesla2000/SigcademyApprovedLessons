import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of a shebang in a script?', 'How does Linux determine if a file is executable or not?', 'What happens if a script file does not have the executable bit set?', 'What is the trick used with shebangs to run executables with environment variables?', 'What is a limitation of shebangs related to file names?', 'How does Windows handle shebangs compared to Linux?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of a shebang in a script?', 'How does Linux determine if a file is executable or not?', 'What happens if a script file does not have the executable bit set?', 'What is the trick used with shebangs to run executables with environment variables?', 'What is a limitation of shebangs related to file names?', 'How does Windows handle shebangs compared to Linux?'], ['The shebang in a script tells the operating system or shell how to evaluate the script and which program to use to run it. It typically includes the path to the executable program.', 'Linux determines if a file is executable based on its file permissions. If the executable bit is set in the file permissions, the file can be run as an executable. Otherwise, it will not be executable.', "If a script file does not have the executable bit set, attempting to run it will result in a 'permission denied' error. The file needs to have the executable bit set using the 'chmod' command.", "The trick is to abuse the executable called 'env' by setting environment variables and then running an executable using 'env'. This allows for flexibility in specifying the executable without hard-coding to a specific path.", 'One limitation of shebangs is that they may max out at 127 characters, which can be problematic when working with long file paths, especially in CI systems like Jenkins.', "Windows does not support shebangs like Linux does. Instead, Windows determines how to execute files based on file extensions and the 'PATHEXT' variable, without the concept of executable and non-executable files."]))
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
