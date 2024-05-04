import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What does TTY stand for?', 'What is a TTY in modern computing?', 'What is the role of a shell in relation to a TTY?', 'What is the significance of the TTY method in UNIX pipes and files?', 'What is the purpose of piping output in a command line interface?', "What does it mean when the 'is a TTY' value is false for a stream in a command line interface?", "How does the 'is a TTY' value differ for standard input, standard output, and standard error in a command line interface?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What does TTY stand for?', 'What is a TTY in modern computing?', 'What is the role of a shell in relation to a TTY?', 'What is the significance of the TTY method in UNIX pipes and files?', 'What is the purpose of piping output in a command line interface?', "What does it mean when the 'is a TTY' value is false for a stream in a command line interface?", "How does the 'is a TTY' value differ for standard input, standard output, and standard error in a command line interface?"], ['TTY stands for teletypewriter.', 'In modern computing, a TTY refers to a terminal emulator that allows interaction with a console in a similar way to the traditional teletypewriter.', 'The shell is the program that the terminal is running, which receives commands and executes them. It defines the prompt text and handles user input in the terminal.', 'In UNIX pipes and files, the TTY method on streams determines if a stream can accept input from a keyboard, indicating whether it is a TTY or not.', 'The purpose of piping output in a command line interface is to redirect the output of one command as input to another command, allowing for the chaining of commands and manipulation of data streams.', "When the 'is a TTY' value is false for a stream in a command line interface, it indicates that the stream is not connected to an interactive terminal. This typically occurs when the output is redirected or piped to a file or another command.", "The 'is a TTY' value for standard input, standard output, and standard error in a command line interface indicates whether the input or output stream is interactive. When the value is true, it means the stream is connected to an interactive terminal, and when it is false, it means the stream is not connected to an interactive terminal."]))
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
