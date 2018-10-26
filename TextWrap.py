import textwrap
if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    k = wrapper.wrap(text=string)
    for i in range(len(k)-1): 
        print(k[i])
    return(k[len(k)-1])