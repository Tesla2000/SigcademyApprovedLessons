Existing and new lessons must be structured in a following way:

- `SigcademyApprovedLessons/`:  !Important! both lesson and final test must be present in order to create lesson successfully
  - `approved_lessons/`: All approved lessons that are to be created are stored there
    - `[lesson_name].json` file contains information needed for lesson creation.
  - `final_tests/`: All final tests for approved lessons, their goal is to check whether a trainee has necessary skills it is fully independent of training materials.
    - `[lesson_name].json`: file contains information needed for final test creation.
  - `final_tests_code/`: Directory to store files for dynamic question creation and scoring 
    - `[lesson_name].py`: file corresponding to specific final test [Optional]

  - `html_files/`: Holds html files.

  - `training_materials/`: Holds training materials.
    - `[lesson_name]/`: Folder containing training materials for specific lesson.
      - `[author]/`: folder containing training material itself.
        - `.json`: file contains information needed for training material creation.
        - `[step_number].json`: file contains information needed for creation of training material step.
        - `[step_number].html`: file html visible to trainee during step training.
        - `[step_number].py`: file responsible for dynamic question creation and scoring.
  - `default_users.txt`: Files holding default users initiated with student privileges.

# Lesson

## approved_lessons .json example
```json
{
  "description": "",
  "author": "",
  "basic_requirements": [""]  # lessons required to perform this lesson
}
```
## final_tests .json example
```json
{
  "questions": [""],  # hard-coded questions
  "answers": [""],  # hard-coded answers
  "html_file": "" # html file name <- must be present in html_files folder
}
```

# training material 
## .json file
```json
{
  "expected_step_times": [300],  # expected time of compleation for each step (to provide feedback to oversears)
  "author": "",
  "video_path": ""  # video path for final test
}
```

Video path can be either YouTube url example: https://www.youtube.com/watch?v=dQw4w9WgXcQ or space separated url to download file and sha256 hash of this file example https://drive.google.com/uc?export=download&id=1t0fSasHVB_f5XI70j00EYuDvCS_2n6Sb b8985194ae83d6dd5e5862c5bc9db548c71bcb120e81bf0c86f8b856a5a45a44.
## [Step number].json
```json
{
  "questions": [""],
  "answers": [""],
  "video_path": "https://drive.google.com/uc?export=download&id=1t0fSasHVB_f5XI70j00EYuDvCS_2n6Sb b8985194ae83d6dd5e5862c5bc9db548c71bcb120e81bf0c86f8b856a5a45a44"
}
```

# Both
## file for dynamic question creation

```python
def generate_questions() -> list[str]:
    return ["", ""]  # typically in html


def generate_answers(question: str, answer: str, file: str) -> bool | str:
    """True if correct comment otherwise, file or answer can be _ if they are not necessary"""
    try:
        if iscorrect(question, answer, file):
            return True
        return ""
    except:
        return ""
```

