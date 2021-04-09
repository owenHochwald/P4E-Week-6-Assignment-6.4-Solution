# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

# Starting Code
text = "X-DSPAM-Confidence:    0.8475"
# -------------------

string = str('X-DSPAM-Confidence:    0.8475')
start = string.find('0')
end = string.find('5')
num = string[23:28+1]
sliced_var = slice(23, 29)
diced = float(string[sliced_var])
print(diced)
