import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the name of the terminal multiplexer mentioned in the video?', 'What is the default leader key for Tmux commands?', 'How do the speaker create a new tab in Tmux?', 'How do the speaker switch between tabs in Tmux?', 'How do the speaker vertically split panes in Tmux?', 'What is the purpose of setting synchronized panes in the debugger?', 'How can the speaker set synchronized panes in the debugger?', 'How can synchronized panes help in debugging Python code differences between Python 2 and Python 3?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the name of the terminal multiplexer mentioned in the video?', 'What is the default leader key for Tmux commands?', 'How do the speaker create a new tab in Tmux?', 'How do the speaker switch between tabs in Tmux?', 'How do the speaker vertically split panes in Tmux?', 'What is the purpose of setting synchronized panes in the debugger?', 'How can the speaker set synchronized panes in the debugger?', 'How can synchronized panes help in debugging Python code differences between Python 2 and Python 3?'], ['Tmux', 'Control B', 'Control B followed by C', 'Control B followed by a number', 'Control B followed by %', 'Setting synchronized panes in the debugger allows the speaker to send commands to multiple Python instances simultaneously, making it easier to compare their behavior and identify differences in code execution.', "To set synchronized panes in the debugger, the speaker can use the command 'set synchronize-panes' or 'set synchronize-panes on' in the debugger interface.", 'Synchronized panes help in debugging Python code differences between Python 2 and Python 3 by allowing the speaker to step through the code in both versions simultaneously and identify discrepancies in behavior, making it easier to pinpoint and fix bugs.']))
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
