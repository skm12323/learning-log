strs = ["flower","flow","flight"]
lens = [len(strs[i]) for i in range(len(strs))]
maxlens = min(lens)
ans = ""
for i in range(maxlens):
    strs_i = [strs[j][i] for j in range(len(strs))]
    if strs_i.count(strs_i[0]) == len(strs):
        ans += strs[0][i]
    else:
        break
print("\"",ans,"\"",sep="")