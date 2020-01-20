import feedparser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView

from .forms import RssForm
from .models import RSS

# Create your views here.


class RSSLinkAddView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    '''Add Link for parse RSS, also, we can use a rss/atom file
    for retrive RSS url; finaly  create a model for RSS '''
    
    model = RSS
    form_class = RssForm

    template_name = "rss/rss_form.html"

    success_url = reverse_lazy("homepage")
    success_message = "Rss aggiunto"

    def form_valid(self, form):

        link_reference = None

        if form.data['link']:

            link_reference = form.cleaned_data['link']

        else:

            file = self.request.FILES['file']
            link_feed = feedparser.parse(file)

            for link in link_feed.feed.links:

                if link.get('type') == 'application/atom+xml':
                    link_reference = link.get('href')

                elif link.get('type') == 'application/rss+xml':
                    link_reference = link.get('href')

        rss, created = RSS.objects.get_or_create(link=link_reference,
                                                 user=self.request.user)

        if not created:
            rss.link = link_reference
            rss.save()

        return super().form_valid(form)


class RSSDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''Delete RSS'''
    model = RSS

    success_url = reverse_lazy("homepage")
    success_message = "RSS eliminato"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class RSSArticleView(LoginRequiredMixin, DetailView):
    '''Show articles for selected RSS channel'''
    model = RSS
    template_name = "rss/rss.html"

    def get_context_data(self, **kwargs):
        link = RSS.objects.get(pk=self.kwargs['pk'])
        feeds = feedparser.parse(str(link))

        for entry in feeds.entries:
            for enclosure in entry.enclosures:
                print(enclosure)

        context = super().get_context_data(**kwargs)
        context['feeds'] = feeds

        return context
