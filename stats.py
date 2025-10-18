#counting total words in frankenstein file
def count_words(r):
    word_list=r.split()
    val=len(r.split())
    return val
    
#counting the each character in a file
def count_characters(con):
    wl=con.split()
    ch_count=dict([])
    for word in wl:
        w_lower=word.lower()
        for c in w_lower:
            if c in ch_count:
                ch_count[c]=ch_count[c]+1
            else:
                ch_count[c]=1
    return ch_count
    

def sort_dict(ch_dict):
    new_chlist=[]
    index=0
    for key in ch_dict:
      if key.isalpha():
          d=dict()
          d["char"]=key
          d["num"]=ch_dict[key]
          new_chlist.append(d)
      else:
          continue
    
    new_chlist.sort(key=lambda c:c["num"],reverse=True)     
    #print(new_chlist)
    return new_chlist





