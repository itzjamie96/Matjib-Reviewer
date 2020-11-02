# Matjib Reviewer

### Index

![image-20200821171322851](img/image-20200821171322851.png)

<br>

**부가설명**

![hrefs](img/hrefs.png)

<br>




### 3. new_review , create_review

![image-20200821171457228](img/image-20200821171457228.png)




### 4. review_detail

![image-20200821171414454](img/image-20200821171414454.png)


### 5. models.py

```python
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

<hr>

### 6. admin.py

```python
admin.site.register(Review)
```

![image-20200821180253760](img/image-20200821180253760.png)

