# **📌 Glossary of AI Agent and LLM Terms**  

This glossary contains key terms encountered in the course, covering AI Agents, LLMs, and essential concepts in modern AI systems.

---

## **A**
- **AI Agent** → A system that uses an AI model to interact with its environment, reason, plan, and execute actions.
- **API Interface** → A tool that allows an AI Agent to interact with external APIs, such as GitHub, YouTube, or Spotify.
- **Attention Mechanism** → A fundamental part of the Transformer architecture that helps the model focus on the most relevant parts of an input sequence.
- **Autoregressive Model** → A type of AI model that generates sequences one token at a time, using previously generated tokens as context.

---

## **B**
- **Base Model** → A pre-trained model that predicts the next token but is not fine-tuned for specific tasks.
- **Beam Search** → A decoding strategy that considers multiple possible sequences to choose the best one.

---

## **C**
- **Chat Template** → A predefined structure that formats messages between a user and an AI assistant to maintain consistency.
- **Code AI Agent** → An AI Agent that generates and executes code to solve tasks instead of just returning structured responses.
- **Context Length** → The maximum number of tokens an LLM can process in a single input.
- **Conversation History** → A sequence of previous user and assistant messages, structured into a single prompt.
- **Cycle: Thought → Action → Observation** → The iterative workflow AI Agents follow to make decisions and act in their environment.

---

## **D**
- **Decoder** → A type of Transformer that generates output sequences token by token (e.g., LLaMA, GPT).
- **Decoding Strategy** → The method used to select the next token in text generation (e.g., greedy decoding, beam search).
- **Domain-Specific Tool** → A tool designed for a particular field or application, such as financial analysis or medical diagnostics.
- **Dummy Agent Library** → A minimal AI Agent implementation used for educational purposes, helping to understand AI Agent fundamentals.

---

## **E**
- **Encoder** → A type of Transformer that processes input text into embeddings but does not generate text.
- **EOS (End of Sequence) Token** → A special token used by LLMs to indicate the end of a generated response.
- **Embedding** → A dense numerical representation of text used for machine understanding.
- **Execution (Tool Invocation)** → The process of an AI Agent calling and executing an external function.

---

## **F**
- **Fine-Tuning** → The process of further training a pre-trained model on specific data to adapt it for a new task.
- **Function-Calling Agent** → A type of AI Agent that generates structured function calls (e.g., JSON actions) instead of direct responses.
- **Final Answer Tool** → A tool that ensures an AI Agent correctly formats and provides a conclusive response.

---

## **G**
- **Greedy Decoding** → A simple decoding strategy that always selects the token with the highest probability.
- **Grammar Constraints** → Rules that restrict how an AI Agent generates output to ensure structured formatting.

---

## **I**
- **Inference** → The process of using a trained LLM to generate predictions based on input text.
- **Instruction-Tuned Model (Instruct Model)** → A model fine-tuned to follow instructions and engage in structured conversations.
- **Iteration** → The repeated execution of the Thought → Action → Observation cycle in an AI Agent.

---

## **J**
- **JSON AI Agent** → An AI Agent that generates and processes actions in JSON format, typically for structured automation.
- **JSON Blob** → A formatted JSON object used by an AI Agent to define actions and parameters.

---

## **L**
- **LLM (Large Language Model)** → An AI model trained on vast text datasets to understand and generate natural language.
- **LLM-Powered Agent** → An AI Agent that uses an LLM as its core reasoning engine.
- **LlamaIndex** → A library that enables efficient retrieval and search within AI Agents.

---

## **M**
- **Message Formatting** → The structuring of user and assistant messages in a format that an LLM can process.
- **Multi-Turn Conversation** → A conversation where the LLM maintains context across multiple exchanges.
- **Memory Integration** → The process by which an AI Agent remembers past interactions to improve responses.

---

## **N**
- **Next Token Prediction** → The core function of an LLM, where it predicts the next token based on previous ones.
- **Natural Language Processing (NLP)** → A field of AI focused on understanding and generating human language.

---

## **O**
- **Observations** → Data or feedback that an Agent gathers from its environment before making a decision.
- **Optimization (Parameter Tuning)** → The process of adjusting model settings (temperature, token limits) to improve performance.

---

## **P**
- **Pre-Training** → The initial training phase of an LLM on a large dataset to learn language patterns.
- **Prompt Engineering** → The practice of crafting input text to guide the model’s response effectively.
- **Planning Interval** → A set period in which an AI Agent re-evaluates its strategy before taking an action.
- **Python API Client** → A wrapper library that enables interaction with AI models via API requests.

---

## **R**
- **Reasoning** → The ability of an AI Agent to analyze information and make logical decisions.
- **Retrieval-Augmented Generation (RAG)** → A method where an AI Agent retrieves external knowledge before generating a response.
- **Retrieval Tool** → A tool that fetches information from an external knowledge base.

---

## **S**
- **Seq2Seq Model (Sequence-to-Sequence)** → A Transformer model that includes both an encoder and a decoder, commonly used for tasks like translation or summarization.
- **Serverless API** → A cloud-based API that allows inference without requiring local model installation.
- **Special Tokens** → Unique tokens used to mark sections of text, such as EOS tokens or role delimiters in chat templates.
- **Stop Token** → A predefined token that signals an LLM to stop generating output.
- **System Message** → A persistent instruction given to the LLM to define its behavior.
- **SmolAgents** → A lightweight AI Agent framework for building simple and functional AI workflows.

---

## **T**
- **Tool** → A function that extends an AI Agent’s capabilities by allowing it to perform external tasks (e.g., calculations, API calls).
- **Tool Invocation** → The process of an LLM generating a function call, which the Agent executes.
- **Tokenization** → The process of breaking text into smaller units (tokens) for an LLM to process.
- **Transformer** → The neural network architecture that powers modern LLMs, based on self-attention mechanisms.
- **Text Generation API** → An endpoint that allows an AI Agent to generate text via external API requests.
- **Text-to-Image Tool** → A tool that converts text prompts into images using AI models.

---

## **U**
- **User Message** → A message input from the user in a chat interface.
- **Utility Tool** → A tool that performs basic calculations or processing for an AI Agent.

---

## **W**
- **Web Search Tool** → A tool that enables an AI Agent to fetch up-to-date information from the internet.
- **Workflow** → The sequence of steps an AI Agent follows: **Observe → Think → Act**.
- **Weight Parameters** → The internal numerical values in an LLM that define how it processes and generates text.

---

## **Z**
- **Zero-Shot Learning** → The ability of an AI model to perform tasks it has never explicitly been trained on.

---

### **Summary**
This glossary provides a **comprehensive reference for AI Agent terminology**, including key concepts, model architectures, and specialized tools. Understanding these terms is essential for effectively building and deploying AI-powered Agents. 
