using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Collections;

namespace projecteuler
{
	class Problem35 
	{	
		public static List<int> primeList;
	
		public static void Main(string[] args) 
		{
			new Problem35().getCircularPrimes(1000000);
		}

		public void getCircularPrimes(int uperLimit)
		{
			Stopwatch watch = new Stopwatch();
			watch.Start();
	
			primeList = new List<int>();	
			primeList.Add(2);
			primeList.Add(3);
			primeList.Add(5);
			primeList.Add(7);
			
			List<int> circularPrimesList = new List<int>();
			/*circularPrimesList.Add(2);
			circularPrimesList.Add(3);
			circularPrimesList.Add(5);
			circularPrimesList.Add(7);*/
			
			for (int x = 11; x < uperLimit; x=x+2)
			{
				string stX = x.ToString();
				if (stX.Contains("0") || stX.Contains("2") || stX.Contains("4") || stX.Contains("5") || stX.Contains("6") || stX.Contains("8"))
					continue;
				if (isPrime(x))	
				{
					primeList.Add(x);
				}
			}

			//Console.WriteLine("***********************************************************");
			//Console.WriteLine("There is a total of {0} primes: " + listToString(primeList),primeList.Count);
			foreach(int prime in primeList)
			{
				List<int> rotations = getRotations(prime);
				foreach(int rotation in rotations)
				{
					if (primeList.Any(item => item == rotation))
					{
						circularPrimesList.Add(rotation);
					}
					else
					{
						//Not prime
						//Console.WriteLine("Not prime: {0}",rotation);
						circularPrimesList = circularPrimesList.Except(rotations).ToList();
						break;
					}
				}
			}
	
			watch.Stop();
			circularPrimesList = circularPrimesList.Distinct().ToList();
			Console.WriteLine("There is a total of {0} circular primes: " + listToString(circularPrimesList),circularPrimesList.Count);
			Console.WriteLine("Execution time: " + watch.Elapsed.TotalMilliseconds + " ms.");
		}

		public string listToString(List<int> list)
		{
			string result = "";
			foreach (int item in list)
			{
				result += item + ",";
			}
			return result;
		}

		public string setToString(SortedSet<int> list)
		{
			string result = "";
			foreach (int item in list)
			{
				result += item + ",";
			}
			return result;
		}
	
		public List<int> getRotations(int n)
		{
			List<int> rotations = new List<int>();
			int digitNumber = n.ToString().Length;;

			rotations.Add(n);
			
			for (int x = 1; x < digitNumber;x++)
			{	
				//Console.WriteLine("		Current rotation: {0}rd",x);
				int pow1 = (int)Math.Pow(10, x);
				int pow2 = (int)Math.Pow(10, digitNumber -x);
				int current0 = n/pow1;
				int current1 = (n%pow1)*pow2;
				//Console.WriteLine("			Values: {0} and {1}",current0,current1);
				rotations.Add(current0+current1);
			}
			return rotations.Distinct().ToList();
		}
	
		public bool isPrime(int n)
		{
			if (n < 2)
			{	
				return false;
			}
			if (primeList.Any(item => item == n))
			{	
				return true;
			}

			int limit = (int)Math.Sqrt(n)+1;
			int last = 1;
			foreach (int prime in primeList)
   			{
				if (prime > limit)
					break;
				if (n % prime == 0)
				{
					return false;
				}
				last = prime;
    		}
	
			for (int x = last; x < limit; x = x+2)
			{
				if (n % x == 0)
				{	
					return false;
				}
			}
			
			return true;
		}

	}
}
