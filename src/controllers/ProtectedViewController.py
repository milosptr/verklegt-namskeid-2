from django.shortcuts import render, redirect

from src.models import User, Skill, UserSkill


class ProtectedViewController:
    def __init__(self, request):
        self.request = request
        self.is_authenticated = request.session.get('is_authenticated')
        self.user_id = request.session.get('user_id')
        self.skills = Skill.objects.all()

    def render(self, template, context=None):
        if context is None:
            context = {}
        if self.is_authenticated is None or self.user_id is None:
            return redirect('/login')
        user = User.get_by_id(self.user_id)
        if user is None:
            return redirect('/login')
        context['user'] = user.parse_logged_in_user()

        # Get the skills that the user does not have
        user_skills = UserSkill.objects.filter(user_id=self.user_id)
        context['skills'] = filter(lambda x: x.id not in [s.skill_id for s in user_skills], self.skills)

        return render(self.request, template, context)
