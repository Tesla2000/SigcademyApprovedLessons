import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['How does Anthony recommend getting started with programming?', 'What is the suggestion for learning more advanced or specific topics in programming?', 'What is the recommendation for a website to learn Python programming?', 'Why is it important to find a project to work on when learning programming?', 'Can the speaker provide an example of a project that was created during the learning process?', 'What was the main idea behind the program the speaker wanted to write?', 'What challenges did the speaker face while working on the program?', 'What advice do the speaker have for someone looking for programming project ideas?', 'What message do the speaker have for aspiring programmers?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['How does Anthony recommend getting started with programming?', 'What is the suggestion for learning more advanced or specific topics in programming?', 'What is the recommendation for a website to learn Python programming?', 'Why is it important to find a project to work on when learning programming?', 'Can the speaker provide an example of a project that was created during the learning process?', 'What was the main idea behind the program the speaker wanted to write?', 'What challenges did the speaker face while working on the program?', 'What advice do the speaker have for someone looking for programming project ideas?', 'What message do the speaker have for aspiring programmers?'], ['Anthony recommends starting by picking a programming language, such as Python, Ruby, or JavaScript. He suggests focusing on one language and getting proficient at it before branching out to others. He emphasizes the importance of practical application and building things for learning. Anthony also recommends resources like learnpython.org for learning the basics of Python syntax.', 'To explore topics like web development or data science and find projects that are personally motivating to work on.', 'Real Python, which offers structured tutorial content in the form of blog posts.', 'Working on a project that has personal value can increase motivation, improve learning, and encourage self-learning through problem-solving.', 'A program that reminded the user to take their dogs in and out at regular intervals, with a sound notification and a tray icon display.', 'The main idea was to write a simple program that made life easier and also helped in learning new things like playing sound in a Windows application and dealing with timers.', 'I faced synchronization issues while dealing with timers, and I also wanted to make the right-click menu work on the tray icon.', "Find a project to work on and build it to completion. If you're having trouble finding ideas, the speaker can Google beginner programming project ideas for resources and inspiration.", 'I hope your journey through programming is great and enjoyable. Keep learning and exploring new things in the field. Thank the speaker for watching and best of luck on your programming journey!']))
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
