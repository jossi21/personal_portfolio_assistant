"use client";

import ReactMarkdown from "react-markdown";
import ActionButtons from "./ActionButtons";
import { Action } from "@/types/chat";

type Message = {
  role: "user" | "assistant";
  content: string;
  actions?: Action[];
};

export default function MessageBubble({
  message,
  onAction,
}: {
  message: Message;
  onAction: (action: Action) => void;
}) {
  return (
    <div className="space-y-2">
      {message.content && (
        <div
          className={`flex ${
            message.role === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div
            className={`
              max-w-[85%]
              px-4
              py-2.5
              text-sm
              rounded-2xl
              ${
                message.role === "user"
                  ? "bg-indigo-500 text-white rounded-br-md"
                  : "bg-white  shadow-md rounded-bl-md text-zinc-700"
              }
            `}
          >
            {message.role === "assistant" ? (
              <ReactMarkdown>{message.content}</ReactMarkdown>
            ) : (
              message.content
            )}
          </div>
        </div>
      )}

      {message.role === "assistant" &&
        message.actions &&
        message.actions.length > 0 && (
          <ActionButtons actions={message.actions} onAction={onAction} />
        )}
    </div>
  );
}
