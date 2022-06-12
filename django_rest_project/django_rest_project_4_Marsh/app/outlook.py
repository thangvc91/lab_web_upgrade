import win32com.client as win32
def sendemail(email, password):
    template = '''
        <p>Hi <strong>Useremail</strong>,</p>
        <p><strong>You password is <span style="color: rgb(224, 62, 45);">password1</span></strong></p>
        <p>&nbsp;</p>
        <p><strong><span style="color: rgb(224, 62, 45);">Thank you for using our services</span></strong></p>
    '''
    template = template.replace('Useremail',email)
    template = template.replace('password1', password)
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = 'Im your password assistant'
    # mail.Body = 'Message body'
    mail.HTMLBody = template #this field is optional
    mail.Send() 
# To attach a file to the email (optional):
# attachment  = "Path to the attachment"
# mail.Attachments.Add(attachment)

