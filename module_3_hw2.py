def send_email(message, recipient, *, sender='university.help@gmail.com'):
    message = str(message)
    recipient = str(recipient)
    sender = str(sender)
    variants = ('.com', '.ru', '.net')
    if '@' not in recipient or not (recipient.endswith(variants)) or '@' not in sender or not (sender.endswith(variants)):
        print('невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    if sender == recipient:
        print('нельзя отправить письмо самому себе')
    if recipient == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса:', sender, 'на адрес: ', recipient)
    else:
        print('нестандартный отправитель! Письмо отправлено с адреса: ', sender, 'на адрес: ', recipient)

    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

