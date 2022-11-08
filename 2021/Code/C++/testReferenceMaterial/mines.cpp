bool addMine(matrix& map)
{
	//Generate a random location for this mine
	int x = rand() % x_dim, y = rand() % y_dim;

	//Add the mine, if one isn't already there
	if(map[x][y] != '*')
	{
		map[x][y] = '*';
		//walk through all neighboring locations and increment their proximity counts
		for(int dx = x-1; dx <= x+1; dx++)
			for(int dy = y-1; dy <= y+1; dy++)
				if(dx >= 0 && dx < x_dim && dy >= 0 && dy < y_dim)
					if(map[dx][dy] != '*') //Don't update proximity count for mine locations
						if(map[dx][dy] == '.')
							map[dx][dy] = '1'; //initial proximity, set to 1
						else
							map[dx][dy]++; //otherwise, increment current count (works even with chars so long as count never exceeds 9)
		return true;
	}

	//random location already contains a mine
	return false;
}