using System;
using System.Diagnostics;

namespace projecteuler
{
	class Problem36 
	{	
		public static void Main(string[] args) 
		{
			int defaultValue = 1000000;
			if (args.Length > 0)
				 defaultValue = Int32.Parse(args[0]);
			new Problem36().findSumOfPalindromes(defaultValue);
		}

		public void findSumOfPalindromes(int upperLimit)
		{
			Stopwatch watch = new Stopwatch();
			watch.Start();
		
			int sum = 0;
			int totalPalindromes = 0;
			for (int i = 1; i < upperLimit; i = i + 2){
				if (isPalindrome(i,10) && isPalindrome(i,2)){
					sum += i;
					totalPalindromes++;
				}
			}

			watch.Stop();
			Console.WriteLine("The sum of {0} palindromes below {1} is {2}",totalPalindromes,upperLimit,sum);
			Console.WriteLine("Execution time: " + watch.Elapsed.TotalMilliseconds + " ms.");
		}

		public void test(){
			Console.WriteLine("585 is palindrome base 10? {0}",isPalindrome(585,10));
			Console.WriteLine("585 is palindrome base 2? {0}",isPalindrome(585,2));
			Console.WriteLine("125 is palindrome base 10? {0}",isPalindrome(125,10));
			Console.WriteLine("125 is palindrome base 2? {0}",isPalindrome(125,2));
		}

		public bool isPalindrome(int number, short baseToConvert)
		{
			string num = Convert.ToString(number,baseToConvert);
			return num.Equals(ReverseString(num));
		}

		public static string ReverseString(string s)
		{
    		char[] charArray = s.ToCharArray();
    		Array.Reverse( charArray );
    		return new string(charArray);
		}
	}
}
