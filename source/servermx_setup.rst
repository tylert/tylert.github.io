Webmail Access
Username:  firstname.lastname@domainname.tld
Password:  YOUREMAILPASSWORD
URLs:
1.  https://sogo.servermx.com  (has working calendar and contacts stuff)
2.  https://roundcube.servermx.com  (just webmail)
3.  https://afterlogic.servermx.com  (just webmail)
4.  https://squirrel.servermx.com  (just webmail)

Email Client Setup
Username:  firstname.lastname@domainname.tld
Password:  YOUREMAILPASSWORD
Incoming:  imap.servermx.com, SSL/TLS, port 993, normal password
Outgoing:  smtp.servermx.com, STARTTLS, port 587, normal password
Account name:  servermx
Display name:  Firstname Lastname
https://sogo.servermx.com/SOGo/dav/firstname.lastname%domainname%2Etld/Contacts/personal
https://sogo.servermx.com/SOGo/dav/firstname.lastname%domainname%2Etld/Calendar/personal

DAVdroid Setup
URL:  https://sogo.servermx.com/SOGo/dav
Username:  firstname.lastname@domainname.tld
Password:  YOUREMAILPASSWORD
Contacts:  Personal Address Book  (poll every 1 hour)
Calendar:  Personal Calendar  (poll every 1 hour)
Tasks:  Personal Calendar  (poll every 1 hour)
Account name:  firstname.lastname@domainname.tld

DNS Setup
priority 1, mx1.servermx.com
priority 2, mx1backup.servermx.com
"v=spf1 a mx include:servermx.com ~all"
"servermx.com.UNIQUEKEYPROVIDEDTOYOU"
