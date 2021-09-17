punctuations = "!@$^&()-;#:?/|\.,<>"
my_str = 'Well, here is where it all starts!@#'
nopunct = ''
for char in my_str:
    if char not in punctuations:
        nopunct = nopunct + char
print(nopunct)
