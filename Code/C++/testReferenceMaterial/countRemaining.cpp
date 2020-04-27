int countMask(matrix& mask)
{
	int count = 0;
	for(int x = 0; x < x_dim; x++)
		for(int y = 0; y < y_dim; y++)
			if(mask[x][y] == '#') count++;

	return count;
}