from __future__ import unicode_literals

from django.db import models

# Create your models here.


ASSET_ENV = (
    (1, u'base'),
    (2, u'dev')
)

ASSET_STATUS = (
    (1, u"used"),
    (2, u"unused"),
    (3, u"bad")
)

ASSET_TYPE = (
    (1, u"物理机"),
    (2, u"虚拟机"),
    (3, u'阿里云'),
    (4, u"Docker"),
    (5, u"switch"),
    (6, u"router"),
    (7, u"firewall"),
    (8, u'storage'),
    (9, u"other")
)


class Asset(models.Model):
    """
    asset model
    """
    ASSET_SYSTEM_TYPE = (
        (1, u'Linux'),
        (2, u'MAC OS'),
        (3, u'Windows'),
        (4, u'Service'),
    )
    ip = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'主机IP')
    other_ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'其他IP')
    hostname = models.CharField(unique=True, max_length=128, verbose_name=u"主机名")
    system_type = models.CharField(choices=ASSET_SYSTEM_TYPE, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    system_arch = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"系统平台")
    asset_status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"机器状态")
    asset_type = models.IntegerField(choices=ASSET_TYPE, blank=True, null=True, verbose_name=u"主机类型")
    asset_env = models.IntegerField(choices=ASSET_ENV, blank=True, null=True, verbose_name=u"运行环境")
    create_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.ip
