using System;
using System.Diagnostics;
using System.Collections.Generic;

namespace projecteuler
{
	class Problem37 
	{	
		public const short PRIME = 0;
		public const short NOT_PRIME = 1;

		SortedSet<int> primes;
		
		public static void Main(string[] args) 
		{
			int defaultValue = 1000000;
			if (args.Length > 0)
				 defaultValue = Int32.Parse(args[0]);
			new Problem37().findTruncatablePrimes(defaultValue);
		}

		public void findTruncatablePrimes(int upperLimit)
		{
			Stopwatch watch = new Stopwatch();
			watch.Start();
		
			primes = EratosthenesSieve(upperLimit);
			//test();
			int found = 0, sum = 0;
			foreach (int prime in primes){
				if (prime > 10 && isTruncatablePrime(prime)){
					found++;
					Console.WriteLine("\t{0} is truncatable",prime);
					sum += prime;
				}
				if (found == 11){
					break;
				}
			}

			watch.Stop();
			Console.WriteLine("Sum of {0} truncatable primes found is {1}",found,sum);
			Console.WriteLine("Execution time: " + watch.Elapsed.TotalMilliseconds + " ms.");
		}

		public void test(){
			Console.WriteLine("597 after cutting off highest digit is {0}",cutHighestDigit(597));
			Console.WriteLine("2229 after cutting off highest digit is {0}",cutHighestDigit(2229));
			Console.WriteLine("3797 after cutting off highest digit is {0}",cutHighestDigit(3797));
			Console.WriteLine("17 is truncatable? {0}",isTruncatablePrime(17));
			Console.WriteLine("3797 is truncatable? {0}",isTruncatablePrime(3797));
		}

		public bool isTruncatablePrime(int num){
			int h = num,h2 = num;
			//Console.WriteLine("\tCurrent: {0}",num);
			while (h > 0 && h2 > 0){
				if (!isPrime(h))
				{
					//Console.WriteLine("\t\t{0} is not prime (1)!",h);
					return false;
				}
				if (!isPrime(h2))
				{
					//Console.WriteLine("\t\t{0} is not prime (2)!",h2);
					return false;
				}

				h /= 10;
				h2 = cutHighestDigit(h2);
			}
			return true;
		}

		public int cutHighestDigit(int n){
			string s = n.ToString();
			if (s.Length == 1){
				return 0;
			}
			else {
				return Int32.Parse(s.Substring(1));
			}
		}

		public bool isPrime(int n){
			return primes.Contains(n);
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
	}
}
