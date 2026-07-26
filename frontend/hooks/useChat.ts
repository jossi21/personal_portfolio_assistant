"use client";
import { useEffect, useState } from "react";
import { sendMessage } from "@/services/chatApi";
import { ChatMessage, Language, Action } from "@/types/chat";
import { changeLanguage } from "@/services/languageApi";
import { getConversation } from "@/services/conversationApi";

const CHANGE_LANGUAGE_ACTION: Action = {
  label: "Change Language",
  type: "language",
  value: "change_language",
};

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [sessionId, setSessionId] = useState<string>();
  const [language, setLanguage] = useState<Language>("English" as Language);
  const [loading, setLoading] = useState(false);

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

  function resetChat() {
    localStorage.removeItem("session_id");
    setSessionId(undefined);
    setLanguage("en" as Language);
    setMessages([
      {
        role: "assistant",
        content: "",
        actions: [
          {
            label: "Change Language",
            type: "language",
            value: "change_language",
          },
        ],
      },
    ]);
  }

  useEffect(() => {
    async function loadConversation() {
      const savedSession = localStorage.getItem("session_id");

      if (!savedSession) {
        setMessages([
          {
            role: "assistant",
            content: "",
            actions: [
              {
                label: "Change Language",
                type: "language",
                value: "change_language",
              },
            ],
          },
        ]);
        return;
      }

      try {
        const data = await getConversation(savedSession);

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
