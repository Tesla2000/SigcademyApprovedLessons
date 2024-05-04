import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the series the speaker are planning to create?', 'How do the speaker plan to structure the episodes of the series?', 'Where can viewers submit ideas for topics or questions for the series?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the series the speaker are planning to create?', 'How do the speaker plan to structure the episodes of the series?', 'Where can viewers submit ideas for topics or questions for the series?'], ['The purpose of the series is to deep dive into various programming topics and explain them in detail, based on questions asked during Twitch streams or generated questions. The goal is to provide focused content without distractions from Twitch streaming, and to avoid unnecessary fluff at the beginning of videos.', 'The episodes will focus on answering questions related to programming topics, potentially including explanations of stream setups or other relevant subjects. The content will be presented in a one-take format to simplify editing and ensure a direct jump into the learning content without unnecessary delays.', 'Viewers can submit ideas for topics or questions in the comments section of the videos or during Twitch streams. The creator will consider interesting questions or commonly asked ones to create videos for the series.']))
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
