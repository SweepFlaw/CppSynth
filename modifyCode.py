#!/usr/bin/env python
# coding: utf-8

# In[115]:


from makeVscm import genVscm


# In[116]:


# input: targetFilename(string)
# output: entireFile String line by line (list(string))
def readTargetFile(targetFilename):
    with open(targetFilename, 'r') as file:
        codeStr = file.readlines()
    return codeStr


# In[117]:


import csv

# input: vscmFilename(string)
# output: list(dictionary)
# -- dictionary layout
#    - targetLine (int)
#    - targetColumn (int)
#    - targetOffset (int)
#    - targetLength (int)
#    - targetStr (string)
#    - candidateLine (int)
#    - candidateColumn (int)
#    - candidateOffset (int)
#    - candidateLength (int)
#    - candidateStr (string)

def readVscm(vscmFilename, csvSeparator=','):
    vscm = []
    with open(vscmFilename, 'r') as csvfile:
        vscmReader = csv.reader(csvfile, delimiter=csvSeparator)
        for row in vscmReader:
            r = {}
            r['targetLine'] = int(row[0])
            r['targetColumn'] = int(row[1])
            r['targetOffset'] = int(row[2])
            r['targetLength'] = int(row[3])
            r['targetStr'] = row[4]
            r['candidateLine'] = int(row[5])
            r['candidateColumn'] = int(row[6])
            r['candidateOffset'] = int(row[7])
            r['candidateLength'] = int(row[8])
            r['candidateStr'] = row[9]
            vscm.append(r)
    return vscm


# In[118]:


# input: 
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndex (int)
# output: multiple return values.
#   - modified codeline String (string),
#   - modified codeline Index, start from 0 (int),
#   - returnStatus(int)
def modCode(code, vscm, vscmIndex):
    if len(vscm) < vscmIndex:
        return (code, -1, -1)
    modSpec = vscm[vscmIndex]
    lineNo = modSpec['targetLine'] - 1
    colNo = modSpec['targetColumn'] - 1
    mc = code[lineNo]
    front = mc[:colNo]
    end = mc[colNo + modSpec['targetLength']:]
    mc = "".join([front, modSpec['candidateStr'], end])
    return (mc, lineNo, 0)
    


# In[119]:


# function modCodeFull (make this for main functionality)
# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndex (int)
# output: multiple return values.
#   - modified whole source String (string)
#   - modified codeline Index, start from 0 (int)
#   - returnStatus(int)
def modCodeFull(code, vscm, vscmIndex):
    mc, mci, rs = modCode(code, vscm, vscmIndex)
    if mci > 0:
        codeFront = "".join(code[:(mci - 1)])
    else:
        codeFront = ""
    if mci + 1 < len(code):
        codeEnd = "".join(code[(mci + 1):])
    else:
        codeEnd = ""
    return ("".join([codeFront, mc, codeEnd]), mci, 0)


# ## MAIN

# In[136]:


# run main function (code for command-line interface)
import sys

# argv[1]: targetCppSourcePath (string)
# argv[2]: vscmOutputFilePath (string)
# argv[3]: vscmIndexNum (int)
# standard output:
#   If the modifying process done well,
#     this prints out modifiedCode whole string.
#   If not, prints nothing.
def mainFunc (tcsp, vofp, vscmIndexNum):
    genVscm(tcsp, vofp)
    code = readTargetFile(tcsp)
    vscm = readVscm(vofp)
    mcode, mci, rs = modCodeFull(code, vscm, vscmIndexNum)
    if rs == 0:
        print(mcode)

if __name__ == '__main__':
    if(len(sys.argv) > 3):
        mainFunc(sys.argv[1], sys.argv[2], int(sys.argv[3]))


# ## TEST

# In[137]:


# TEST FLAG
TEST_FLAG = False


# In[138]:


# run main function (code for jupyter interface)
import os

if TEST_FLAG:
    # readTargetFile test
    tc_fn = '/home/ubuntu/workspace/VarSubsCandListGenCpp/test/tc.cpp'
    #print(readTargetFile(tc_fn))
    
    # readVscm test
    vscm_fn = '/home/ubuntu/workspace/VarSubsCandListGenCpp/test/log6.txt'
    #vscm_test = readVscm(vscm_fn)
    #print(vscm_test)
    
    # modCode test
    #code_test = readTargetFile(tc_fn)
    #vscm_test = readVscm(vscm_fn)
    #print("MODIFICATION:")
    #vscm_index_test = 3
    #print(vscm_test[vscm_index_test])
    #modedstr_test, modedLine_test, returnStatus_test = modCode(code_test, vscm_test, vscm_index_test)
    #print("BEFORE:")
    #print(code_test[modedLine_test])
    #print("AFTER:")
    #print(modedstr_test)
    
    # mainFunc test
    print(mainFunc(tc_fn, vscm_fn, 1))


# In[74]:


# test multiple return value.
def aaa():
    return 1, 2, 3

a, b, c = aaa()
print(a)


# In[75]:





# In[ ]:




