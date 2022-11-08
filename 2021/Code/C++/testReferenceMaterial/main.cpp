int main()
{
	srand((unsigned int)time(NULL));

	//map contains our mines and proximity values
	//Only unmasked locations of map will be visible though
	//as tracked by our following mask matrix
	matrix map;

	//mask tracks revealed locations
	//# char indicates unrevealed locations
	//. char indicated revealed locations
	matrix mask;


	//Generate our map and mask
	for(int i = 0; i < x_dim; i++)
	{
		map.push_back(vector<char>(y_dim, '.'));
		mask.push_back(vector<char>(y_dim, '#'));
	}
	int mineCount = 0;


	//loop to add mines until we have a full minefield
	do
	{
		if(addMine(map))
			mineCount++;
	}while(mineCount != numMines);


	int x_in, y_in;
	do
	{
		//Display the masked minefield
		//output column indices first
		cout << "  0123456789" << endl;
		cout << "  ----------" << endl;

		//loop through our rows
		for(int x = 0; x < x_dim; x++)
		{
			//output each row index before the row itself
			cout << x << "|";

			//loop through all the columns for this row
			for(int y = 0; y < y_dim; y++)
			{
				//if location is still masked, display mask char
				//otherwise display the underlying map value
				if(mask[x][y] == '#')
					cout << '#';
				else
					cout << map[x][y];
			}
			cout << endl;
		}

		//Wait for user input to reveal a location
		cin >> x_in >> y_in;

		//pass the specified location to our revealLocation function
		//revealLocation returns true if a mine was unmasked
		if(revealLocation(map, mask, x_in, y_in))
		{
			cout << "You set off a mine.  Game over!" << endl;
			break;
		}

		//Count our masked location, if == numMines, then only mines are left
		//and player has won the game
		if(countMask(mask) == numMines)
		{
			cout << "You have found all the mines.  Congratulations!" << endl;
			break;
		}

	}while(1);

	map.clear();
	mask.clear();

	cout << endl;

	system("pause");
	return 0;
}