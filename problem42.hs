import Data.Char
import Data.List
import qualified Data.Text as T
import System.IO     

triangleNumber :: Int -> Int
triangleNumber n = quot (n * (n + 1)) 2

toInt :: Char -> Int
toInt '"' = 0
toInt c = let offset = 64
          in (ord c) - offset

isTriangleWord :: String -> Bool
isTriangleWord w = let val = sum $ map toInt w
                   in elem val (takeWhile (< val) $ map triangleNumber [1..])

totalTriangleWords :: [String] -> Int
totalTriangleWords [] = 0
totalTriangleWords [x:xs] = let c = if isTriangleWord x then 1 else 0
                            in c + totalTriangleWords xs

problem42 :: FilePath -> Int
problem42 fileName = withFile fileName ReadMode (\handle -> do  
                        xs <- hGetContents handle
                        print $ totalTriangleWords $ T.splitOn (T.pack ",") (T.pack xs))  

main = problem42 "../files/p042_words.txt"