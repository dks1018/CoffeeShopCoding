#include <fstream>
#include <stdlib.h>
#include <iostream>

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

                if(check_File(entered_user,"user.txt"))
                {
                    if(check_File(entered_pass,"pass.txt"))
                    {
                        cout << "Successfull Login!" << endl;
                    }
                }
                else
                    {
                        cout << "Incorrect Username or Password!" << endl;
                        login();
                    }
        }
    bool check_File(string attempt, const char* file_name)
    {
        string line;
        fstream file;

        int encrypt_text;
        file.open(file_name, ios::in);

        while(1)
        {
            file >> encrypt_text;
            if(encrypt_text == 0 )
            {
                if(attempt == line)
                {
                    file.close();
                    return true;
                }
                else
                {
                    line.erase(line.begin(), line.end());
                }
            }
            else
            {
              line += (char)decrypt(encrypt_text);  
            }
            
            if(file.peek() == EOF)
            {
                file.close();
                return false;
            }
        }
    }

    void save_File(string text, const char* file_name, const int& ID)
    {
        fstream file;
        file.open(file_name, ios::app);

        file.seekg(0,ios::end);

        if(file.tellg() != 0)
            file << "\n";

        for(int i = 0; i < text.length(); i++)
        {
            file << encrypt(text[i]);
            file << "\n";
        }
        file << "User Identifier: " << ID;
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
    bool login_success;
};

int main()
{
    Login_Func auth;
    // int ID = 1;
    // auth.save_File("katia", "pass.txt", ID = 2);
    // auth.save_File("katia","user.txt", ID = 2);

    // auth.save_File("kd", "pass.txt", ID = 3);
    // auth.save_File("kd","user.txt", ID = 3);

    // auth.save_File("darius", "pass.txt", ID);
    // auth.save_File("dks1018","user.txt", ID);
    auth.login();
    
    cin.get();
}
