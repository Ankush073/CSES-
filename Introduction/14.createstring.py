from itertools import permutations
def Solve(s):
      S_sorted=sorted(s)
      unique_strings=set()
      for perm in permutations(S_sorted):
            unique_strings.add(''.join(perm))
      return unique_strings
def main():
      string=input()
      unique_strings=Solve(string)
      print(len(unique_strings))
      for str in unique_strings:
            print(str)
if __name__ == "__main__":
      main()