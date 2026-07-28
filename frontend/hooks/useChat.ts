"use client";

import { useEffect, useState } from "react";
import { sendMessage } from "@/services/chatApi";
import { ChatMessage, Language } from "@/types/chat";
import { changeLanguage } from "@/services/languageApi";
import { getConversation } from "@/services/conversationApi";

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [sessionId, setSessionId] = useState<string>();
  const [language, setLanguage] = useState<Language>("English" as Language);
  const [loading, setLoading] = useState(false);

  // Normal chat messages
  async function chat(text: string) {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: text,
      },
    ]);

    setLoading(true);

    try {
      const response = await sendMessage({
        session_id: sessionId,
        message: text,
      });

      setSessionId(response.session_id);

      localStorage.setItem("session_id", response.session_id);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.answer,
          actions: response.actions,
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  // First welcome message
  async function startConversation() {
    setLoading(true);

    try {
      const response = await sendMessage({
        message: "/start",
      });

      setSessionId(response.session_id);

      localStorage.setItem("session_id", response.session_id);

      setMessages([
        {
          role: "assistant",
          content: response.answer,
          actions: response.actions,
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  async function updateLanguage(newLanguage: Language) {
    if (!sessionId) return;

    setLoading(true);

    try {
      const response = await changeLanguage(sessionId, newLanguage);

      setLanguage(newLanguage);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.answer,
          actions: response.actions,
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  async function resetChat() {
    localStorage.removeItem("session_id");

    setSessionId(undefined);

    setLanguage("English" as Language);

    setMessages([]);

    // create new welcome session
    await startConversation();
  }

  useEffect(() => {
    async function loadConversation() {
      const savedSession = localStorage.getItem("session_id");

      // First visit
      if (!savedSession) {
        await startConversation();

        return;
      }

      try {
        const data = await getConversation(savedSession);

        setSessionId(savedSession);

        setLanguage(data.language);

        const history = data.history.map((item: string) => {
          const isUser = item.startsWith("User:");

          return {
            role: isUser ? "user" : "assistant",

            content: item.replace("User:", "").replace("Assistant:", "").trim(),
          };
        });

        setMessages(history);
      } catch (error) {
        localStorage.removeItem("session_id");

        await startConversation();
      }
    }

    loadConversation();
  }, []);

  return {
    messages,
    chat,
    loading,
    language,
    updateLanguage,
    resetChat,
  };
}
