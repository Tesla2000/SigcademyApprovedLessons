import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What repository did the user find a typo in?', 'What was the typo that the user found in the repository?', 'What command is used to clone a repository?', 'What command is used to create a new branch from an existing branch in Git?', 'How can the speaker preview the changes made to a file in Git?', 'What command is used to stage a file for commit in Git?', 'What command is used to commit changes in Git with a commit message?', 'What is the commit message in the text?', 'What command is used to push the branch to the remote repository?', 'What is the next step after pushing the branch to the remote repository?', 'What view does the author prefer when reviewing code changes on GitHub?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What repository did the user find a typo in?', 'What was the typo that the user found in the repository?', 'What command is used to clone a repository?', 'What command is used to create a new branch from an existing branch in Git?', 'How can the speaker preview the changes made to a file in Git?', 'What command is used to stage a file for commit in Git?', 'What command is used to commit changes in Git with a commit message?', 'What is the commit message in the text?', 'What command is used to push the branch to the remote repository?', 'What is the next step after pushing the branch to the remote repository?', 'What view does the author prefer when reviewing code changes on GitHub?'], ['flake8 annotations', "A missing 'S' in the word 'ellipses'", 'git clone <repository_url>', 'git checkout -b <branch_name>', 'git diff', 'git add <file_name>', 'git commit -m <commit_message>', 'Fix typo in readme MD.', 'git push origin head.', 'Creating a pull request.', 'Split diff view.']))
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
