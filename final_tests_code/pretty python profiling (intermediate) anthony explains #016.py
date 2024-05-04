import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What tool is being introduced in the video?', 'What tool is the focus of the video?', 'What is the specific issue being addressed with the tool in the video?', 'What is the minimum time that the tool could take according to the speaker?', 'What tool is used to analyze module import times?', 'What tool is used to analyze performance after the import time?', 'What tool do the speaker use to profile Python and C code?', 'What format is the output of the profiling data in?', 'What tool do the speaker use to visualize the profiling data?', 'What format do the speaker convert the visualization into for viewing?', 'How do the speaker prune the graph to focus on specific functions?', 'What function is taking 60 to 70% of a no op run?', 'Is it easy to fix the issue with the healthy function?', 'How do the speaker go about profiling stuff?', 'Where can I find the tools mentioned in the video?', 'How can viewers reach out to the speaker with questions?', 'Thank the speaker message']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What tool is being introduced in the video?', 'What tool is the focus of the video?', 'What is the specific issue being addressed with the tool in the video?', 'What is the minimum time that the tool could take according to the speaker?', 'What tool is used to analyze module import times?', 'What tool is used to analyze performance after the import time?', 'What tool do the speaker use to profile Python and C code?', 'What format is the output of the profiling data in?', 'What tool do the speaker use to visualize the profiling data?', 'What format do the speaker convert the visualization into for viewing?', 'How do the speaker prune the graph to focus on specific functions?', 'What function is taking 60 to 70% of a no op run?', 'Is it easy to fix the issue with the healthy function?', 'How do the speaker go about profiling stuff?', 'Where can I find the tools mentioned in the video?', 'How can viewers reach out to the speaker with questions?', 'Thank the speaker message'], ['Profiling performance profiling in Python.', 'Pre-commit.', 'A particular part of pre-commit is slow and needs improvement.', '120 milliseconds.', 'Import time waterfall.', 'C profile.', 'You use PStats to profile Python and C code.', 'The output of the profiling data is in a binary PStats format.', 'You use Yelp Gprof2Dot to visualize the profiling data.', 'You convert the visualization into an SVG format for viewing.', 'You prune the graph by specifying a root function using the -Z flag in Gprof2Dot.', 'The healthy function', "Yes, it is easy to fix but it hasn't been done yet.", 'This is how I go about profiling stuff.', 'The tools will be linked in the description for the speaker to check out.', 'Viewers can leave comments, reach out on Twitter, or join the Twitch stream.', 'Thank the speaker all for watching, and see the speaker in the next video!']))
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
