from .models import Article

def get_prev_next_id(current_id):
    number_of_articles = Article.objects.count()
    
    # current_id = article.id

    if current_id > 1:
        prev_id = current_id - 1
    else:
        prev_id = number_of_articles

    if current_id < number_of_articles:
        next_id = current_id + 1
    else:
        next_id = 1
    
    return prev_id, current_id, next_id


def get_context(prev_id, current_id, next_id):
    return {
        "prev": Article.objects.filter(id=prev_id).first(),
        "article": Article.objects.filter(id=current_id).first(),
        "next": Article.objects.filter(id=next_id).first()
    }
    
