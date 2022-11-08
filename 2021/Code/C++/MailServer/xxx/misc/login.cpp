#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

class loginManager
{
    public:
        loginManager()
        {
                accessGranted = 0; //access granted is a bool equal to false
        }
        void login()
        {
            cout << "Enter Username then Password.\nUsername: "; //prints the statement
            cin >> userNameAttempt; //takes in user input and assigns it to userNameAttempt
            cout << "Password: "; //prints the statement
            cin >> passWordAttempt;//takes in user input and assigns it to passWordAttempt

            //userName = checkFile("username.txt"); //call to getfile using the file
            //passWord = checkFile("password.txt"); //call to getfile using the file

            if(checkFile(userNameAttempt, "username.txt"))
            {
                if(checkFile(passWordAttempt,"password.txt")) //tests to see if username is equal to username attempt
                    {
                        cout << "Login Successful"; //if it is equal print the statement
                        cin.get(); //pauses the program here so it does not just quit on its own
                    }
                else
                    {
                        cout << "Login Unsuccessful \n"; //if it is not equal print the statment
                        login(); //recursivelly give user a chance to log in by calling the function again
                    }
            }
            
        }
        bool checkFile(string attempt, const char* p_fileName)
        {
            string line;
            fstream file;

            long long encryptChar;

            file.open(p_fileName, ios::in);

            while(1)
            {
                file >> encryptChar;
                if(encryptChar == 0)
                {
                    if(attempt == line)
                    {
                        file.close();
                        return true;
                    }
                        else
                        {
                            line.erase(line.begin(),line.end());        
                        }
            else
            {
                line += (char)decrypt(encryptChar);//
            }
              
            if(file.peek() == EOF) //check to see if we are at the end of the file
            {
                file.close();
                    return false;
            }
        }
            // if(file.is_open())
            // {
            //     getline(file, line);
            // }
            // file.close();
            //return line;
        }

        long long encrypt(int p_letter)
        {

            return powf(p_letter, 5);
        }

        int decrypt(long long p_letter)
        {
            return powf(p_letter, 1/4.f);
        }

        void saveFile(string p_line, const char* p_fileName, const int& id)
        {
            fstream file; //create stream with file
            //file.open(p_fileName, ios::out); //open file and overwrite it using ios::out
            file.open(p_fileName, ios::app); //open file and add to it using ios::app (append)
            file.seekg(0, ios:end);

            if(file.tellg() != 0)
                file << "\n";

            for(int i = 0;i < p_line.length(); i++) //go through every lett encrypt it
            {
                file << encrypt(p_line[i]); //call the encrypt function passing in the string starting at indecy i
                file << "\n"; //adds a new line
                
            }
            file << "#ID:" << id; //add a 0 to the end of the word to indicate it is done
            file.close(); //close the file
        }

    private:
        // string passWord = "darius";
        // string userName = "dks1018@yahoo.com";

        // //creating variables for input username and password
        // string passWord;
        // string userName;

        //creating variables for the user typed attempts
        string userNameAttempt;
        string passWordAttempt;
        bool accessGranted;
};

int main()
{
    loginManager app;
    //cout << app checkFile("password.txt") << endl;
    //app.saveFile("GrapeJuice", "password.txt");
    // app.saveFile("darius","username.txt");
    // app.saveFile("password","password.txt");
    app.login();

    cin.get(); //slows program
}