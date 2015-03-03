#!/usr/bin/python3 -tt
  
def decode(p, q, e, y):
  s2 = 0
  s1 = 1
  r = (p-1)*(q-1)
  a = r
  while r != 0:
    quot = e // r
    e, r = r , e - quot * r
    s1 , s2 = s2 , s1 - quot * s2
  d = s1 % a
  N = p * q 
  x = pow(y,d,N)
  return x

def int2str(x):
  # Given an integer x, returns its corresponding string
  chars = []
  while x != 0:
    chars.append(chr(x % 128))
    x = x // 128
  return ''.join(chars)

 
def str2int(s):
  # Given a string s, returns its corresponding integer 
  x, p = 0, 1
  for char in string:
    x = x + power * ord(c)
    p = p * 128
  return x


def main():    
  test_num = int(input())
  for unused_i in range(test_num):
    p, q, e = list(map(int, input().split()))
    y = int(input())
    print(int2str(decode(p, q, e, y)))


if __name__ == '__main__':
  main()
