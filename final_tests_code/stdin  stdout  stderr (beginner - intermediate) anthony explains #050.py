import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is standard in?', 'How can the speaker read from standard in in Python?', 'What is standard out?', 'How can the speaker write to standard out in Python?', 'What is the purpose of redirecting standard output to a file?', 'How can standard output be redirected to a file in a command line?', 'What is the difference between standard output and standard error?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is standard in?', 'How can the speaker read from standard in in Python?', 'What is standard out?', 'How can the speaker write to standard out in Python?', 'What is the purpose of redirecting standard output to a file?', 'How can standard output be redirected to a file in a command line?', 'What is the difference between standard output and standard error?'], ['Standard in is the input stream that allows the speaker to read from the keyboard or redirect input from a file or another process.', 'You can read from standard in in Python using sys.stdin.read() or sys.stdin.readline().', 'Standard out is the default place to produce outputs in a program. It is where the program prints its output.', 'You can write to standard out in Python using the print statement or sys.stdout.write().', 'Redirecting standard output to a file allows the output of a program to be saved in a file instead of displayed on the console, making it easier to store or analyze the output later.', "Standard output can be redirected to a file in a command line by using the '>' symbol followed by the file name. For example, 'command > output.txt' redirects the output of 'command' to a file named 'output.txt'.", 'Standard output is used for normal program output, while standard error is used for error messages or diagnostic information. Redirecting standard error separately allows for better organization of program output and error messages.']))
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
