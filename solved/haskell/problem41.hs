import Data.List

-- 20 => [2,4,5]
getDivisors :: Int -> [Int]
getDivisors x = let up = ceiling $ sqrt $ fromIntegral x
                in [y | y <- [2..up], x `mod` y == 0]


-- [1,2] => [[1,2],[2,1]]
permute :: [Int] -> [[Int]]
permute xs
        | null xs = [[]]
        | otherwise = concatMap (\x -> map (x:) $ permute $ delete x xs) xs

-- [1,2] => 12
intArrayToInt :: [Int] -> Int
intArrayToInt xs = let len  = length xs
                       pows = reverse $ take len $ iterate (* 10) 1
                   in sum $ zipWith (*) xs pows

-- [1,2] => [12,21]
permuteNumbers :: [Int] -> [Int]
permuteNumbers xs
        | null perms = []
        | otherwise = map intArrayToInt perms
        where perms = permute xs

-- 13 => True
isPrime :: Int -> Bool
isPrime x 
        | x <= 1 = False
        | x `div` 2 == 0 = False
        | x `div` 5 == 0 = False
        | otherwise = (length $ getDivisors x) == 0


-- 4 isPrime => Just 4231
maxNPandigital :: Int -> (Int -> Bool) -> Maybe Int
maxNPandigital n pre
        | n == 1 = if pre 1 then Just 1 else Nothing
        | otherwise = let arr = dropWhile pre $ permuteNumbers [n,n-1..1]
                      in find pre arr

-- 123456789 => 9
digitSum :: Int -> Int
digitSum x
        | x < 10 = x
        | otherwise = digitSum $ x `mod` 10 + digitSum (x `div` 10)

problem41' :: Int -> Maybe Int
problem41' n
        | x == Nothing = problem41 (n - 1)
        | otherwise = x
        where x = maxNPandigital n isPrime

problem41 :: Int -> Maybe Int
problem41 n
        | n == 0 = Nothing
        | dsum `mod` 3 == 0 = problem41 (n - 1)
        | otherwise = problem41' n
        where dsum = digitSum $ intArrayToInt [1..n]

main 
    | result == Nothing = print "None"
    | otherwise = print result
    where result = problem41 9