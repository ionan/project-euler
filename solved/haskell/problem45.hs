isInt :: RealFrac a => a -> Bool
isInt x = x == fromInteger (round x)

triangleNumber :: Int -> Int
triangleNumber n = quot (n * (n + 1)) 2

pentagonalNumber :: Int -> Int
pentagonalNumber n = (n * (3*n-1)) `div` 2

isPentagonal :: (Integral a) => a -> Bool
isPentagonal x = let fx = fromIntegral x :: Double
                 in isInt ((sqrt (24 * fx + 1) + 1) / 6)

hexagonalNumber :: Int -> Int
hexagonalNumber n = n * (2*n-1)

isHexagonal :: (Integral a) => a -> Bool
isHexagonal x = let fx = fromIntegral x :: Double
                 in isInt ((sqrt (8 * fx + 1) + 1) / 4)

p45pred :: Int -> Bool
p45pred x = not (isPentagonal x) || not (isHexagonal x)

p45gen :: Int -> [Int]
p45gen n = [triangleNumber x | x <- [n..]]

p45pred' :: Int -> Bool
p45pred' x = not (isPentagonal x)

p45gen' :: Int -> [Int]
p45gen' n = [hexagonalNumber x | x <- [n..]]

problem45 :: Int -> Int
problem45 n = head $ dropWhile p45pred' (p45gen' n)

main = print $ problem45 286