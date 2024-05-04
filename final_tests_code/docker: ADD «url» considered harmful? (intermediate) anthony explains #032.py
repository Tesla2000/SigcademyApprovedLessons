import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["Why did Anthony use curl instead of Docker's built-in ADD instruction to download files?", 'What is the purpose of test3 image compared to test2?', 'What is the downside of using curl for downloading files in test3 image?', 'How did the speaker validate the files in test3 image?', 'What is the difference in size between test2 and test3 images?', "Why does the speaker not use 'add' with URL for downloading files in Docker images?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["Why did Anthony use curl instead of Docker's built-in ADD instruction to download files?", 'What is the purpose of test3 image compared to test2?', 'What is the downside of using curl for downloading files in test3 image?', 'How did the speaker validate the files in test3 image?', 'What is the difference in size between test2 and test3 images?', "Why does the speaker not use 'add' with URL for downloading files in Docker images?"], ["Anthony used curl instead of Docker's built-in ADD instruction to download files because he found that using curl had some advantages over Docker's ADD instruction. One advantage is that using curl allows for safety checksumming, which enables validation of the downloaded file to ensure it is the expected file. Additionally, using curl helps to avoid adding temporary files to the final image, which can make the image size unnecessarily larger.", 'To compare the image sizes and demonstrate the installation of curl and CA certificates in test3.', 'Curl takes up about 10 megabytes of space in the image.', 'The speaker properly checksummed the files to ensure they were the expected ones.', 'Test3 is about 110 megabytes smaller than test2.', 'To have a better way to download files and validate them in Docker images.']))
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
