import Data.List

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
permuteNumbers :: [Int] -> [[Int]]
permuteNumbers xs
        | null perms = []
        | otherwise = filter divisibility perms
        where perms = permute xs

isDivisible :: Int -> Int -> Bool
isDivisible x y = x `mod` y == 0 

divisibility :: [Int] -> Bool
divisibility (d1:d2:d3:d4:d5:d6:d7:d8:d9:d10:_) = and [(isDivisible (intArrayToInt [d2,d3,d4]) 2), 
                                                (isDivisible (intArrayToInt [d3,d4,d5]) 3), 
                                                (isDivisible (intArrayToInt [d4,d5,d6]) 5), 
                                                (isDivisible (intArrayToInt [d5,d6,d7]) 7), 
                                                (isDivisible (intArrayToInt [d6,d7,d8]) 11), 
                                                (isDivisible (intArrayToInt [d7,d8,d9]) 13),  
                                                (isDivisible (intArrayToInt [d8,d9,d10]) 17)]

problem43 :: [Int] -> Int
problem43 x = let f = permuteNumbers x
              in sum $ map (\x -> intArrayToInt x) f

main = print $ problem43 [0..9]