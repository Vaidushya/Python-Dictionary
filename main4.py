def mirrChar(input,k):

    original = 'abcdefghijklmnopqrstuvwxyz'
    reversed = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reversed))

    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    for i in range(0, len(suffix)):
        if suffix[i] in dictChars:
            mirror += dictChars[suffix[i]]

    print(prefix + mirror)

    if __name__ == "__main__":
        input = 'Letter'
        k = 3
        mirrChar(input, k)