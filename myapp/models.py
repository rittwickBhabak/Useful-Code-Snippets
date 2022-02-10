from django.urls import reverse
from django.db import models

LANGUAGE_CHOICES = [
    ('cpp', 'C++'),
    ('javascript', 'JavaScript'),
    ('python', 'Python'),
    ('c', 'C language'),
    ('java', 'Java'),
    ('css', 'CSS'),
    ('text', 'Plain Text'),
    ('php', 'PHP'),
    ('git', 'Git'),
    ('shell', 'terminal'),
    ('django', 'Django'),
    ('jinja', 'Jinja'),
    ('docker', 'Docker'),
    ('powershell', 'PowerShell'),
    ('nginx', 'Nginx'),
    ('mongodb', 'MongoDB'),
    ('markup', 'HTML'),
    ('matlab', 'MATLAB'),
    ('json', 'JSON'),
    ('graphql', 'GraphQL'),
    ('pug', 'PUG'),
    ('jsx', 'JSX'),
    ('regex', 'Regular Expression'),
    ('sass', 'SASS'),
    ('sql', 'SQL'),
    ('typescript', 'TypeScript'),
    ('vim', 'VIM')
]

class Code(models.Model):
    title = models.CharField(max_length=100)

    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    code = models.TextField()

    def get_absolute_url(self):
        return reverse("codesnippets:view-code", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title 
