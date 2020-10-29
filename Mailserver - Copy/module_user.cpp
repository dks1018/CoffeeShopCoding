#include "module_user.h"
#include "module_mail.h"

// find if user exists
int user_exist_check() {
	FILE* fp;
	char file[80] = "";
	char data[60];

	strncpy(file, data_dir);
	strncat(file, userinfo);

	fp = fopen(file, "r");
	while (fgets(data, sizeof(data), fp) != NULL) {
		if (strncmp(from_user, data, strnlen(from_user)) == 0)
			return 1;
	}
	return 0;
}

void auth(int snd) {
	char auth_name[50], auth_password[50];
	char *name, *pass;
	int len;

	send_data(snd, reply[25]);
	sleep(3);
	len = recv(snd, auth_name, sizeof(auth_name), 0);
	if (len > 0) {
		cout << "Request stream: " << auth_name << endl;
		name = base64_decode(auth_name);
		cout << "Decoded username: " << name << endl;
		send_data(snd, reply[26]);
		sleep(3);
		len = recv(snd, auth_password, sizeof(auth_password), 0);
		if (len > 0) {
			cout << "Request stream: " << auth_password << endl;
			pass = base64_decode(auth_password);
			cout << "Decoded password: " << pass << endl;
			if (check_name_pass(name, pass)) {
				mail_stat = 13;
				send_data(snd, reply[27]);
			} else {
				send_data(snd, reply[16]);
			}
		} else {
			send_data(snd, reply[16]);
		}
	} else {
		send_data(snd, reply[16]);
	}
}

// check adn compare the pass and user file
int check_name_pass(char* name, char* pass) {
	FILE* fp;
	char file[80], data[60];

	strncpy(file, data_dir);
	strncat(file, userinfo);
	fp = fopen(file, "r");
	while (fgets(data, sizeof(data), fp) != NULL) {
		if (strncmp(data, name, strnlen(name)) == 0) {
			char *p;
			p = strchr(data, ' ');
			if (strncmp(p + 1, pass, strnlen(pass)) == 0) {
				fclose(fp);
				strncpy(file, data_dir);
				strncat(file, userstat);
				fp = fopen(file, "w+");
				strncat(name, " on");
				fwrite(name, 1, strnlen(name), fp);
				fclose(fp);
				return 1;
			} else {
				return 0;
			}
		}
	}
	return 0;
}

void user_quit() {
	FILE* fp;
	char file[80], data[60];
	int flag = 0, len;

	strncpy(file, data_dir);
	strncat(file, userstat);
	fp = fopen(file, "w+");
	while (fgets(data, sizeof(data), fp) != NULL) {
		if (strncmp(data, from_user, strnlen(from_user)) == 0) {
			flag = 1;
		}
		if (flag) {
			len = strnlen(data);
			if (fgets(data, sizeof(data), fp) != NULL) {
				len = -len;
				fseek(fp, len, SEEK_CUR);
				fputs(data, fp);
				len = strnlen(data);
				fseek(fp, len, SEEK_CUR);
			}
		}
	}
	fclose(fp);
}
