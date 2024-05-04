import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is post-mortem debugging?', "What does the term 'post-mortem' refer to in post-mortem debugging?", 'What is the purpose of post-mortem debugging?', 'How does post-mortem debugging help in understanding program failures?', 'What is post-mortem debugging?', 'What are some common scenarios where post-mortem debugging is useful?', 'What are the three ways mentioned in the text to perform post-mortem debugging?', 'What tool can the speaker use for post-mortem debugging in Python tests?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is post-mortem debugging?', "What does the term 'post-mortem' refer to in post-mortem debugging?", 'What is the purpose of post-mortem debugging?', 'How does post-mortem debugging help in understanding program failures?', 'What is post-mortem debugging?', 'What are some common scenarios where post-mortem debugging is useful?', 'What are the three ways mentioned in the text to perform post-mortem debugging?', 'What tool can the speaker use for post-mortem debugging in Python tests?'], ['Post-mortem debugging is a technique used to debug programs after a failure has occurred, allowing developers to investigate the problem that caused the failure.', "The term 'post-mortem' comes from 'after death,' indicating that the debugging occurs after the program has encountered a failure.", 'The purpose of post-mortem debugging is to analyze and debug failures that have already occurred in a program, helping developers understand the root cause of the issue.', 'Post-mortem debugging allows developers to inspect the state of the program at the time of failure, identify the cause of the failure, and make necessary corrections to prevent similar issues in the future.', 'Post-mortem debugging is a technique used to debug programs after they have crashed or encountered an error. It involves analyzing the state of the program at the time of the error to identify the cause of the issue.', 'Post-mortem debugging is useful in scenarios where errors occur during program execution, such as division by zero errors, unexpected exceptions, or crashes. It helps developers analyze the state of the program at the time of the error to diagnose and fix the issue.', 'The three ways mentioned in the text to perform post-mortem debugging are: 1. Using PDB (Python Debugger) to debug errors after they occur. 2. Manually triggering post-mortem debugging by importing PDB and using PDB post-mortem in the code. 3. Using a test runner like Pytest to create intentionally failing tests for debugging.', 'You can use the PDB option in Pytest for post-mortem debugging in Python tests.']))
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
