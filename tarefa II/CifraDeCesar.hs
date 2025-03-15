-- CifraDeCesar.hs
-- Implementação da Cifra de César com interface simples em Haskell
-- Lucas Nunes Silveira: 20.2.8040
-- Matheus Lopes Moreira: 20.2.8002

module Main where

import Data.Char (chr, isLower, isUpper, ord)
import System.IO (hFlush, stdout)

shiftChar :: Int -> Char -> Char
shiftChar k c
  | isUpper c = let base = ord 'A' in chr $ base + (ord c - base + k) `mod` 26
  | isLower c = let base = ord 'a' in chr $ base + (ord c - base + k) `mod` 26
  | otherwise = c

encrypt :: Int -> String -> String
encrypt k = map (shiftChar k)

decrypt :: Int -> String -> String
decrypt k = encrypt (-k)

main :: IO ()
main = do
  putStrLn "\nCifra de César - Menu:"
  putStrLn "1. Criptografar"
  putStrLn "2. Descriptografar"
  putStrLn "3. Sair"
  putStr "Escolha uma opção: "
  hFlush stdout
  option <- getLine
  case option of
    "1" -> doEncrypt
    "2" -> doDecrypt
    "3" -> putStrLn "Saindo..."
    _ -> do
      putStrLn "Opção inválida. Tente novamente."
      main

doEncrypt :: IO ()
doEncrypt = do
  putStr "Digite a mensagem para criptografar: "
  hFlush stdout
  msg <- getLine
  putStr "Digite a chave (número inteiro): "
  hFlush stdout
  keyStr <- getLine
  case reads keyStr of
    [(k, "")] -> do
      let encrypted = encrypt k msg
      putStrLn $ "Mensagem criptografada: " ++ encrypted
      main
    _ -> do
      putStrLn "Chave inválida. Use um número inteiro."
      doEncrypt

doDecrypt :: IO ()
doDecrypt = do
  putStr "Digite a mensagem para descriptografar: "
  hFlush stdout
  msg <- getLine
  putStr "Digite a chave (número inteiro): "
  hFlush stdout
  keyStr <- getLine
  case reads keyStr of
    [(k, "")] -> do
      let decrypted = decrypt k msg
      putStrLn $ "Mensagem descriptografada: " ++ decrypted
      main
    _ -> do
      putStrLn "Chave inválida. Use um número inteiro."
      doDecrypt