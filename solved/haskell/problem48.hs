problem48 :: (Integral b) => b -> b -> b
problem48 l d = let dg = 10^d
                in (`mod` dg) $ sum [(x^x) `mod` dg | x <- [1..l]]

main = print $ problem48 1000 10               