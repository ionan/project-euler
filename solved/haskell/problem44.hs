pentagonalNumber :: Int -> Int
pentagonalNumber n = (n * (3*n-1)) `div` 2

isInt :: RealFrac a => a -> Bool
isInt x = x == fromInteger (round x)

isPentagonal :: (Integral a) => a -> Bool
isPentagonal x = let fx = fromIntegral x :: Float
                 in isInt ((sqrt (24 * fx + 1) + 1) / 6)

constraints :: Int -> (Int,Int) -> Bool
constraints x (_,y) = isPentagonal (x + y) && isPentagonal (abs (x - y))

problem44 :: Int -> (Int,Int)
problem44 n
        | null r = problem44 (n + 1)
        | otherwise = (n, fst $ head r)
        where   p = pentagonalNumber n
                mc = constraints p
                r = filter mc $ [(y,pentagonalNumber y) | y <- [n,n-1..1]]

main = let (x,y) = problem44 2
       in putStrLn ("x = " ++ (show x) ++ ", y = " ++ (show y) ++ ", D = " ++ (show (pentagonalNumber x - pentagonalNumber y)))