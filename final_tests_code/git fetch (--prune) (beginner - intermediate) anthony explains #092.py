import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the command that is frequently run on stream?', "What does 'git fetch' do?", "What does 'git push' do?", "Why might someone use 'git fetch --prune'?", 'What is the purpose of using `git fetch --prune`?', 'How can the speaker configure Git to always prune remote branches without specifying `--prune` in the command line?', "What command is used to fetch with dash's prune?", 'Why is the diagram provided helpful?', "Why do the speaker use the command 'get fetch with dash's prune'?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the command that is frequently run on stream?', "What does 'git fetch' do?", "What does 'git push' do?", "Why might someone use 'git fetch --prune'?", 'What is the purpose of using `git fetch --prune`?', 'How can the speaker configure Git to always prune remote branches without specifying `--prune` in the command line?', "What command is used to fetch with dash's prune?", 'Why is the diagram provided helpful?', "Why do the speaker use the command 'get fetch with dash's prune'?"], ['git fetch --prune', 'Pulls branches from the remote repository to the local version.', 'Puts branches from the local version to the remote repository.', 'To delete references to branches that have been deleted in the remote repository and save disk space.', 'The purpose of using `git fetch --prune` is to delete remote branches that have been deleted on the remote repository, ensuring that the local repository stays in sync with the remote repository and saves disk space.', 'You can configure Git to always prune remote branches by setting the global configuration option `git config --global fetch.prune true`. This setting will automatically prune remote branches during fetch operations.', "get fetch with dash's prune", 'It is somewhat helpful', 'To set it to true']))
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
