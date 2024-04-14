from .models import Article
import re

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
    
def convert_markdown(orig):
    pattern = r'```(.*?)\n(.*?)\n```'

    def replace_code_block(match):
        language = match.group(1)
        code_snippet = match.group(2)
        replacement = f'<pre><code class="language-{language}">\n{code_snippet}\n</code></pre>'
        return replacement

    result = re.sub(pattern, replace_code_block, orig, flags=re.DOTALL)

    return result