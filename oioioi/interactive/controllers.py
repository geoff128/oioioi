from django.utils.translation import gettext_lazy as _

from oioioi.filetracker.utils import django_to_filetracker_path
from oioioi.interactive.models import Interactor
from oioioi.programs.controllers import ProgrammingProblemController


class InteractiveProblemController(ProgrammingProblemController):
    description = _("Interactive programming problem")

    def fill_evaluation_environ(self, environ, submission, **kwargs):
        super().fill_evaluation_environ(environ, submission, **kwargs)

        interactor = Interactor.objects.get(problem=self.problem)
        environ['interactor_file'] = django_to_filetracker_path(interactor.exe_file)

        environ['task_type_suffix'] = '-interactive-exec'

    def can_generate_user_out(self, request, submission_report):
        return False

    def allow_test_runs(self, request):
        return False
