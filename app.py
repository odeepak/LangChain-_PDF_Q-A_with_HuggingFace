import os

# ✅ Fixes for PyTorch/Protobuf/Streamlit issues on Windows
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# ✅ First Streamlit command
import streamlit as st
st.set_page_config(page_title="Chat with Your PDF 🤖", page_icon="🤖")

from qa_chain import load_qa_chain

# App title
st.title("🤖 Chat with Your PDF")

# File uploader
uploaded_file = st.file_uploader("📄 Upload a PDF", type="pdf")

# Load and process PDF on first upload
if uploaded_file and "qa_chain" not in st.session_state:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.session_state.qa_chain = load_qa_chain("temp.pdf")
    st.session_state.messages = []  # Store chat history
    st.success("✅ PDF uploaded successfully. You can start chatting!")

# Chat interface logic
if "qa_chain" in st.session_state:

    # Display past messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            if msg["role"] == "assistant":
                st.markdown(f"🤖 **Bot:** {msg['content']}")
            else:
                st.markdown(f"🧑 **You:** {msg['content']}")

    # Input for new question
    user_input = st.chat_input("Ask a question about the PDF...")

    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(f"🧑 **You:** {user_input}")

        # Generate and show bot response
        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                answer = st.session_state.qa_chain.run(user_input)
                st.markdown(f"🤖 **Bot:** {answer}")

        # Add bot response
        st.session_state.messages.append({"role": "assistant", "content": answer})
