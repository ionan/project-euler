using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Collections;

namespace projecteuler
{
	class Problem35 
	{	
		public const short PRIME = 0;
		public const short NOT_PRIME = 1;

		public static void Main(string[] args) 
		{
			int defaultValue = 1000000;
			if (args.Length > 0)
				 defaultValue = Int32.Parse(args[0]);
			new Problem35().getCircularPrimes(defaultValue);
		}

		public void getCircularPrimes(int uperLimit)
		{
			Stopwatch watch = new Stopwatch();
			watch.Start();
	
			SortedSet<int> primeList = EratosthenesSieve(uperLimit);
			
			List<int> circularPrimesList = new List<int>();

      		Console.WriteLine("There is a total of {0} primes below {1} (execution took " + watch.Elapsed.TotalMilliseconds + " ms.)",primeList.Count,uperLimit);

			foreach(int prime in primeList)
			{
				if (prime < 10)
				{
					circularPrimesList.Add(prime);
				}
				else
				{
					List<int> rotations = getRotations(prime);
					string stX = prime.ToString();
					if (stX.Contains("0") || stX.Contains("2") || stX.Contains("4") || stX.Contains("5") || stX.Contains("6") || stX.Contains("8"))
					{
						circularPrimesList = circularPrimesList.Except(rotations).ToList();
					}
					else 
					{
						foreach(int rotation in rotations)
						{	
							if (primeList.Any(item => item == rotation))
							{
								circularPrimesList.Add(rotation);
							}
							else
							{
								//Not prime
								circularPrimesList = circularPrimesList.Except(rotations).ToList();
								break;
							}
						}	
					}
				}
			}
	
			watch.Stop();
			circularPrimesList = circularPrimesList.Distinct().ToList();
			Console.WriteLine("There is a total of {0} circular primes",circularPrimesList.Count);
			Console.WriteLine("Execution time: " + watch.Elapsed.TotalMilliseconds + " ms.");
		}

		public SortedSet<int> EratosthenesSieve(int limit)
		{
			int[,] numbers = new int[limit, 2];
			List<int> primeList = new List<int>();
 
      		for (int i = 1; i < limit; i++)
      		{
      			numbers[i, 0] = i;
				numbers[i, 1] = PRIME;
      		}

			numbers[1, 1] = NOT_PRIME;
 
			for (int i = 1; i < limit; i++)
			{
				if (numbers[i, 1] == PRIME)
        		{
					int current = numbers[i, 0];
					primeList.Add(current);
					for (int multiplier = 1; multiplier < limit + 1; multiplier++)
					{
						int multiple = current * multiplier;
						if (multiple < limit)
						{
							numbers[multiple, 1] = NOT_PRIME;
						}
						else
						{
							break;
						}
					}
				}
			}
			return new SortedSet<int>(primeList.ToArray());
		}
	
		public List<int> getRotations(int n)
		{
			List<int> rotations = new List<int>();
			int digitNumber = n.ToString().Length;

			rotations.Add(n);
			
			for (int x = 1; x < digitNumber;x++)
			{	
				int pow1 = (int)Math.Pow(10, x);
				int pow2 = (int)Math.Pow(10, digitNumber -x);
				int current0 = n/pow1;
				int current1 = (n%pow1)*pow2;
				int current = current0+current1;
				if (current.ToString().Length == digitNumber) 
					rotations.Add(current);
			}
			return rotations.Distinct().ToList();
		}

	}
}
