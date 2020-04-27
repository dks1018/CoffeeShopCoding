//used online references to generate logic
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <random>
#include <ctime>

using namespace std;

//set the 2d vector to store the game board
typedef vector<vector<char>> matrix;

//set size of minesweeper board
//printf("Enter the size of the board, X value then Y value:");
// int x = scanf("%d",&i);
// int y = scanf("%d",&i);
// int M = scanf("%d",&i);

//change values to change the size of the board numMines should be equal to x or y to make the game fair
const int xBoardSize = 16, yBoardSize = 16, numMines = 16;

//Tried to set user input as global variables, could not figure out how so went back to hard coded board
//const int xBoardSize = x, yBoardSize = y, numMines = M;

//uses matric to create 2D array
//creates mines for the board
bool createMines(matrix &board)
{
	//using random function to place mines somewhere on the board
	int x = rand() % xBoardSize, y = rand() % yBoardSize;
	//performs checks to see if mines already exist
	if (board[x][y] != '*')
	{
		board[x][y] = '*';

		for (int x_location = x - 1; x_location <= x + 1; x_location++)

			for (int y_location = y - 1; y_location <= y + 1; y_location++)

				if (x_location >= 0 && x_location < xBoardSize && y_location >= 0 && y_location < yBoardSize)

					if (board[x_location][y_location] != '*')

						if (board[x_location][y_location] == '.')

							board[x_location][y_location] = '1';

						else

							board[x_location][y_location]++;
		return true;
	}

	//random function generates same spot on the grid so it already has a mine
	return false;
}

//shows the location of the markers and mine if hit
bool revealLocation(matrix &board, matrix &markers, int x, int y)
{
	//reveals location
	markers[x][y] = '.';

	//ends the game because a mine has been hit
	if (board[x][y] == '*')
		return true;

	//if there is a dot there is not a mine close by
	if (board[x][y] == '.')
	{

		queue<pair<int, int>> openLocations;
		openLocations.push(make_pair(x, y));

		while (!openLocations.empty())
		{

			pair<int, int> next = openLocations.front();

			for (int x_location = next.first - 1; x_location <= next.first + 1; x_location++)
			{
				for (int y_location = next.second - 1; y_location <= next.second + 1; y_location++)
				{

					if (x_location >= 0 && x_location < xBoardSize && y_location >= 0 && y_location < yBoardSize)
					{

						if (board[x_location][y_location] == '.' && markers[x_location][y_location] == '#')
							openLocations.push(make_pair(x_location, y_location));

						markers[x_location][y_location] = '.';
					}
				}
			}
			openLocations.pop();
		}
	}

	return false;
}

//calculate whether the game is over as a win
//counts remaining marker locations
int countMask(matrix &markers)
{
	int count = 0;
	for (int x = 0; x < xBoardSize; x++)

		for (int y = 0; y < yBoardSize; y++)

			if (markers[x][y] == '#')

				count++;

	return count;
}

int main()
{
	//error in user sizing of the baord
	//printf("Enter the size of the board, X value then Y value:");
	// int x = scanf("%d",&i);
	// int y = scanf("%d",&i);
	// int M = scanf("%d",&i);
	// int x,y,M;
	// cin >> x >> y >> M;
	srand((unsigned int)time(NULL));

	matrix board;

	matrix markers;

	//Generate our board and markers
	for (int i = 0; i < xBoardSize; i++)
	{
		board.push_back(vector<char>(yBoardSize, '.'));
		markers.push_back(vector<char>(yBoardSize, '#'));
	}
	int mineCount = 0;

	//add mines
	do
	{
		if (createMines(board))
			mineCount++;
	} while (mineCount != numMines);

	int xUserInput, yUserInput;
	do
	{
		//count board size and display spacing numbers
		int numCount = 0;
		while (numCount < xBoardSize)
		{
			cout << "\t" << numCount;
			//printf(numCount);
			numCount++;
		}
		cout << endl;

		numCount = 0;
		while (numCount < xBoardSize)
		{
			cout << "\t"
				 << "_";
			numCount++;
		}
		cout << endl;

		//shows marked mines
		for (int x = 0; x < xBoardSize; x++)
		{
			//print the number then a pipe character for seperation
			cout << "\n"
				 << x << " | ";
			// for(int dash = 0; dash < xBoardSize;dash++)
			// {
			// 	cout << "--------";
			// }cout << "\n";
			//loop through all the columns for this row
			for (int y = 0; y < yBoardSize; y++)
			{
				//if location is still masked, display markers char
				//otherwise display the underlying board value
				if (markers[x][y] == '#')
					cout << "\t" << '#';
				//cout << "\t\t" << "-";
				else
					cout << board[x][y];
			}
			cout << endl;
		}

		//takes user input for x and y values
		cin >> xUserInput >> yUserInput;

		if (revealLocation(board, markers, xUserInput, yUserInput))
		{
			cout << "MINE!" << endl;
			break;
		}

		if (countMask(markers) == numMines)
		{
			cout << "No Mines Set Off!" << endl;
			break;
		}

	} while (1);

	board.clear();
	markers.clear();

	cout << endl;

	system("pause");
	return 0;
}