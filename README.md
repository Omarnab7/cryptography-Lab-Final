# HTML Text Highlighter

Two functions to fetch web content and highlight target words in a GUI window.

---

## `show_html_with_highlight(url, target_word)`
Displays **raw HTML** with highlighted words

## `highlight_word_in_url_with_parsing(url, target_word)`
Displays **processed HTML** with highlighted words - tries to limit words on screen to paragraphs - not supported

🔴 Above func Deprecated!


```python
show_html_with_highlight("https://google.com", "google")
