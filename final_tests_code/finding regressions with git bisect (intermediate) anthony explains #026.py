import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What does Git bisect help with?', 'What is git bisect used for?', "Where does the term 'bisect' in git bisect come from?", 'Can the speaker explain how git bisect works with a diagram?', 'What example repository and issue is being used to demonstrate git bisect in this video?', 'What command is being used to validate the script?', 'What is the purpose of the script check_py_inputs?', 'What exit code is used to indicate that the current revision should be skipped during git bisect?', 'What command puts us into bisection mode in Git?', 'What are the commands used in Git bisect to set the before and after states for bisection?', 'What command is used to run the bisection process in Git?', 'What tool is being discussed in the text?', 'How does Git bisect work?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What does Git bisect help with?', 'What is git bisect used for?', "Where does the term 'bisect' in git bisect come from?", 'Can the speaker explain how git bisect works with a diagram?', 'What example repository and issue is being used to demonstrate git bisect in this video?', 'What command is being used to validate the script?', 'What is the purpose of the script check_py_inputs?', 'What exit code is used to indicate that the current revision should be skipped during git bisect?', 'What command puts us into bisection mode in Git?', 'What are the commands used in Git bisect to set the before and after states for bisection?', 'What command is used to run the bisection process in Git?', 'What tool is being discussed in the text?', 'How does Git bisect work?'], ['Figuring out open source problems by identifying the commit that introduced a bug or issue', 'Git bisect is used to find when a change occurred in a repository, particularly to find regressions where things got worse or broke between versions.', "The term 'bisect' comes from splitting something in half, and git bisect uses a binary search algorithm to find when the change occurred.", 'Git bisect works by splitting the range between a known good and bad version in half, testing the middle point, and then narrowing down the range based on the result. It continues this process until it finds the exact commit that introduced the change in behavior.', 'The example repository being used is PI code style, and the issue is related to tab indented code triggering a bug in an old version of PI code style.', 'subprocess.run', 'To determine whether each revision is good, bad, or needs to be skipped during the git bisect process.', '125', 'git bisect start', 'git bisect good <commit> and git bisect bad <commit>', 'git bisect run', 'Git bisect', 'It uses a binary search algorithm to efficiently find the commit that introduced a bug or regression']))
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
