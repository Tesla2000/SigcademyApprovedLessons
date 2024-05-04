import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What was the technique Anthony learned about in the video?', 'What was the problem with the commit Anthony showed in the video?', 'What parameter did Anthony use to ignore whitespace in Git commands?', "How did Anthony use the -w parameter in the 'git show' command?", 'What did Anthony suggest as a better approach for committing changes related to indentation and adding a line of code?', "What additional option did Anthony mention using with 'git blame' command?", 'How did Anthony enable whitespace only mode on GitHub for a commit?', 'What does question mark W equals one do?', 'How can question mark W equals one be used in reviewing changes on pull requests?', 'What should the speaker do if the speaker have additional questions or need further explanations?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What was the technique Anthony learned about in the video?', 'What was the problem with the commit Anthony showed in the video?', 'What parameter did Anthony use to ignore whitespace in Git commands?', "How did Anthony use the -w parameter in the 'git show' command?", 'What did Anthony suggest as a better approach for committing changes related to indentation and adding a line of code?', "What additional option did Anthony mention using with 'git blame' command?", 'How did Anthony enable whitespace only mode on GitHub for a commit?', 'What does question mark W equals one do?', 'How can question mark W equals one be used in reviewing changes on pull requests?', 'What should the speaker do if the speaker have additional questions or need further explanations?'], ['Comparing whitespace in Git commits.', 'The commit was hard to follow because it reinvented the file and attributed all lines to the same commit.', 'The -w parameter.', "He used 'git show <commit> -w' to only show the one line that changed.", 'To make separate commits for updating the indentation and adding the line of code.', "He mentioned using the -M option with 'git blame'.", "By adding '?W=1' to the end of the commit URL in the address bar.", 'Enables white space only mode to show changes on one line only.', 'It can be used to ignore all the whitespace changes and focus on the actual code changes.', 'Leave a comment below, reach out on various platforms, or join the Twitch stream for more information.']))
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
