# AI Projects

## Travel Planner Agent

An AI-powered travel planning assistant built using LangGraph, LangChain, Groq, FastAPI, PostgreSQL, and Next.js. This agent automates the end-to-end travel planning process by breaking down user requests into sub-tasks such as destination research, budget estimation, itinerary scheduling, and real-time booking suggestions. It uses stateful workflows to maintain context across multiple interactions, allowing users to refine their plans iteratively. The system integrates with external APIs for live data on weather, flights, hotels, and local attractions. Groq provides low-latency LLM inference for responsive conversational turnarounds, while PostgreSQL stores user profiles, past trips, and preference vectors for personalization. FastAPI handles asynchronous request processing, and Next.js delivers a dynamic, SEO-friendly frontend with server-side rendering and real-time updates.

Technologies:

- LangGraph
- LangChain
- Groq
- FastAPI
- PostgreSQL
- Next.js

---

## Document Editing Agent

An intelligent document editing assistant that reads, rewrites, summarizes, and improves documents using Retrieval-Augmented Generation (RAG) and large language models. Unlike basic text editors, this agent performs semantic understanding of document structure, tone, and audience. It applies multi-pass editing strategies: first parsing the document into semantic chunks, then generating improvement suggestions for clarity, coherence, and conciseness. The RAG pipeline retrieves relevant reference documents, style guides, or domain-specific knowledge bases to ground the edits in factual and contextual accuracy. The agent supports both extractive summarization (pulling key sentences) and abstractive summarization (generating new concise text). It can also transform documents between formal, academic, business, or casual tones. OpenAI's GPT-4 provides the primary generation backbone, while LangGraph orchestrates conditional workflows—for example, skipping summarization if the document is already short, or triggering deeper fact-checking for technical content.

Technologies:

- LangGraph
- OpenAI
- RAG

---

## AI Chatbot

A conversational AI assistant capable of answering user questions using large language models and contextual retrieval. This chatbot is designed for open-domain question answering with a focus on accuracy, relevance, and conversational fluidity. It uses a two-stage retrieval-augmented pipeline: first, it retrieves relevant passages from a vector database of documents, FAQs, or knowledge articles; second, it synthesizes a response using the retrieved context and the user's conversation history. The system supports multi-turn dialogues with memory management, allowing it to reference earlier exchanges and maintain topic coherence. Groq accelerates inference for near-instant responses, making the chatbot suitable for high-traffic customer support or internal knowledge assistance. The RAG component is continuously updated with new documents, enabling the chatbot to stay current without retraining the underlying LLM. It also includes confidence scoring to flag uncertain answers and fallback mechanisms for out-of-domain queries.

Technologies:

- LangChain
- Groq
- RAG
