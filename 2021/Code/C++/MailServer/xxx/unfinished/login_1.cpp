#include <fstream>
#include <stdlib.h>
#include <iostream>
#include <sstream>

using namespace std;


class Login_Func
{
    public:
    void Login_func()
    {
        login_success = 0;
    }
    void login()
        {
            cout << "Username: ";
            cin >> entered_user;

            cout << "Password: ";
            cin >> entered_pass;

                int usrID = check_File(entered_user,"user.txt");
                if(usrID != 0)
                {
                    int passID = check_File(entered_pass,"pass.txt");
                    if(usrID == passID)
                    {
                        cout << "Successfull Login!" << endl;
                    }
                    else
                    {
                        cout << "Incorrect Username or Password!" << endl;
                        login();
                    }
                    
                }
                else
                    {
                        cout << "Incorrect Username or Password!" << endl;
                        login();
                    }
        }

    int get_LastID()
    {
        fstream file;
        file.open("user.txt", ios::in);
        file.seekg(0, ios::end);

        if(file.tellg() == -1)
            return 0;

        string s;

        for(int i = -1; s.find("#") == string::npos; i--)
        {
            file.seekg(i, ios::end);
            file >> s;
        }

        file.close();
        s.erase(0,4);

        int id;
        istringstream(s) >> id;

        return id;
    }

    int check_File(string attempt, const char* file_name)
    {
        string line;
        fstream file;

        string current_Char;
        long long encrypt_text;

        file.open(file_name, ios::in);

        while(1)
        {
            file >> current_Char;
            if(current_Char.find("#id:") != string::npos)
            {
                    if(attempt == line)
                    {
                        file.close();
                        current_Char.erase(0,4);
                        int id;
                        istringstream(current_Char) >> id;
                        return id;
                    }
                    else
                    {
                        line.erase(line.begin(), line.end());
                    }
                }
            {
                istringstream(current_exception) >> encrypt_text;
                line += (char)decrypt(encrypt_text);
                current_Char = "";
            }
            
            if(file.peek() == EOF)
            {
                file.close();
                return 0;
            }
        }
    }

    void save_File(string text, const char* file_name, const int& id)
    {
        fstream file;
        file.open(file_name, ios::app);
        file.seekg(0,ios::end);

        if(file.tellg() != 0)
            file << "\n";

        file.seekg(0, ios::beg);


        for(int i = 0; i < text.length(); i++)
        {
            file << encrypt(text[i]);
            file << "\n";
        }
        file << "#ID:" << id;
        file.close();

    }

    int encrypt(int letter)
    {
        return letter + 3;
    }

    int decrypt(int letter)
    {
        return letter - 3;
    }

private:
    string entered_user;
    string entered_pass;
    string type_user;
    string type_pass;
    bool login_success;
};

int main()
{
    Login_Func auth;
    // int id = 1;
    // auth.save_File("katia", "pass.txt", id = 2);
    // auth.save_File("katia","user.txt", id = 2);

    // auth.save_File("kd", "pass.txt", id = 3);
    // auth.save_File("kd","user.txt", id = 3);

    // auth.save_File("darius", "pass.txt", id);
    // auth.save_File("dks1018","user.txt", id);

    // auth.addUser("darius","password");
    // auth.addUser("dariu","password");
    // auth.addUser("dari","password");
    // auth.addUser("dar","password");
    // auth.addUser("da","password");
    // auth.addUser("d","password");
    auth.login();
    
    //cin.get();
}
