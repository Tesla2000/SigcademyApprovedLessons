import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What command can be used to modify the initial commit in Git?', 'Why do developers put an empty git commit at the beginning of their repositories when starting a new project?', 'How do developers create an empty git commit at the beginning of a new project?', 'Why do the speaker make an initial commit even if the speaker might not need it?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What command can be used to modify the initial commit in Git?', 'Why do developers put an empty git commit at the beginning of their repositories when starting a new project?', 'How do developers create an empty git commit at the beginning of a new project?', 'Why do the speaker make an initial commit even if the speaker might not need it?'], ['git commit --amend', "Developers put an empty git commit at the beginning of their repositories when starting a new project to establish a clean starting point for version control. This empty commit serves as the initial commit in the repository, allowing developers to easily track changes and manage the project's history.", "To create an empty git commit at the beginning of a new project, developers can use the command 'git commit --allow-empty' with an optional commit message. This command creates a commit that does not change any files in the repository, effectively marking the start of the project's history.", 'As a force of habit and because the speaker are more used to your normal workflow with rebase.']))
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
