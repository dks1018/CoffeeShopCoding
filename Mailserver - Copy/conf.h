#ifndef __XSMTP_CONF_H
#define __XSMTP_CONF_H

#define PORT 25  // configuration of mail on port 25
#define MAX_CLIENTS 32
#define MAX_RCPT_USR 50
#define BUF_SIZE 1024

const char data_dir[] = "/root/Documents/git/repos/xsmtp/data/"; // retrieve information
const char userinfo[] = "userinfo";
const char userstat[] = "userstat";

extern int mail_stat;
extern int rcpt_user_num;
extern char from_user[64];
extern char rcpt_user[MAX_RCPT_USR][30];

#endif
