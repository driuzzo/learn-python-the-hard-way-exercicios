print("Hello {name}, your balance is {blc:9.4f}".format(name="Adam", blc=230.2346))

# integer arguments
print("The number is: {:d}".format(123))

# float arguments
print("The float number is: {:f}".format(123.456789))

# octal, binary, and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# integer numbers with minimun width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

#show space for + sign
print("{: f} {: f}".format(12.23, -12.23))
