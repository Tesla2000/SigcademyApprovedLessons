import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["What is the command to remove an accidental commit using 'git reset --hard'?", "What is the command to remove an accidental commit using 'git reset --soft'?", 'Which command is more suitable if the speaker want to keep the changes in your working directory but remove the commit itself?', "When using 'git rebase' to remove an older commit, what flag is used for interactive rebase?", 'How do the speaker remove a commit during a rebase process?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["What is the command to remove an accidental commit using 'git reset --hard'?", "What is the command to remove an accidental commit using 'git reset --soft'?", 'Which command is more suitable if the speaker want to keep the changes in your working directory but remove the commit itself?', "When using 'git rebase' to remove an older commit, what flag is used for interactive rebase?", 'How do the speaker remove a commit during a rebase process?'], ['git reset --hard', 'git reset --soft', 'git reset --soft', '-i', 'To remove a commit during a rebase process, the speaker need to delete the line corresponding to that commit in the rebase dialog and then save the file. This action will successfully rebase and update the refs head. The removed commit will no longer be included in the file or the git log.']))
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
