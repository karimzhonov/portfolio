from datetime import date
from django.db import models


class Settings(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icon/')
    background = models.ImageField(upload_to='background/')
    jobs = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatar/')
    views = models.IntegerField(default=1)
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.title

    def get_full_name(self):
        return f'{self.first_name} <br> {self.last_name}'


class SocialLink(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    social_id = models.CharField(max_length=255)

    def __str__(self):
        return self.link


class AboutMe(models.Model):
    job = models.CharField(max_length=255)
    img = models.ImageField(upload_to='about/')
    birth_day = models.DateField()
    email = models.EmailField(max_length=255)
    text = models.TextField(max_length=255, blank=True)
    more = models.ManyToManyField('AboutMeMore', blank=True)

    def __str__(self):
        return self.job

    def get_age(self):
        return date.today().year - self.birth_day.year - \
               ((date.today().month, date.today().day) < (self.birth_day.month, self.birth_day.day))


class AboutMeMore(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Experience(models.Model):
    name = models.CharField(max_length=255)
    from_at = models.DateField()
    to_at = models.DateField()
    where = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    experience = models.ForeignKey('ExperienceType', on_delete=models.CASCADE, related_name='exp')

    def __str__(self):
        return self.name

    def get_from_to_at(self):
        return f'{self.from_at.year} - {self.to_at.year}'


class ExperienceType(models.Model):
    name = models.CharField(max_length=255)
    empty = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_exp(self):
        return Experience.objects.filter(experience__name=self.name)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    rate = models.CharField(max_length=100)
    type = models.ForeignKey('SkillType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SkillType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    def get_skills(self):
        return Skill.objects.filter(type__slug=self.slug)


class Project(models.Model):
    img = models.ImageField(upload_to='projects/')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    link = models.CharField(max_length=255)
    type = models.ManyToManyField('ProjectType')

    def __str__(self):
        return self.name

    def get_filter_name(self):
        res = ''
        for point in self.type.all():
            res += f'{point.slug} '
        return res

    class Meta:
        ordering = ['-pk']


class ProjectType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
