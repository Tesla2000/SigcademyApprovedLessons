import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the basic functionality of the `git show` command?', 'How can the speaker show the contents of a merge commit using `git show`?', 'How can the speaker use the `--name-only` flag with `git show` to view only the names of the files changed?', 'What is the command to show the commit history in Git?', 'What does the option -M do in the git show command?', 'How can the speaker combine the tip with -M in the git show command?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the basic functionality of the `git show` command?', 'How can the speaker show the contents of a merge commit using `git show`?', 'How can the speaker use the `--name-only` flag with `git show` to view only the names of the files changed?', 'What is the command to show the commit history in Git?', 'What does the option -M do in the git show command?', 'How can the speaker combine the tip with -M in the git show command?'], ['The `git show` command shows the difference introduced by a particular commit or blob, including author, date, commit message, and patch for that commit.', 'To show the contents of a merge commit, the speaker can use the `-m` flag with `git show`. For example, `git show -m HEAD` will show all the differences to each of the parents of the merge commit.', "You can use the `--name-only --format=''` flags with `git show` to view only the names of the files changed without any additional information. This format option helps in selecting a pretty format for `git show` output.", 'git log', 'The -M option in git show command is used to detect renames.', 'You can combine the tip with -M by using the lowercase m option in the git show command.']))
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
