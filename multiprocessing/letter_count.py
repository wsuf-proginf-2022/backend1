import json
from urllib import request
import time
from threading import Thread

def count_letters(ur, frequency):
  response = request.urlopen(ur)
  txt = str(response.read())
  for letter in txt:
    letter = letter.lower()
    if letter in frequency:
      frequency[letter] += 1


def main():
  frequency = {}
  for c in "abcdefghijklmnopqrstuvwxyz":
    frequency[c] = 0
  start = time.time()
  threads = []
  for i in range(1000,1020):
    t = Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency))
    t.start()
    threads.append(t)

  for thread in threads:
    thread.join()
  print(json.dumps(frequency, indent=4))
  end = time.time()
  print(f"Time taken: {end - start}")

if __name__ == "__main__":
  main()
