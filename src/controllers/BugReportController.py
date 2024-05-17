from django.shortcuts import redirect

from src.models.bug_report import BugReport


class BugReportController:

    @staticmethod
    def report_bug(request):
        back_to = request.POST.get('back_to')
        if request.method != 'POST':
            return redirect(back_to)

        try:
            description = request.POST.get('report_bug')

            if not description:
                return redirect(back_to)

            report = BugReport(
                title='bug report',
                description=description
            )
            report.save()

            return redirect(back_to)
        except Exception:
            return redirect(back_to)


