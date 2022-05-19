
import time
import sys

def ft_progress(lst):
	eta = 0
	lenght = len(lst)
	elapsed = 0
	for i, elem in enumerate(lst):
		i += 1
		sys.stdout.write("ETA: {:5.2f}s [{:3}%][{: <20}] {}/{} | elapsed time {:.2f}s\r".format(eta, int((i*100)/lenght), ''.rjust(int((((i*100)/lenght * 20))/100), '=')[:-1]+">" if int((i*100)/lenght) != 100 else ''.rjust(int((((i*100)/lenght * 20))/100), '='), i, lenght, elapsed))
		sys.stdout.flush()
		pre = time.time()
		yield elem
		post = time.time()
		eta = (post - pre) * (lenght - i)
		elapsed += post - pre

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
	
print(ret)