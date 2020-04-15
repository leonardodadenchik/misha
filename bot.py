import telebot
import random

name=['э','ъ','ы',]

bot = telebot.TeleBot('1154140248:AAHpn76FaINWi1On0SwqrHE6-HWC8cBLeF8')

@bot.message_handler(commands=["rules"])
def handler_text(message):
    bot.reply_to(message, 'Правила: \n  1) Заборонена агресія стосовно інших учасників.  \n 2) Ми не зацікавленні в флуді, спамі і нескінченних суперечках. \n 3) Ми використовуємо в чаті загальнозрозумілу українську мову. Репліки, контент і репости з каналів мовою вбивць і окупантів заборонені. \n 4) Тут можуть бути лише люди з Київської області, бажано лівобережжя.')


@bot.message_handler(content_types=["text"])
def handle_text(lol):
     mess=str(lol.text)
     mess=mess.lower()
     for i in range(3):
        if name[i] in mess:
            misha = random.randint(1,3)
            if misha == 1:
                bot.reply_to(lol,'@oblakon - ти секс, а ще тут рос!!!')
            elif misha == 2:
                bot.reply_to(lol,'@ShadowTemplar - це злий пан вчитель, тож зараз він надає тобі піздюлів за рос мову')
            elif misha == 3:
                bot.reply_to(lol,'@Reykoslid - Хитра срака пердить тихо, зате бан за рос виписує на все життя')


@bot.message_handler(content_types=["new_chat_members"])
def handler_text(mem):
    bot.reply_to(mem, 'Вітаю в групі новачку,у нас є одне важливе правило, російська мова в будь яких її проявах заборонена, а інші правила ти можеш прочитати в описі групи, приємного спілкування https://t.me/animka_darnytsya/13')




if 1 == 1:
     bot.infinity_polling()
