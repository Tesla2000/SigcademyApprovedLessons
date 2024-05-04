import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["What technologies are used to generate Anthony's YouTube thumbnails?", "Where can the speaker find the code for generating Anthony's thumbnails?", 'What package is being used to automate browser interactions in the code snippet?', "What is the purpose of the 'make_screenshot.py' script mentioned in the text?", "What is the purpose of the 'driver.get' function in Selenium?", 'How is the window size adjusted to create a thumbnail-sized screenshot in the script?', 'What is the recommended size for YouTube thumbnails according to the text?', 'What concept does Selenium have for handling windows?', 'What does the script do after determining the window handle to interact with?', 'How are panels on Twitch or offline pages generated according to the text?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["What technologies are used to generate Anthony's YouTube thumbnails?", "Where can the speaker find the code for generating Anthony's thumbnails?", 'What package is being used to automate browser interactions in the code snippet?', "What is the purpose of the 'make_screenshot.py' script mentioned in the text?", "What is the purpose of the 'driver.get' function in Selenium?", 'How is the window size adjusted to create a thumbnail-sized screenshot in the script?', 'What is the recommended size for YouTube thumbnails according to the text?', 'What concept does Selenium have for handling windows?', 'What does the script do after determining the window handle to interact with?', 'How are panels on Twitch or offline pages generated according to the text?'], ["The technologies used to generate Anthony's YouTube thumbnails include HTML, a browser for rendering, and Selenium WebDriver for scraping the screen.", "The code for generating Anthony's thumbnails can be found on Anthony's GitHub repository at github.com/AnthonyWritesCode/thumbnails.", 'Selenium', 'To take a screenshot of a webpage at a specific size for use as a thumbnail on YouTube.', 'To navigate to a specific URL in the browser.', 'A JavaScript script is used to open a new window with the exact size needed for a thumbnail.', '720p', 'Window handle', 'Run save screenshots and exit everything out', 'Automated process using HTML']))
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
