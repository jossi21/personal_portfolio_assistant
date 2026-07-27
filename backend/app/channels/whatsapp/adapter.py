# class WhatsAppAdapter:


#     def parse_message(self,data):

#         message = data["entry"][0]["changes"][0]["value"]


#         return {

#             "user_id":
#             message["messages"][0]["from"],

#             "message":
#             message["messages"][0]["text"]["body"],

#             "channel":"whatsapp"
#         }