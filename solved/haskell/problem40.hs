import Data.Char

takeNth :: [Char] -> Int -> Int
takeNth sol n = digitToInt $ sol !! n

problem40 :: [Int] -> Int
problem40 arr = let sol = concat [show x | x <- [0..]]
                in product $ map (takeNth sol) arr

main = print $ problem40 [1,10,100,1000,10000,100000,1000000]