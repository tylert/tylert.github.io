#!/usr/bin/env python

import base64


def b64_wtf(input_filename, output_filename):
    ''''''
    with open(input_filename, 'r') as input_file, \
            open(output_filename, 'wb') as output_file:
        encoded = input_file.read()
        data = base64.b64_decode(encoded)
        output_file.write(data)


if __name__ == '__main__':
    for item1, item2 in base64.__dict__:
        print('key={}'.format(item1))
        print('val={}'.format(item2))
    # b64_wtf(u'hostess.b64', u'tyler_test')
