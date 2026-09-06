import os
import json
from dotenv import load_dotenv
from groq import Groq

from tools import add_assignment, get_upcoming

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


tools = [
    {
        "type": "function",
        "function": {
            "name": "add_assignment",
            "description": "Add a student's assignment and its due date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the assignment"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Due date in YYYY-MM-DD format"
                    }
                },
                "required": ["name", "due_date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_upcoming",
            "description": "Get all stored assignments ordered by due date.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


messages = [
    {
        "role": "system",
        "content": """
You are an Assignment Deadline Tracker Agent.

Your job is to help students manage their assignments.

Use the tools when necessary.

When the user asks you to add an assignment, use add_assignment.

When the user asks what assignments are upcoming,
what is urgent, or what they should work on first,
use get_upcoming.

After receiving a tool result, analyze it and give the
user a useful final answer.
"""
    }
]


def run_agent(user_input):

    messages.append({
        "role": "user",
        "content": user_input
    })

    while True:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message

        # No more tools needed
        if not message.tool_calls:

            messages.append({
                "role": "assistant",
                "content": message.content
            })

            return message.content

        # Add the assistant's tool request to conversation
        messages.append(message)

        # Execute every requested tool
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            print(f"\n[Agent decided to call: {tool_name}]")

            if tool_name == "add_assignment":

                result = add_assignment(**arguments)

            elif tool_name == "get_upcoming":

                result = get_upcoming()

            else:

                result = {
                    "error": "Unknown tool"
                }

            print(f"[Tool result: {result}]")

            # Send tool result back to Groq
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })


if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        answer = run_agent(user_input)

        print("\nAgent:", answer)

