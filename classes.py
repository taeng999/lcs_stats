
# coding: utf-8

# In[15]:


class Player (object): 
    def __init__(self, name, position, coach, country): 
        self.name = name
        self.position = position
        self.coach = coach
        self.country = country
    def isCoach(self): 
        return bool(self.coach)


# In[16]:


sherly = Player(name="Sherly", position="Student", coach=0, country="USA")


# In[19]:


sherly.isCoach()


# In[ ]:


class 

