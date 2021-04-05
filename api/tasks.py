import logging

from celery import shared_task

from .models import Post


@shared_task
def reset_upvotes():
    """
    Celery task to reset amount of upvotes for every post.
    """
    logging.info("Reset upvotes in process...")
    Post.objects.all().update(upvotes_amount=0)
    logging.info("Reset upvotes successfully done!")
