import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the Git command being discussed in the video?', 'How is cherry-pick described in the video?', 'What is the purpose of cherry-pick according to the video?', 'How does the speaker decide which commit to cherry-pick in the video?', 'Can the speaker describe the process of cherry-picking a commit in Git as shown in the video?', 'What happens when a conflict occurs during a cherry-pick operation in Git according to the video?', 'What is the purpose of cherry-picking in Git?', 'How do the speaker resolve a merge conflict during a cherry-pick operation in Git?', "What does the '-m1' flag do in the 'git cherry-pick' command when cherry-picking a merge commit?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the Git command being discussed in the video?', 'How is cherry-pick described in the video?', 'What is the purpose of cherry-pick according to the video?', 'How does the speaker decide which commit to cherry-pick in the video?', 'Can the speaker describe the process of cherry-picking a commit in Git as shown in the video?', 'What happens when a conflict occurs during a cherry-pick operation in Git according to the video?', 'What is the purpose of cherry-picking in Git?', 'How do the speaker resolve a merge conflict during a cherry-pick operation in Git?', "What does the '-m1' flag do in the 'git cherry-pick' command when cherry-picking a merge commit?"], ['git cherry-pick', 'Cherry-pick is described as the process of taking a commit or a set of commits and replaying them in a different place in the repository.', 'The purpose of cherry-pick, as explained in the video, is to copy a commit to another branch in order to include specific changes in that branch.', 'In the video, the speaker mentions that in their workflow (specifically with pytest), they prefer to cherry-pick the merge commit instead of the actual commit to better reflect the original history.', "To cherry-pick a commit in Git, the speaker demonstrates switching to a different branch, running 'git cherry-pick' followed by the revision of the commit to be cherry-picked. If the changes apply cleanly, a new commit is created on the target branch with the same modifications as the original commit.", 'When a conflict occurs during a cherry-pick operation in Git, Git will indicate the conflicting files and show conflict markers. The user can then resolve the conflict by editing the files to resolve the differences.', 'Cherry-picking in Git allows the speaker to choose specific commits from one branch and apply them to another branch, allowing the speaker to selectively merge changes.', "To resolve a merge conflict during a cherry-pick operation in Git, the speaker can manually edit the conflicted files to resolve the conflicts, then add the changes and continue the cherry-pick using 'git cherry-pick --continue' command.", "The '-m1' flag in the 'git cherry-pick' command specifies that the speaker want to pick the changes from the first parent of the merge commit when cherry-picking a merge commit."]))
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
