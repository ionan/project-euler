-- 20 => [2,4,5]
getDivisors :: Int -> [Int]
getDivisors x = let up = ceiling $ sqrt $ fromIntegral x
                in 1 : x : concat [if y /= cp then [y, cp] else [y] | y <- [2..up], x `mod` y == 0, let cp = x `div` y]

isInt :: RealFrac a => a -> Bool
isInt x = x == fromInteger (round x)

isPrime :: Int -> Bool
isPrime x = x `mod` 2 /= 0 && (length (getDivisors x)) == 2

primes :: [Int]
primes = [x | x <- [2..], isPrime x]

primesBelow :: Int -> [Int]
primesBelow n = takeWhile (< n) primes

toDouble :: Int -> Double
toDouble x = fromIntegral x :: Double

getCandidate :: Int -> Int -> Double
getCandidate x y = let t    = (x - y) `div` 2
                       dblT = toDouble t
                 in sqrt dblT

satisfiesConjecture :: Int -> Bool
satisfiesConjecture x
                | isP = True
                | otherwise = let pb = primesBelow x
                              in not $ null $ dropWhile (\y -> not $ isInt $ getCandidate x y) pb
                where isP = isPrime x

problem46 :: Int
problem46 = head $ dropWhile satisfiesConjecture [3,5..]

main = print $ problem46