#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

class Manager_Func
{
 public:

    Manager_Func()
    {
        access = 0;
    }
    void login_func()
    {
        cout << "Do you have an account? Enter Y (Yes) or N (No).";
        cin >> answer;

        if(answer == "N")
        {
            sign_up();
        }
        cout << "Enter your username and then password\nUsername:";
        cin >> user_input_entered;

        int usrID = content_check(user_input_entered, "users.txt");
        if(usrID != 0)
        {
            cout << "Password:";
            cin >> pass_input_entered;

            int pwdID = content_check(pass_input_entered, "pass.txt");
            if(usrID == pwdID)
            {
                cout << "Successful Login!\n" << endl;;
                //login_func();

            }
            else
            {
                cout << "Incorrect Username or Password" << endl;
                login_func();
            }
        }
        else
        {
            cout << "Incorrect Username or Password" << endl;
            login_func();
        }
    }

    void user_add_to_file(const string username, const string password)
    {
        if(content_check(username, "users.txt") != 0)
        {
            cout << "That username is not availble." << endl;
            return;
        }

        int UID = 1 + increment_ID();
        saveFile(username, "users.txt", UID);
        saveFile(password, "pass.txt", UID);
    }

    int increment_ID()
    {
        fstream file;
        file.open("users.txt", ios::in);
        file.seekg(0, ios::end);

        if(file.tellg() == -1)
            return 0;

        string key_search;

        for(int i = -1; key_search.find("#") == string::npos; i--)
        {
            file.seekg(i, ios::end);
            file >> key_search;
        }

        file.close();
        key_search.erase(0, 4);

        int UID;
        istringstream(key_search) >> UID;

        return UID;
    }

    int content_check(string attempt, const char* file_name)
    {
        string line;
        fstream file;

        string curr_char;
        long long encrypt_function_char;

        file.open(file_name, ios::in);
        
        while(1)
        {
            file >> curr_char;
            if(curr_char.find("#ID:") != string::npos)
            {
                if(attempt == line)
                {
                    file.close();
                    curr_char.erase(0, 4);
                    int UID;
                    istringstream(curr_char) >> UID;
                    return UID;
                }
                else
                {
                    line.erase(line.begin(), line.end());
                }
            }
            else
            {
                istringstream(curr_char) >> encrypt_function_char;
                line += (char)decrypt_func(encrypt_function_char);
                curr_char = "";
            }

            if(file.peek() == EOF)
            {
                file.close();
                return 0;
            }
        }
    }

    void saveFile(string line_file, const char* file_name, const int& UID)
    {
        fstream file;
        file.open(file_name, ios::app);
        file.seekg(0, ios::end);

        if(file.tellg() != 0)
            file << "\n";

        file.seekg(0, ios::beg);

        for(int i = 0; i < line_file.length(); i++)
        {
            file << encrypt_func(line_file[i]);
            file << "\n";
        }

        file << "#ID:" << UID;
        file.close();
    }

    long long encrypt_func(int letter_file)
    {
        return powf(letter_file, 5) * 4 - 14;
    }
    int decrypt_func(long long letter_file)
    {
        return powf((letter_file + 14) / 4, 1/5.f);
    }
////
void sign_up()
{
    cout << "Enter the account details. Remember your email it will be used as your username to log in!\nEmail: ";
    cin >> email;
    cout << "Password: ";
    cin >> password;
    user_add_to_file(email,password);
}

private:
    //string f_name;
    //string l_name;
    string email;
    string password;
    string answer;
    string user_input_entered;
    string pass_input_entered;
    bool access;
};

int main()
{
    Manager_Func auth;
    auth.login_func();
    cin.get();
}