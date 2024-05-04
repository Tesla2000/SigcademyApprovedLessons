import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of checking a directory but ignoring all of its contents in Git?', 'How does Git handle directories in comparison to other version control systems like SVN?', 'What approach can be used to check a directory in Git but ignore its contents?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of checking a directory but ignoring all of its contents in Git?', 'How does Git handle directories in comparison to other version control systems like SVN?', 'What approach can be used to check a directory in Git but ignore its contents?'], ['The purpose is to avoid checking in certain files or directories, such as build outputs, into version control while still including the directory structure itself.', 'Git does not natively support directories as part of its values. In Git, all values are files or file-like things like symlinks or submodules. Other version control systems like SVN have native support for directories.', 'One approach is to use a .gitignore file inside the directory and include an exclusion rule to un-ignore the directory itself while ignoring its contents. This allows the directory structure to be included in version control without including specific files within the directory.']))
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
