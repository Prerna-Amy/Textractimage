#!/usr/bin/env python
# coding: utf-8

# In[20]:


import boto3


# In[21]:


boto3.__version__


# In[22]:


client = boto3.client('textract', region_name='us-east-2')


# In[28]:


response = client.detect_document_text(Document={
        'S3Object': {
      'Bucket': 'prernavermabucket',
      'Name': 'test.jpg'
    
    

    }
        

        

})


# In[29]:


response


# In[32]:


img_path= "C:/Users/DELL/Desktop/myimage/test.jpg"


with open(img_path,"rb") as raw_image:
    _temp_image = raw_image.read()
    bytes_image = bytearray(_temp_image)
    
response = client.detect_document_text(Document = {'Bytes' : bytes_image})


# In[33]:


response


# In[35]:


response["DetectDocumentTextModelVersion"]


# In[43]:


blocks=response["Blocks"]
type(blocks)


# In[44]:


from collections import Counter



    


# In[45]:


block_counts = Counter(x["BlockType"] for x in blocks)
block_counts


# In[46]:


blocks[1]


# In[48]:


all_lines = [l for l in blocks if l["BlockType"] == "LINE"]
len(all_lines)


# In[50]:


for l in all_lines:
    print(l["Text"])


# In[61]:


all_lines


# In[62]:


import json
with open('C:/Users/DELL/Desktop/l.json', 'w') as f:
    json.dump(l, f)


# In[58]:


import csv
csvfile=open('C:/Users/DELL/Desktop/lll.csv','w', newline='')
obj=csv.writer(csvfile)
for l in all_lines:
    obj.writerow(l)
csvfile.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




