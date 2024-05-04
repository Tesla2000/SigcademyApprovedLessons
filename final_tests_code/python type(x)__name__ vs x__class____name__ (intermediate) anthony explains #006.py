import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["Why did the speaker use 'type(self).__name__' instead of 'self.__class__.__name__' in the wrapper?", 'What should the speaker prefer in Python 3 and modern code when dealing with classes?', 'What was the purpose of the short video mentioned in the text?', 'Where can the speaker ask questions if the speaker have other stuff the speaker want to know about?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["Why did the speaker use 'type(self).__name__' instead of 'self.__class__.__name__' in the wrapper?", 'What should the speaker prefer in Python 3 and modern code when dealing with classes?', 'What was the purpose of the short video mentioned in the text?', 'Where can the speaker ask questions if the speaker have other stuff the speaker want to know about?'], ["The two are essentially equivalent in normal cases. However, using 'type(self).__name__' can avoid potential issues in special cases where a class may return a different class type than expected. Additionally, in Python 2, there are differences between old-style and new-style classes where 'type(self).__name__' may be preferred for compatibility with old-style classes.", "You should probably prefer using classes unless you're trying to figure out whether a class is spoofing.", 'The purpose of the short video was to provide an explanation on when to prefer using classes in Python 3 and modern code.', 'You can ask questions in chat, discord, twitch stream, or wherever the speaker prefer. The speaker is happy to answer them.']))
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
