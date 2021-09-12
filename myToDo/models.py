from django.db import models
# whenever there is a change in the model make sure we run "makemogrations" in the terminal
class ToDo(models.Model):
    text_todo = models.CharField(max_length= 500)
    added_date = models.DateTimeField(auto_now_add = True)# auto_now_add update date only when the data first time saved 
    update_date = models.DateTimeField(auto_now = True) # auto_now will update date every time a data has been updated
   # def __str__(self):                      # string representation of class
    #    return self.text

    class Meta:
        ordering = ['-added_date']









        # username = aniket
        #password  = Himachal@12
 
