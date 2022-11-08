bool revealLocation(matrix& map, matrix& mask, int x, int y)
{
	//reveal the location
	mask[x][y] = '.';

	//if location is a mine, game over, just return true
	if(map[x][y] == '*')
		return true;

	//If our location isn't in proximity to a mine
	//we reveal all neighboring locations
	//dots indicate no neighboring mine
	if(map[x][y] == '.')
	{
		//openLocations holds neighboring locations that also
		//are not in proximity to a mine
		queue<pair<int, int> > openLocations;
		openLocations.push(make_pair(x, y));

		//Walk through all dot locations and reveal their neighboars
		while(!openLocations.empty())
		{
			//Get the next location from our queue
			pair<int, int> next = openLocations.front();
			
			//The two for loops iterate over a 3x3 block within our map
			//surrounding the point next.  It will check the point itself
			//as well, which is redundant, but we hardly need highly
			//optimized code here
			for(int dx = next.first-1; dx <= next.first+1; dx++)
			{
				for(int dy = next.second-1; dy <= next.second+1; dy++)
				{
					//Let's make sure the current location is within the
					//bounds of our map.  If next is an edge location, then
					//we'll be iterating over some points outside the map
					//So just ignore those points
					if(dx >= 0 && dx < x_dim && dy >= 0 && dy < y_dim)
					{
						//if this neighbor is a dot location and hasn't
						//previously been revealed, add it to our list
						if(map[dx][dy] == '.' && mask[dx][dy] == '#')
							openLocations.push(make_pair(dx, dy));

						//reveal this neighboring location
						mask[dx][dy] = '.';

					}
				}
			}
			//We're done with the current location in our queue, so we can remove it
			openLocations.pop();
		}
	}

	return false;
}