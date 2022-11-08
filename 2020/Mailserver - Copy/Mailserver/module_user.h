#ifndef __XSMTP_MODULE_USER_H
#define __XSMTP_MODULE_USER_H

#include "common.h"

int check_user();
void auth(int sockfd);
int check_name_pass(char* name, char* pass);
void user_quit();

#endif