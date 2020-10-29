#ifndef __XSMTP_MESSAGES_H
#define __XSMTP_MESSAGES_H

const char reply_code[][100]={
	{" \r\n"},
	{"200 Mail is Successful.\r\n"},
	{"211 System status,system help reply.\r\n"},
	{"214 Message for help\r\n"},
	{"220 Ready\r\n"},
	{"221 Goodbye\r\n"},
	{"250 Okay, ready\r\n"},
	{"251 User is not local;forward to %s<forward-path>.\r\n"},

	{"354 Send from Rising mail proxy\r\n"},
	{"421 service not available, closing transmission channel\r\n"},
	{"450 Requested mail action not taken: mailbox unavailable\r\n"},
	{"451 Requested action aborted: local error in processing\r\n"},
	{"452 Requested action not taken: insufficient system storage\r\n"},
	{"500 Syntax error, command unrecognised\r\n"},
	{"501 Syntax error in parameters or arguments\r\n"},
	{"502 Error: command not implemented\r\n"},
	{"503 Error: bad sequence of commands\r\n"},
	{"504 Error: command parameter not implemented\r\n"},
	{"521 <domain>%s does not accept mail (see rfc1846)\r\n"},
	{"530 Access denied (???a Sendmailism)\r\n"},
	{"550 Mailbox requested is not availible\r\n"},
	{"551 User not local; please try <forward-path>%s\r\n"},
	{"552 Mail action aborted: storage needed\r\n"},
	{"553 Authentication is required\r\n"},

	{"250-mail \n250-PIPELINING \n250-AUTH LOGIN PLAIN\n250-AUTH=LOGIN PLAIN\n250 8BITMIME\r\n"},
	{"334 dXNlcm5hbWU6\r\n"},
	{"334 UGFzc3dvcmQ6\r\n"},  
	{"Log in Success, Authenticated\r\n"}
};

#endif