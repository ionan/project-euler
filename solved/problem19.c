#include <stdio.h>

int monthDays[11];

void fillMonthDays()
{
	monthDays[0] = 31;  //January
	monthDays[1] = 28;  //February
	monthDays[2] = 31;  //March
	monthDays[3] = 30;  //April
	monthDays[4] = 31;  //May
	monthDays[5] = 30;  //June
	monthDays[6] = 31;  //July
	monthDays[7] = 31;  //August
	monthDays[8] = 30;  //September
	monthDays[9] = 31;  //October
	monthDays[10] = 30;  //November
	monthDays[11] = 31;  //December
}

int getNumberDays(int year, int month)
{
	if (month != 2)
	{
		//Not February
		return monthDays[month-1];
	}
	else
	{
		//February
		//Check wether is a leap year or not
		if ((year % 100 == 0) && (year % 400 == 0))
		{
			//It's a century and it is divisible by 400
			printf("$$$$ Leap year(%d)! $$$$\n",year);
			return 29;
		}
		else if ((year % 100 != 0) && (year % 4 == 0))
		{
			//Leap year
			printf("$$$$ Leap year(%d)! $$$$\n",year);
			return 29;
		}
		else
		{
			//Not a leap year
			return monthDays[month-1];
		}
	}
}

void main()
{
	printf("Working....\n");
	fillMonthDays();
	int year = 1901;
	int month = 1;
	long days = 365;
	int numberOfSundays = 0;
	while (year < 2001)
	{
		while (month < 13)
		{
			//printf("Days: %ld\n",days);
			//printf("Month: %d\n",month);
			if ((days+1) % 7 == 0)
			{
				//First day of next month fell on sunday
				numberOfSundays++;
				printf("**** Found a sunday (%d-%d-%d)! ****\n",1,month,year);
			}
			int numberOfDays = getNumberDays(year,month);
			//printf("Dys in the month: %d\n",numberOfDays);
			days = days + numberOfDays;
			printf("***** Number of days 'til now: %ld *****\n",days);
			month++;
		}
		year++;
		month = 1;
	}
	printf("Number of sundays: %d\n",numberOfSundays);

}
