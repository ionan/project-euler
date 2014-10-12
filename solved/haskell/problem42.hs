import Data.Char
import Data.List
import System.IO     

triangleNumber :: Int -> Int
triangleNumber n = quot (n * (n + 1)) 2

toInt :: Char -> Int
toInt '"' = 0
toInt c = let offset = 64
          in (ord c) - offset

boolToInt :: Bool -> Int
boolToInt x = if x then 1 else 0

isTriangleWord :: String -> Bool
isTriangleWord w = let val = sum $ map toInt w
                   in elem val (takeWhile (<= val) $ map triangleNumber [1..])

countTriangleWords :: ([Char],Int) -> Char -> ([Char],Int)
countTriangleWords (s,c) x = if x == ',' then ([],c + (boolToInt $ isTriangleWord s)) else (x:s,c)

totalTriangleWords :: [Char] -> Int
totalTriangleWords xs = snd $ foldl (countTriangleWords) ([],0) xs

problem42 fileName = do 
                        text <- readFile fileName
                        print $ totalTriangleWords text

main = problem42 "../files/p042_words.txt"