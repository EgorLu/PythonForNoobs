## What changed?


### Questions

Questions are now stored in a separate JSON file, instead of being hard-coded in the program.

Questions format is as follows:
```json
[
    {
        "question": "",
        "answers": [
            "",
            "",
            "",
            ""
        ],
        "correct_answer": 1
    }
]
```
`answers` are enumerated automatically by order.
`correct_answer` is one-based index of the correct answer.

### Input validation

We now check the user's input when it comes to guessing the correct answer.

Ensuring that only the numbers 1-4 can be used and asking to repeat the input in case the previous one was illegal.