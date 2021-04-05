import dropbox

class Upload:
    def __init__(self,token):
        self.token = token
    def send(self,to,frm):
        d = dropbox.Dropbox(self.token)
        with open(frm,'rb') as s:
            d.files_upload(s.read(),to)

def main():
    token='sl.AuYUpbsrc_1jUN1lz0AyL466xTW5ZWqtHcbacOO2sDgJfBE48PnEquLQ-xo8aL1mtvivTS0Wu-Cm8tFTI5rTZVTaRG0mM2XtteVsXpR1CoEy8N1meIeYV3Y4zTLY5Poq5ceUcTFlpHI'
    upload = Upload(token)
    to = '/two.txt'
    frm = './two.txt'
    upload.send(to,frm)

main()


