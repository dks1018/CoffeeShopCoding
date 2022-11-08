#include "module_mail.h"
#include "module_user.h"

void *library_mail(void* param) {
	int client_sockfd, len;
	char buf[BUF_SIZE];

	memset(buf, 0, sizeof(buf));
	client_sockfd = *(int*) param;

	send_data(client_sockfd, reply_code[4]);
	mail_stat = 1;

	while (1) {
		memset(buf, 0, sizeof(buf));
		len = recv(client_sockfd, buf, sizeof(buf), 0);
		if (len > 0) {
			cout << "Request stream: " << buf;
			respond(client_sockfd, buf);
		} else {
			sleep(1);
			continue;
		}
	}
	cout << "S:[" << client_sockfd << "] socket closed by client." << endl;
	cout << "*--------------------------------------------------------*\n\n";
	return NULL;
}

void respond(int client_sockfd, char* request) {
	char output[1024];
	memset(output, 0, sizeof(output));

	if (strncmp(request, "HELO", 4) == 0) {
		if (mail_stat == 1) {
			send_data(client_sockfd, reply_code[6]);
			rcpt_user_num = 0;
			memset(rcpt_user, 0, sizeof(rcpt_user));
			mail_stat = 2;
		} else {
			send_data(client_sockfd, reply_code[15]);
		}
	} else if (strncmp(request, "MAIL FROM", 9) == 0) {
		if (mail_stat == 2 || mail_stat == 13) {
			char *pa, *pb;
			pa = strchr(request, '<');
			pb = strchr(request, '>');
			strncpy(from_user, pa + 1, pb - pa - 1);
			if (check_user()) {
				send_data(client_sockfd, reply_code[6]);
				mail_stat = 3;
			} else {
				send_data(client_sockfd, reply_code[15]);
			}
		} else if (mail_stat == 12) {
			send_data(client_sockfd, reply_code[23]);
		} else {
			send_data(client_sockfd, "503 Error: send HELO/EHLO first\r\n");
		}
	} else if (strncmp(request, "RCPT TO", 7) == 0) {
		if ((mail_stat == 3 || mail_stat == 4) && rcpt_user_num < MAX_RCPT_USR) {
			char *pa, *pb;
			pa = strchr(request, '<');
			pb = strchr(request, '>');
			strncpy(rcpt_user[rcpt_user_num++], pa + 1, pb - pa - 1);
			send_data(client_sockfd, reply_code[6]);
			mail_stat = 4;
		} else {
			send_data(client_sockfd, reply_code[16]);
		}
	} else if (strncmp(request, "DATA", 4) == 0) {
		if (mail_stat == 4) {
			send_data(client_sockfd, reply_code[8]);
			mail_data(client_sockfd);
			mail_stat = 5;
		} else {
			send_data(client_sockfd, reply_code[16]);
		}
	} else if (strncmp(request, "RSET", 4) == 0) {
		mail_stat = 1;
		send_data(client_sockfd, reply_code[6]);
	} else if (strncmp(request, "NOOP", 4) == 0) {
		send_data(client_sockfd, reply_code[6]);
	} else if (strncmp(request, "QUIT", 4) == 0) {
		mail_stat = 0;
		user_quit();
		send_data(client_sockfd, reply_code[5]);
		pthread_exit((void*)1);
	}

	else if (strncmp(request, "EHLO", 4) == 0) {
		if (mail_stat == 1) {
			send_data(client_sockfd, reply_code[24]);
			mail_stat = 12;
		} else {
			send_data(client_sockfd, reply_code[15]);
		}
	} else if (strncmp(request, "AUTH LOGIN", 10) == 0) {
		auth(client_sockfd);
	} else if (strncmp(request, "AUTH LOGIN PLAIN", 10) == 0) {
		auth(client_sockfd);
	} else if (strncmp(request, "AUTH=LOGIN PLAIN", 10) == 0) {
		auth(client_sockfd);
	} else {
		send_data(client_sockfd, reply_code[15]);
	}
}

void send_data(int sockfd, const char* data) {
	if (data != NULL) {
		send(sockfd, data, strlen(data), 0);
		cout << "Reply stream: " << data;
	}
}

void mail_data(int sockfd) {
	sleep(1);
	char buf[BUF_SIZE];
	memset(buf, 0, sizeof(buf));
	recv(sockfd, buf, sizeof(buf), 0);
	cout << "Mail Contents: \n" << buf << endl;

	int tm = time(NULL), i;
	char file[80], tp[20];

	for (i = 0; i < rcpt_user_num; i++) {
		// str cpy change
		strncpy(file, data_dir, 100);
		// str cpy change
		strncat(file, rcpt_user[i], 100);
		if (access(file,0) == -1) {
			mkdir(file,0777);
		}
		sprintf(tp, "/%d", tm);
		//str cat change
		strncat(file, tp, 100);

		FILE* fp = fopen(file, "w+");
		if (fp != NULL) {
			fwrite(buf, 1, strlen(buf), fp);
			fclose(fp);
		} else {
			cout << "File open error!" << endl;
		}
	}
	send_data(sockfd, reply_code[6]);
}

char *base64_decode(char *s) { 
	char *p = s, *e, *r, *_ret;
	int len = strlen(s);
	unsigned char i, unit[4];

	e = s + len;
	len = len / 4 * 3 + 1;
	r = _ret = (char *) malloc(len);

	while (p < e) {
		memcpy(unit, p, 4);
		if (unit[3] == '=')
			unit[3] = 0;
		if (unit[2] == '=')
			unit[2] = 0;
		p += 4;

		for (i = 0; unit[0] != B64[i] && i < 64; i++)
			;
		unit[0] = i == 64 ? 0 : i;
		for (i = 0; unit[1] != B64[i] && i < 64; i++)
			;
		unit[1] = i == 64 ? 0 : i;
		for (i = 0; unit[2] != B64[i] && i < 64; i++)
			;
		unit[2] = i == 64 ? 0 : i;
		for (i = 0; unit[3] != B64[i] && i < 64; i++)
			;
		unit[3] = i == 64 ? 0 : i;
		*r++ = (unit[0] << 2) | (unit[1] >> 4);
		*r++ = (unit[1] << 4) | (unit[2] >> 2);
		*r++ = (unit[2] << 6) | unit[3];
	}
	*r = 0;

	return _ret;
}

