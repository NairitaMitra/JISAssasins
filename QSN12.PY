#QSN 12 SUBMOTTED BY NAIRITA MITRA


s=input("Enter the sentence") 
w = s.split(" ")    
nw = [i[::-1] for i in w]
ns = " ".join(nw)
print("The reverse is",ns)
