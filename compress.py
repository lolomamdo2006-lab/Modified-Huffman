import heapq
class node:
    def __init__(self,probability,symbol,left,right):
        self.probability=probability
        self.symbol=symbol
        self.left=left
        self.right=right
    def __lt__(self, other):
        return self.probability < other.probability

#===================
def calc_freq(data):
    freq={}
    for i in data:
        freq[i] = freq.get(i, 0) + 1
    s=len(data)
    for i in freq:
        
        freq[i]/=s
        #(freq[i]," ",i)
    return freq
#==================
def org_code(prob):
    original_code={}
    max_bits= (len(prob)-1).bit_length()
    j=0
    letters=list(prob.keys())
    letters.sort()
    for i in letters:
        original_code[i]=format(j, f"0{max_bits}b")
        j+=1
    return original_code
#====================
def generate_code(node,code,bits):
    if node is None:
        return
    elif(len(node.symbol)==1 or node.symbol=="others"):
       code[node.symbol]=bits
       return
    generate_code(node.left,code,bits+'0')
    generate_code(node.right,code,bits+'1')
    

#======================
def compress(data):
    h=[]
    code={}
    prob=calc_freq(data)
    others=node(0,"others",None,None)
    h.append(others)
    original_code=org_code(prob)
    #================Create nodes
    for i in prob.keys():
        if(prob[i]>0.05):
            n=node(prob[i],i,None,None)
            h.append(n)
        else:
            others.probability+=prob[i]
    heapq.heapify(h)
    #=======================sum the smallest node
    while(len(h)!=1):
        min1= heapq.heappop(h)
        min2= heapq.heappop(h)
        n=node(min1.probability+min2.probability,"",min2,min1)
        heapq.heappush(h,n)
    root=heapq.heappop(h)
    generate_code(root,code,"")
    #=====================print codes
    print("Symbol Code")
    for s,c in code.items():
        print(s," ",c)

    #===================the final step make compressed data using generating codes
    compressed_data=""
    for i in data:
        s=code.get(i,"others")
        if(s=="others"):
            compressed_data+=code["others"]+original_code[i]
        else:
            compressed_data+=s

    return compressed_data,code,original_code
#-------------------
