import imaplib

class Mail:
    """ Access info from mail inbox """
    def __init__(self, address, password):
        self.address = address
        self.password = password

    def get_unread_mail_count(self):
        """ 
        Simply fetches the number of unread emails in an inbox. 
        Mine is currently set to Gmail, but the imap settings can be changed
        for other inboxes. 

        Like weather, I should store this in a database and only update the value
        every minute or two because it takes a bit of time to fetch.
        """
        try:
            imap_object = imaplib.IMAP4_SSL('imap.gmail.com', '993')
            imap_object.login(self.address, self.password)
            imap_object.select()
            number_unread = str(len(imap_object.search(None, 'UnSeen')[1][0].split())) 
        except:
            number_unread = '?'
        return number_unread + ' unread'
