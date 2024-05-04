import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the topic of the video?', 'What was the mistake made in the commit shown in the video?', 'What command is used to amend the previous commit to remove the unwanted changes?', 'What warning is given about editing commit history in git?', 'What type of rebase is used in the second scenario shown in the video?', 'What is the purpose of interactive rebase in Git?', "What does changing 'pick' to 'edit' do in an interactive rebase?", 'How can the speaker prevent the editor from showing up during an interactive rebase?', 'What does git rebase allow the speaker to do?', 'What are the options to meld two commits together in git rebase?', 'What does the fix-up option do in git rebase?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the topic of the video?', 'What was the mistake made in the commit shown in the video?', 'What command is used to amend the previous commit to remove the unwanted changes?', 'What warning is given about editing commit history in git?', 'What type of rebase is used in the second scenario shown in the video?', 'What is the purpose of interactive rebase in Git?', "What does changing 'pick' to 'edit' do in an interactive rebase?", 'How can the speaker prevent the editor from showing up during an interactive rebase?', 'What does git rebase allow the speaker to do?', 'What are the options to meld two commits together in git rebase?', 'What does the fix-up option do in git rebase?'], ['Fixing mistakes in commits using git rebase workflows.', "Accidentally committing an unrelated joke alias 'get good' along with the intended changes.", 'git commit --amend.', 'Editing commit history will require a force push and may cause issues with fast-forward pushes.', 'Interactive rebase.', 'Interactive rebase in Git allows the speaker to modify commit history by rewinding and replaying commits one at a time. It provides a way to edit, reorder, merge, and squash commits in a more controlled and interactive manner.', "Changing 'pick' to 'edit' in an interactive rebase stops the rebase process at that specific commit, allowing the speaker to modify the commit before continuing with the rebase operation.", "You can prevent the editor from showing up during an interactive rebase by using the '--no-edit' flag when committing the changes. This flag skips the commit message editing step and proceeds with the commit directly.", 'Git rebase allows the speaker to reorder and merge commits together.', 'The options to meld two commits together in git rebase are squash and fix-up.', 'The fix-up option in git rebase allows the speaker to meld two commits together without changing the commit message.']))
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
