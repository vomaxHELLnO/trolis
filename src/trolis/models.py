import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.db import models
from django.utils import timezone


class ListObject(models.Model):
    title = models.TextField()
    text = models.TextField()

class CheckerGame(models.Model):
    white = models.ForeignKey('User', related_name='checkers_white')
    black = models.ForeignKey('User', related_name='checkers_balck')
    p1_turn = models.BooleanField(default=True)
    over = models.BooleanField(default=False)
    board = models.TextField(default='wwwWwwwWwwWW        bbbBbbbBbbbB')
    moves = models.TextField(default='')

class User(AbstractBaseUser, PermissionsMixin):
    status = models.IntegerField(default=0)
    # 0 - not playing and no in queue
    # 1 - in queue to play
    # 2 - playing

    # is_online = models.Inte..
    # 0 - offline
    # 1 - online, but
    friends = models.ManyToManyField('self')

    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    email = models.EmailField(_('Email address'), max_length=254, unique=True, null=True)
    email_approved = models.BooleanField(_('Was email approved'), default=False)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    organization = models.TextField(_('Organization'), null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    USERNAME_FIELD = 'username'

    objects = UserManager()
