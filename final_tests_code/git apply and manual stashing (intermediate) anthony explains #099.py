import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of storing patches in patch files instead of using stashes in Git?', 'How can the speaker create a patch file in Git?', 'How do the speaker apply a patch file to your working directory in Git?', 'What is the command to apply a patch file in Git?', 'What is the command to apply a patch file if the speaker are not in Git?', 'What does the -p1 flag do in the patch command?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of storing patches in patch files instead of using stashes in Git?', 'How can the speaker create a patch file in Git?', 'How do the speaker apply a patch file to your working directory in Git?', 'What is the command to apply a patch file in Git?', 'What is the command to apply a patch file if the speaker are not in Git?', 'What does the -p1 flag do in the patch command?'], ['Storing patches in patch files allows for keeping temporary code changes without the risk of losing them, unlike stashes which can sometimes cause conflicts and loss of changes.', "You can create a patch file in Git by using the command 'git diff' to show the difference, and then piping the output to a file using '>' or '>>'. For example, 'git diff > patchfile.patch'.", "You can apply a patch file to your working directory in Git using the command 'git apply <patchfile>'. This command will apply the changes from the patch file to your current working directory.", 'git apply', 'patch -p1 -i', 'It strips the first path component of the diff.']))
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
