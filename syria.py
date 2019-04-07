import wikipedia
#

# ------ January-April 2011 ------
syriatimeline = wikipedia.page("Timeline of the Syrian Civil War (January–April 2011)")

pagecontent = syriatimeline.content.split('\n')
newlist = []
for item in pagecontent:
    each = item.split()
    newlist.append(each)

numlist = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
eachline = []
for thing in newlist:
    if len(thing) > 0:
        if thing[0] in numlist:
            eachline.append(thing)

# print(eachline)

eachlinestr = []
for thing in eachline:
    eachlinestr.append(" ".join(thing))

for line in eachlinestr:
    print(line,'\n')

#
#
# ## ------ May–August 2011 ------
# syriatimeline = wikipedia.page("Timeline of the Syrian Civil War (May–August 2011)")
#
# pagecontent = syriatimeline.content.split('\n=== ')
# newlist = []
#
# for item in pagecontent:
#     # print(item)
#     each = item.split()
#     newlist.append(each)
# # print(newlist)
#
# numlist = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
# eachline = []
# for thing in newlist:
#     if len(thing) > 0:
#         if thing[0] in numlist:
#             eachline.append(thing)
#
# # print(eachline)
#
# eachlinestr = []
# for thing in eachline:
#     eachlinestr.append(" ".join(thing))
#
# for line in eachlinestr:
#     print(line,'\n')
