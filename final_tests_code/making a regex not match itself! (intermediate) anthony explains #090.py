import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What was the initial problem the person faced with their regex in the pre-commit framework?', 'What was the specific comment that the person wanted to block in the code base using the pre-commit hook?', 'What anchor in regular expressions did the person use to solve the problem of the regex matching itself?', "What are some ways to match a literal capital letter 'D' in a regex pattern?", 'When working with grep and trying to grep processes, how can the speaker ensure that the regex pattern does not match the grep process itself?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What was the initial problem the person faced with their regex in the pre-commit framework?', 'What was the specific comment that the person wanted to block in the code base using the pre-commit hook?', 'What anchor in regular expressions did the person use to solve the problem of the regex matching itself?', "What are some ways to match a literal capital letter 'D' in a regex pattern?", 'When working with grep and trying to grep processes, how can the speaker ensure that the regex pattern does not match the grep process itself?'], ['The regex was matching itself, causing the hook to trigger on its own entry.', "The person wanted to block the 'don't ship' comment from ending up in the code base.", "The person used the boundary anchor '\\b' in the regular expression to prevent the regex from matching itself.", "Some ways to match a literal capital letter 'D' in a regex pattern include using a character class with only the character 'D' inside, creating a trivial group, or making an empty parenthesis group.", 'To ensure that the regex pattern does not match the grep process itself, the speaker can put one of the characters in a bracket to make sure it no longer matches the grep process.']))
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
