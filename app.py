import streamlit as st
import tiktoken

REMIT = """You are a College Library Assistant. 
You ONLY answer about: library timings (9am-6pm), books, membership, fines.
If outside, say: 'This is outside my remit.'"""

UNSAFE = ["bomb", "kill", "suicide", "weapon", "drug", "hack"]
OFF_TOPIC = ["cricket", "ipl", "politics", "movie", "game"]

def check_guardrails(q: str):
    q_low = q.lower()
    for w in UNSAFE:
        if w in q_low:
            return False, "Unsafe content blocked."
    for w in OFF_TOPIC:
        if w in q_low:
            return False, f"Off-topic. My remit is: {REMIT}"
    return True, "ok"

st.set_page_config(page_title="Grounded Assistant Capstone")
st.title("Grounded Assistant - Capstone FYIT")
st.info(REMIT)

q = st.text_input("Your question:")
if q:
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = len(enc.encode(REMIT + q))
    cost = tokens * 0.000002
    st.caption(f"Tokens: {tokens} | Est Cost: ${cost:.6f}")

    ok, msg = check_guardrails(q)
    if not ok:
        st.error(msg)
    else:
        st.success(f"Query allowed. Grounded answer for: {q}")
        st.write("Answer: Library is open 9am-6pm. Books can be issued for 7 days.")
