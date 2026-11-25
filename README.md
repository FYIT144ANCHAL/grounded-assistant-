# grounded-assistant-
Capstone Task: Grounded assistant with guardrails, eval set and cost tracking

## Remit
College Library Assistant - Only answers about library timings (9am-6pm), books, membership, fines.

## Features
- Guardrails: blocks unsafe (bomb, kill etc) and off-topic (cricket, politics etc)
- Cost Tracking: uses tiktoken cl100k_base to show tokens and cost
- Eval Set: eval_set.jsonl with safe, off_topic, unsafe cases

## How to Run
pip install -r requirements.txt
streamlit run app.py
