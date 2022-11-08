// MineSweeper.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
using  namespace std;

int NumberOfMinesNearby = 0;
int CorrectGuess = 0;
int TotalCorrectGuessesToWin;
string doublespace = "  ";
int LengthOfGrid = 10;
int Grid[10][10];
string SolvedGrid[15][15];
string newLine = "\n";
int Solved = 0;
bool PrintAgain = false;

void CreateMineGrid();
void addBombs(int BombCount);
void GuessAndDisplayGrid();
void PlayAgain();
void ReprintGrid(int x, int y);


int main()
{
    cout << "\n\n";
    cout << "    Welcome to MineSweeper!\n\n\n";
    cout << "    RULES:\n\n";
    cout << "        Enter Row and Column\n";
    cout << "        Try to avoid all mines (M), else the game is over!\n";
    cout << "        When choosing a row and column, the value of squares around represents the number of bombs touching the square\n";
    cout << "        Game ends when you unveal all squares without landing on a mine (M)\n\n\n";
    cout << "    GOOD LUCK AND DON'T DIE!\n\n";
    CreateMineGrid();
}

void CreateMineGrid() 
{
    // populate the  2D Grid with all 0's initially 
    for (int row = 0; row < LengthOfGrid; row++) 
    {
        for (int column = 0; column < LengthOfGrid; column++) {
            Grid[row][column] = 0;
        }
    }

    // populate the Compled SolvedGrid with empty spaces ( this is only for Styling Purposes )
    for (int row = 0; row < LengthOfGrid; row++)
    {
        for (int column = 0; column < LengthOfGrid; column++) {
            SolvedGrid[row][column] = " ";
        }
    }

    int NumberOfBombs = 10;

    // populate the grid with all the bombs 
    addBombs(NumberOfBombs);

    cout << "        Number of Mines: " << NumberOfBombs << "\n\n\n";

    GuessAndDisplayGrid();
}

void addBombs(int BombCount)
{ 
    int BombsInGrid = 0;
    int i;
    int j;

    do {
        do
        {
            i = rand() % LengthOfGrid;
            j = rand() % LengthOfGrid;
        } while (Grid[i][j] != 0);
        // Let's use the number 9 to represent a Mine for now
        Grid[i][j] = 9;
        BombsInGrid++;
    } while (BombsInGrid < BombCount);
}

void GuessAndGatherInput()
{

    int x;
    int y; 

    cout << doublespace;
    cout << "\n      It's time to guess!\n\n" << doublespace;

    cout << "      Row: ";
    cin >> x; cout << newLine;
    cout << "        Column: ";
    cin >> y; cout << newLine;

    // dont guess a row value that goes not exist on the grid
    if (x >= LengthOfGrid)
    {
        cout << "      \nRow value guessed does not exist. Please try again!";
    };

    // dont guess a column value that goes not exist on the grid
    if (y >= LengthOfGrid)
    {
        cout << "      \nColumn value guessed does not exist. Please try again!";
    };

}

void GuessAndDisplayGrid()
{
    TotalCorrectGuessesToWin = ((5 * 5) - 10);
    int x;
    int y;

    ReprintGrid(0,0);

    do {
        if (Solved == 0)
        { 
            do {

                int x;
                int y;

                cout << doublespace;
                cout << "\n      It's time to guess!\n\n" << doublespace;

                cout << "      Row: ";
                cin >> x; cout << newLine;
                cout << "        Column: ";
                cin >> y; cout << newLine;

                // dont guess a row value that goes not exist on the grid
                if (x >= LengthOfGrid)
                {
                    cout << "      \nRow value guessed does not exist. Please try again!";
                };

                // dont guess a column value that goes not exist on the grid
                if (y >= LengthOfGrid)
                {
                    cout << "      \nColumn value guessed does not exist. Please try again!";
                };

            } while (x >= LengthOfGrid || y >= LengthOfGrid);
        }

        int i = 0;

        if (i >= 0)
        {
            for (int i = 1; i <= LengthOfGrid; i++)
            {
                for (int j = 1; j <= LengthOfGrid; j++)
                {
                    NumberOfMinesNearby = 0;
                    // check each square around current square to see where nearby mines are at
                    if (Grid[x][y] == 9)continue;
                    if (Grid[x - 1][y - 1] == 9) NumberOfMinesNearby++;
                    if (Grid[x][y - 1] == 9) NumberOfMinesNearby++;
                    if (Grid[x + 1][y - 1] == 9) NumberOfMinesNearby++;
                    if (Grid[x - 1][y] == 9) NumberOfMinesNearby++;
                    if (Grid[x + 1][y] == 9) NumberOfMinesNearby++;
                    if (Grid[x - 1][y + 1] == 9) NumberOfMinesNearby++;
                    if (Grid[x][y + 1] == 9) NumberOfMinesNearby++;
                    if (Grid[x + 1][y + 1] == 9) NumberOfMinesNearby++;
                };
            }

            if (Grid[x][y] != 9)
            {
                Grid[x][y] = NumberOfMinesNearby;
                NumberOfMinesNearby = 0;
                CorrectGuess++;

                PrintAgain = true;

                ReprintGrid(x,y);
            }

            if (Grid[x][y] == 9) {
           
                Solved = 1;

                ReprintGrid(x,y);
            }

            if (CorrectGuess == TotalCorrectGuessesToWin)
            {
                system("CLS");
                cout << " You've won!!!" << doublespace;
                Solved = 1;
            }
          
        };
    } while (Solved == 0);

    if (Solved == 1)
    {
        PlayAgain();
    }
}

 void PlayAgain() {
     cout << " YOU LANDED ON A MINE!!!!";
     cout << " GAME OVER :(";
     system("CLS");

}

void ReprintGrid(int x, int y)
{
    if (PrintAgain == true)
    {
        int gridValue = Grid[x][y];
        cout << gridValue;

        if (Grid[x][y] == 9) {
            SolvedGrid[x][y] = "M";
        }else if (Grid[x][y] == 0) {
            SolvedGrid[x][y] = "0";
        }else if (Grid[x][y] == 1) {
            SolvedGrid[x][y] = "1";
        }else if (Grid[x][y] == 2) {
            SolvedGrid[x][y] = "2";
        }
        else if (Grid[x][y] == 3) {
            SolvedGrid[x][y] = "3";
        };

    cout << "       ";
    for (int i = 0; i < LengthOfGrid; i++)
    {
        cout << "    " << i << " ";
    }

    cout << "\n\n";

    for (int i = 0; i < LengthOfGrid; i++) {
        for (int j = 0; j < LengthOfGrid; j++) {
            if (j == 0)
            {
                cout << "    " << i << "  ";
            };
        }

        for (int j = 0; j < LengthOfGrid; j++)
        {
            cout << " | " << " " << SolvedGrid[i][j] << ' ';
        }
        cout << " | ";
        cout << newLine;
        cout << "         ============================================================\n";
    }
}
