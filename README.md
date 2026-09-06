# Assignment Deadline Tracker Agent

## Project Overview

This project implements an AI agent that helps students manage assignment deadlines.

The agent uses two tools:

1. `add_assignment()` - stores an assignment and its due date.
2. `get_upcoming()` - retrieves assignments and orders them by deadline.

The agent maintains conversation memory so that assignments added in earlier turns can be used later when making priority decisions.

### Agent Workflow

User Goal → Agent Decision → Tool Call → Tool Result → Agent Decision → Final Response

The following demonstrations show that the system is an agent rather than a simple chatbot.
