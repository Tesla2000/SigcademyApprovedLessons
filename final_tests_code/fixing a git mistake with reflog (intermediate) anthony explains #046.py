import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What command can help the speaker undo changes in a git repository?', 'What does git reflog do?', 'Is reflog a client-side or server-side log?', 'Can the speaker use reflog to revert back to a previous position in a repository?', 'What is the purpose of using `git reflog`?', 'How can `git reflog` be useful before performing other Git operations like amends, rebases, or merges?', 'Have the speaker ever used `git reflog` to undo a dangerous operation in Git?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What command can help the speaker undo changes in a git repository?', 'What does git reflog do?', 'Is reflog a client-side or server-side log?', 'Can the speaker use reflog to revert back to a previous position in a repository?', 'What is the purpose of using `git reflog`?', 'How can `git reflog` be useful before performing other Git operations like amends, rebases, or merges?', 'Have the speaker ever used `git reflog` to undo a dangerous operation in Git?'], ['git reflog', "It lets the speaker see every single operation that you've done that causes a commit or a checkout, and the speaker can use this log to revert back to any position in time.", 'Reflog is a client-side log.', 'Yes, the speaker can use reflog to revert back to a previous position in a repository.', 'The purpose of using `git reflog` is to view a log of all the reference updates in a Git repository, allowing users to track changes and easily revert to previous states if needed.', '`git reflog` can be useful before performing other Git operations like amends, rebases, or merges because it allows users to undo any unintended changes or mistakes by reverting to previous states recorded in the reflog history.', 'Yes, I have used `git reflog` to undo dangerous operations in Git, such as amends, rebases, or merges, by reverting to a previous state in the reflog history to correct mistakes or unintended changes.']))
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
