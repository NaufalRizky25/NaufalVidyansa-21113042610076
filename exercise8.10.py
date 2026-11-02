def show_messages(messages_list):
    for message in messages_list:
        print(message)


def send_message(message_list, sentMessagelist):
    while message_list:
        currentMessage = message_list.pop()
        print(f"{currentMessage} sedang dikirim")
        sentMessagelist.append(currentMessage)

    return message_list, sentMessagelist


message_list = [
    "Halo, apa kabar?",
    "Jangan lupa makan siang ya.",
    "Apakah tugasnya sudah selesai?",
    "Sampai jumpa nanti malam!"
]
sentMessagelist = []
print("Berikut pesan yang belum terkirim: ")
print("Pesan belum terkirim: ", message_list)
print("Pesan terkirim: ", sentMessagelist)

send_message(message_list, sentMessagelist)

print("Berikut merupakan pesan yang telah terkirim: ")
print("Pesan belum terkirim: ", message_list)
print("Pesan terkirim: ", sentMessagelist)
