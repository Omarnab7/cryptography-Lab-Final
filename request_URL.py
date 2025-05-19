import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def highlight_word_in_url_with_parsing(url, target_word):
    """Fetch HTML and display with target word highlighted"""
    
    # Fetch HTML
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().lower()
    target_word = target_word.lower()
    
    # Create popup window
    popup = tk.Tk()
    popup.title(f"HTML Viewer: {url}")
    popup.geometry("800x600")
    
    # Create text widget with scrollbar
    text_box = ScrolledText(popup, wrap=tk.WORD, bg='white', fg='black')
    text_box.pack(expand=True, fill='both')
    text_box.tag_config('highlight', foreground='red')
    
    # Insert text and highlight matches
    text_box.insert('end', text)
    
    # Highlight all occurrences
    start_idx = '1.0'
    while True:
        start_idx = text_box.search(target_word, start_idx, stopindex='end')
        if not start_idx:
            break
        end_idx = f"{start_idx}+{len(target_word)}c"
        text_box.tag_add('highlight', start_idx, end_idx)
        start_idx = end_idx
    
    popup.mainloop()


def show_html_with_highlight(url, target_word):
    """Display raw HTML with highlighted target word in a simple GUI"""
    try:
        # Fetch raw HTML
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        
        # Create popup window
        window = tk.Tk()
        window.title(f"Raw HTML: {url}")
        window.geometry("1000x700")
        
        # Text widget with scrollbars
        text_box = ScrolledText(window, 
                              wrap=tk.WORD, 
                              font=('Consolas', 10), 
                              bg='white', 
                              fg='black',
                              insertbackground='white')
        text_box.pack(expand=True, fill='both')
        
        # Configure highlight style
        text_box.tag_config('highlight', foreground='red')
        
        # Insert HTML and highlight target
        text_box.insert('end', html_content)
        
        # Highlight all occurrences (case-sensitive)
        start_idx = '1.0'
        while True:
            start_idx = text_box.search(target_word, start_idx, stopindex='end')
            if not start_idx:
                break
            end_idx = f"{start_idx}+{len(target_word)}c"
            text_box.tag_add('highlight', start_idx, end_idx)
            start_idx = end_idx
        
        window.mainloop()
        
    except requests.RequestException as e:
        tk.messagebox.showerror("Error", f"Failed to fetch URL:\n{e}")

# Example usage:
show_html_with_highlight("https://google.com", "google")

# Example usage:
highlight_word_in_url_with_parsing(
    "https://en.wikipedia.org/wiki/Wiki", "Extreme")