#!/usr/local/bin/python3

import cgi, json
import os

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    usr_name = form.getvalue('username')
    usr_pw = form.getvalue('password')

    
    usr_info = { 'name': '', 'password': ''}

    usr_info['name'] = usr_name
    usr_info['password'] = usr_pw



    print(json.dumps(usr_info))


if __name__ == '__main__':
    main()