#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess


# In[2]:


genVscmBinaryPath = '/home/ubuntu/workspace/VarSubsCandListGenCpp/bin/vscm'


# In[3]:


vscmMainOption=0
vscmSelectCandOption=2


# In[4]:


# targetCppSourcePath(string)
# vscmOutputFilePath(string)
# output: (void). File with the name vscmOutputFilePath created.
def genVscm(targetCppSourcePath, vscmOutputFilePath):
    subprocess.call([
        genVscmBinaryPath,
        targetCppSourcePath,
        vscmOutputFilePath,
        str(vscmMainOption),
        str(vscmSelectCandOption)
    ])
    


# ## MAIN

# In[5]:


# run main function (code for command-line interface)
import sys

# argv[1]: targetCppSourcePath (string)
# argv[2]: vscmOutputFilePath (string)
if __name__ == '__main__':
    if(len(sys.argv) > 2):
        genVscm(sys.argv[1], sys.argv[2])


# ## TEST

# In[6]:


# TEST FLAG
TEST_FLAG = False


# In[7]:


# run main function (code for jupyter interface)
if TEST_FLAG:
    test_argv = [
        '',
        '/home/ubuntu/workspace/VarSubsCandListGenCpp/test/tc.cpp',
        'testResult.txt'
    ]
    genVscm(test_argv)


# In[ ]:




