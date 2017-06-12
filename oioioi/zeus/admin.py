from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from oioioi.zeus.models import ZeusProblemData


class ZeusProblemDataInline(admin.StackedInline):
    model = ZeusProblemData
    can_delete = False
    extra = 0
    max_num = 0
    readonly_fields = ['zeus_instance', 'zeus_problem_id']
    fields = readonly_fields
    inline_classes = ('collapse',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def zeus_instance(self, instance):
        zeus_id = instance.zeus_id
        if zeus_id in settings.ZEUS_INSTANCES:
            return '%s: %s' % (zeus_id, settings.ZEUS_INSTANCES[zeus_id][0])
        return zeus_id
    zeus_instance.short_description = _("Zeus instance")


class ZeusProblemAdminMixin(object):
    """Adds :class:`~oioioi.zeus.models.ZeusProblemData` to an admin panel.
    """

    def __init__(self, *args, **kwargs):
        super(ZeusProblemAdminMixin, self).__init__(*args, **kwargs)
        self.inlines = [ZeusProblemDataInline] + self.inlines
