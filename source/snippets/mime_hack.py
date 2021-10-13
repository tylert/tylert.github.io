#!/usr/bin/env python


import email


if __name__ == '__main__':

    with open('noname-2.eml', 'r') as fp:
        message = email.message_from_file(fp)

    index = 0

    for part in message.walk():

        if part.is_multipart() == False:
            with open(repr(index), 'wb') as fp:
                fp.write(part.get_payload(decode=True))

        index += 1


#import mimetypes
#    if part.get_content_maintype() == 'image':
#        filename = part.get_filename()
#        if not filename:
#            ext = mimetypes.guess_extension(part.get_content_type())
#            filename = 'image-%02d%s' % (i, ext or '.tiff')
