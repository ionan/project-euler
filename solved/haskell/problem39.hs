-- "BRUTE FORCE" SOLUTION

rightTriangle :: Int -> Int -> Int -> Bool
rightTriangle a b c = a^2 + b^2 == c^2

triangles :: Int -> [(Int,Int,Int)]
triangles p = let oneThird = quot p 3 
              in [(a,b,(p - a - b)) | a <- [1..oneThird], b <- [a..2 * oneThird], b < (p - a - b), rightTriangle a b (p - a - b)]

problem39' :: Int -> [(Int, Int, Int)]
problem39' maxP = foldl (\arr maxArr -> if length arr > length maxArr then arr else maxArr) [] [triangles p | p <- [2,4..maxP]]

-- FASTER SOLUTION

non2divisor :: Int -> Int
non2divisor x 
    | m /= 0 	= x 
    | otherwise = non2divisor d 
    where m = x `mod` 2 
          d = x `div` 2

findTriplet :: Int -> Int -> Int -> [(Int,Int,Int, Int)]
findTriplet m s2 s = let sm = non2divisor (s2 `div` m)
                         k  = if m `mod` 2 == 1 then m + 2 else m + 1
                     in [ (a,b,c,s) | k' <- [k, k+2..min (2 * m - 1) sm], sm `mod` k' == 0, 
                          gcd k' m == 1, let d = (s2 `div` (k' * m)), let n = k' - m, 
                          let a' = d * ( m * m - n * n), let b' = 2 * d * m * n, 
                          let c = d * (m * m + n * n), let a = min a' b', 
                          let b = max a' b', rightTriangle a b c,
                          a + b + c == s]

parametrisation :: Int -> [[(Int,Int,Int,Int)]]
parametrisation s = let s2 = s `div` 2 
                        mlimit = (ceiling $ sqrt $ fromIntegral s2) - 1 
                     in [triplets | m <- [2..mlimit], s2 `mod` 2 == 0, 
                          let triplets = findTriplet m s2 s, triplets /= []]


problem39 :: Int -> [(Int, Int, Int,  Int)]
problem39 maxP = foldl (\arr maxArr -> if length arr > length maxArr then arr else maxArr) [] [concat $ parametrisation p | p <- [2,4..maxP]]

main = let sol         = problem39 1000
           (a,b,c,p)   = sol !! 0
           ln          = length sol
       in print $ show p ++ " (" ++ show ln ++ " solutions)"