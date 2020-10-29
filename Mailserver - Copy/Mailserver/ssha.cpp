#include <openssl/sha.h>
#include <openssl/rand.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>

using namespace std;

char* path = "data/users.txt"; // location of email text file for authorization
const int salt_length = 16; // length of the salt value
int password_size = 0; // size bit of the password
const string value_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"; // lower upper number string table

// creates the value for salt with random values
char* create_salt(char* salt_val) {
	srand(time(NULL)); 
	for (int i = 0; i < salt_length; i++) {
		salt_val[i] = value_table[rand() % (value_table.size() - 1)];
	}
}
// add salt to the password
char* add_salt(char* password, char* salt_val, char* password_salted) {
	for (int i = 0; i < password_size; i++) { 
		password_salted[i] = password[i]; 
	}
	for (int i = password_size; i < password_size + salt_length; i++) { 
		password_salted[i] = salt_val[i - password_size]; 
	}
}

// creates the password hash
void create_hash(unsigned char* password_regular, unsigned char* pass_enc, int len) {
	SHA256_CTX context;
	
	SHA256_Init(&context);
	SHA256_Update(&context, password_regular, len);
	SHA256_Final(pass_enc, &context);
}

// write information to the file for auth
void write_to_file(string email, string salt_val, string password) {
	ofstream file;
	file.open(path, ios::app);
	file << email << " " << password << " " << salt_val << endl;
	file.close();
}

// encryption
void ssha(string email, string password_string) {
	password_size = password_string.size(); //set the length of the password to the created global variable
	char password[password_string.size()]; //create array to store password
	for (int i = 0; i < password_string.size(); i++) { password[i] = password_string[i]; } // create the array to store value
	char salt_val[salt_length];
	create_salt(salt_val);
	char password_salted[password_size + salt_length];
	add_salt(password, salt_val, password_salted);
	unsigned char password_regular[password_size + salt_length];
	for (int i = 0; i < password_size + salt_length; i++) { password_regular[i] = password_salted[i]; }
	unsigned char pass_enc[SHA256_DIGEST_LENGTH];
	create_hash(password_regular, pass_enc, sizeof(password_salted));
	string pass_str_2((char*) password);
	string string_salt((char*) salt_val);
	write_to_file(email, pass_str_2, string_salt);
	
}

int main() {
	string email;
	string password_string;	
	
	cout << "Please Register.\nEnter username: ";
	cin >> email;

	cout << "Enter password: ";
	cin >> password_string;

	ssha(email, password_string);
	cout << "The user is registered\n";
	return 0;
}
