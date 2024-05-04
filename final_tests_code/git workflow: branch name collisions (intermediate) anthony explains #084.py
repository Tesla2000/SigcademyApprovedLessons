import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['How can the speaker work on a branch locally when the speaker have the same branch name in your fork as the upstream repository?', 'How can the speaker push changes to a branch with a different name in your fork?', 'What is the workflow for pushing a local branch to a remote with a different name?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['How can the speaker work on a branch locally when the speaker have the same branch name in your fork as the upstream repository?', 'How can the speaker push changes to a branch with a different name in your fork?', 'What is the workflow for pushing a local branch to a remote with a different name?'], ["To work on a branch locally when the speaker have the same branch name in your fork as the upstream repository, the speaker can explicitly check out the branch from the remote and give it a special name to avoid collisions. For example, the speaker can use the command 'git checkout <remote_name>/<branch_name> -b <new_branch_name>' to check out the branch from your fork with a unique name.", "To push changes to a branch with a different name in your fork, the speaker can use the command 'git push <remote_name> HEAD:<new_branch_name>'. This command will push the changes from your local branch to the specified branch name in your fork.", "To push a local branch named 'acetylene__allow_ci_key' to the 'acentilli' remote with a different name, the speaker use the following command: git push acentilli acetylene__allow_ci_key:new_branch_name"]))
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
