#include <stdio.h>

long factorial(int n)
{
	if (n == 1)
	{
		return 1;
	}
	else //n > 1
	{
		return n * factorial(n-1);
	}	
}

void main()
{
	printf("Working....\n");
	long fct = factorial(100);
	long fctDgtSum = 0;
	while (fct / 10 > 1)
	{
		fctDgtSum = fctDgtSum + fct % 10;
		fct = fct / 10;
	}
	print("The result is: %ld",fctDgtSum);
}
