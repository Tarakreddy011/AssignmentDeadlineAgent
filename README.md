# Assignment Deadline Tracker Agent

## 1. Project Overview

This project is an AI-powered Assignment Deadline Tracker Agent.

The goal is to help students keep track of assignments and decide which assignment should be completed first.

I built this project using Python and the Groq API. The agent runs locally on my computer and uses the Groq model `openai/gpt-oss-20b`.

This is an agent, not just a chatbot, because it:
- Makes decisions based on the user's request.
- Calls Python tools to perform actions.
- Uses the results returned by those tools.
- Remembers assignments from earlier turns.
- Takes multiple steps before producing a final answer.


## 2. What We Built

The project was built step by step.

### Step 1 - Project Setup

First, I created a local project folder:

AssignmentDeadlineAgent

The project was kept completely local. No website or deployment was required.

I installed the required Python packages:

- groq
- python-dotenv
- jupyter

I also created a `.env` file to store the Groq API key safely.


### Step 2 - Created the First Tool

I created the first tool:

`add_assignment()`

Its purpose is to add an assignment and its deadline.

Example:

User:
"Add my AI assignment due on 2026-09-08"

The agent calls:

`add_assignment()`

The assignment is then stored locally.


### Step 3 - Created the Second Tool

I created the second tool:

`get_upcoming()`

Its purpose is to retrieve the assignments stored by the agent and order them according to their due dates.

For example:

AI Assignment → 2026-09-08
Database Management → 2026-09-12

The tool returns the assignments to the agent.


### Step 4 - Connected Groq

After creating the tools, I connected the Groq API to the project.

The Groq model is given access to both tools.

The model can decide which tool is required based on the user's request.

The Python program then executes the requested tool and sends the tool result back to the model.


### Step 5 - Built the Agent Loop

The agent uses a plan-act style loop:

User Request
↓
Agent decides what to do
↓
Agent calls a tool
↓
Python executes the tool
↓
Tool returns a result
↓
Agent receives the result
↓
Agent decides what to do next
↓
Final response

This makes the project an actual agent instead of a simple question-and-answer chatbot.


### Step 6 - Added Conversation Memory

The agent remembers assignments during the current conversation.

For example:

Turn 1:
"Add my Artificial Intelligence assignment due on September 8."

Turn 2:
"Add my Database Management assignment due on September 12."

Turn 3:
"Which assignment should I work on first?"

The agent remembers both assignments and calls `get_upcoming()`.

It receives:

1. Artificial Intelligence - September 8
2. Database Management - September 12

The agent then decides that Artificial Intelligence should be completed first because it has the earlier deadline.


### Step 7 - Created the Notebook Demo

I created `demo.ipynb` using Jupyter Notebook.

The notebook demonstrates:

1. Adding an Artificial Intelligence assignment.
2. Adding a Database Management assignment.
3. Asking the agent which assignment should be completed first.

The notebook also displays the tool calls and tool results so that the agent's multi-step behavior can be clearly demonstrated.


## 3. Tools Used

### Tool 1 - add_assignment()

Purpose:
Stores a new assignment and its due date.

Input:
- Assignment name
- Due date

Example:

`add_assignment("Artificial Intelligence", "2026-09-08")`


### Tool 2 - get_upcoming()

Purpose:
Retrieves all stored assignments and sorts them according to their deadlines.

Example result:

Artificial Intelligence → 2026-09-08
Database Management → 2026-09-12


## 4. Memory

The agent maintains conversation memory during the running session.

The assignment information stored by `add_assignment()` remains available to later requests.

The conversation messages are also maintained so that the agent can understand previous turns.

This allows a later request such as:

"Which assignment should I do first?"

to use information provided earlier in the conversation.


## 5. Example Agent Workflow

### User

Add my Artificial Intelligence assignment due on 2026-09-08.

### Agent

Decides to call `add_assignment()`.

### Tool

Stores the assignment and returns the result.

### User

Add my Database Management assignment due on 2026-09-12.

### Agent

Calls `add_assignment()` again.

### User

Which assignment should I work on first?

### Agent

Calls `get_upcoming()`.

### Tool

Returns the assignments ordered by deadline.

### Agent

Recommends Artificial Intelligence because its deadline is earlier.


## 6. Problem Faced During Development

Initially, I used a Groq model name that was not available for my API account.

The API returned a `model_not_found` error.

Instead of guessing, I checked the models available to my Groq API account and selected:

`openai/gpt-oss-20b`

After changing the model, the API connection and tool-calling workflow worked successfully.


## 7. Project Files

`agent.py`
- Contains the Groq connection and agent loop.

`tools.py`
- Contains `add_assignment()` and `get_upcoming()`.

`demo.ipynb`
- Contains the project demonstration and multi-step trace.

`README.md`
- Contains project documentation.

`requirements.txt`
- Contains the Python packages required to run the project.

`.env`
- Stores the Groq API key locally.
- This file should NOT be submitted.


## 8. How to Run

Install the required packages:

`pip install -r requirements.txt`

Make sure the `.env` file contains the Groq API key.

Run the agent:

`python agent.py`

For the notebook demonstration:

`jupyter notebook`

Then open:

`demo.ipynb`


## 9. Final Result

The final system is a local AI Assignment Deadline Tracker Agent.

It satisfies the main project requirements:

- Two working tools
- Multi-step agent loop
- Conversation memory
- Tool results used for decision-making
- Notebook demonstration with tool traces
