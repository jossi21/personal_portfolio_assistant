# from app.models.channel import ChannelMessage
# from app.models.chat import ChatResponse


# class WhatsAppAdapter:

#     def parse_message(
#         self,
#         request: dict
#     ) -> ChannelMessage:

#         message = (
#             request["entry"][0]
#             ["changes"][0]
#             ["value"]
#             ["messages"][0]
#         )

#         return ChannelMessage(
#             user_id=message["from"],
#             channel="whatsapp",
#             message=message["text"]["body"],
#             session_id=message["from"]
#         )


#     def format_response(
#         self,
#         response: ChatResponse
#     ):

#         return {
#             "message": response.answer,
#             "actions": [
#                 {
#                     "label": action.label,
#                     "value": action.value,
#                     "type": action.type
#                 }
#                 for action in (response.actions or [])
#             ]
#         }