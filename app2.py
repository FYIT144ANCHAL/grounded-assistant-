import streamlit as st
import tiktoken

# Remit - Change this to your topic
REMIT = """
You are a College Library Assistant.
You ONLY answer about: library timings, books, membership, fines.
If user asks anything else, say: 'This is outside my remit.'
"""

UNSAFE = ["bomb", "kill", "suicide", "weapon", "drug", "hack"]
OFF_TOPIC = ["cricket", "ipl", "politics", "movie", "game", "stock"]

def check_guardrails(q: str):
    q_low = q.lower()
    for w in UNSAFE:
        if w in q_low:
            return False, "Unsafe request - I cannot help."
    for w in OFF_TOPIC:
        if w in q_low:
            return False, f"Off-topic. My remit is: {REMIT}"
    return True, "ok"

st.title("Grounded Assistant - Capstone")
st.info(REMIT)

query = st.text_input("Ask question:")
if query:
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = len(enc.encode(REMIT + query))
    cost = tokens * 0.000002
    st.write(f"Tokens: {tokens} | Cost: ${cost:.6f}")

    allowed, msg = check_guardrails(query)
    if not allowed:
        st.error(msg)
    else:
        st.success(f"Allowed - Would answer: {query}")
