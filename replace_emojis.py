import glob
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SVG_BASE_CLASS = 'vector-icon'

def get_svg(path_data, width=24, height=24, fill='none', stroke='currentColor', color='currentColor'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 24 24" fill="{fill}" stroke="{stroke}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="{SVG_BASE_CLASS}" style="color:{color};vertical-align:middle;display:inline-block;margin-right:4px;">{path_data}</svg>'

emoji_map = {
    '📧': get_svg('<rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>'),
    '🔒': get_svg('<rect x="3" y="11" width="18" height="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>'),
    '🤖': get_svg('<rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="16" y1="16" x2="16" y2="16"></line>'),
    '🎨': get_svg('<circle cx="13.5" cy="5.5" r="2.5"></circle><circle cx="6.5" cy="8.5" r="2.5"></circle><circle cx="6.5" cy="15.5" r="2.5"></circle><circle cx="13.5" cy="18.5" r="2.5"></circle><path d="m13.5 18.5-7-10"></path><path d="m6.5 15.5 7-10"></path>'),
    '🐦': get_svg('<path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path>'),
    '🎯': get_svg('<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>'),
    '⚡': get_svg('<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>'),
    '📊': get_svg('<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line>'),
    '💼': get_svg('<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle>'),
    '📈': get_svg('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>'),
    '🎵': get_svg('<path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"></path>'),
    '🧠': get_svg('<path d="M9.5 2A2.5 2.5 0 0 0 7 4.5v1.79a5.5 5.5 0 0 0-1.6 9.85A2.49 2.49 0 0 0 8 22h8a2.49 2.49 0 0 0 2.6-5.86A5.5 5.5 0 0 0 17 6.29V4.5A2.5 2.5 0 0 0 14.5 2h-5z"></path><path d="M12 2v20"></path><path d="M12 6.5s-1.5 1.5-3 1.5"></path><path d="M12 11.5s-1.5 1.5-3 1.5"></path><path d="M12 16.5s-1.5 1.5-3 1.5"></path><path d="M12 6.5s1.5 1.5 3 1.5"></path><path d="M12 11.5s1.5 1.5 3 1.5"></path><path d="M12 16.5s1.5 1.5 3 1.5"></path>'),
    '🌈': get_svg('<path d="M22 17a10 10 0 0 0-20 0"></path><path d="M6 17a6 6 0 0 1 12 0"></path><path d="M10 17a2 2 0 0 1 4 0"></path>', stroke='var(--primary)'),
    '💬': get_svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>'),
    '🛠': get_svg('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>'),
    '📰': get_svg('<path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"></path>'),
    '🏆': get_svg('<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>'),
    '⭐': get_svg('<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>', fill='var(--primary)', stroke='var(--primary)'),
    '💜': get_svg('<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>', fill='var(--primary)', stroke='var(--primary)', width=16, height=16),
    '💙': get_svg('<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>', fill='var(--secondary)', stroke='var(--secondary)'),
    '🔍': get_svg('<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>'),
    '💡': get_svg('<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"></path><path d="M9 18h6"></path><path d="M10 22h4"></path>'),
    '🌐': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path>'),
    '😄': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>'),
    '😐': get_svg('<circle cx="12" cy="12" r="10"></circle><line x1="8" y1="15" x2="16" y2="15"></line><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>'),
    '😟': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M16 16s-1.5-2-4-2-4 2-4 2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>'),
    '😊': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>'),
    '😞': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M8 16s1.5-2 4-2 4 2 4 2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>'),
    '🙂': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>'),
    '🫂': get_svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>'),
    '🆘': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M12 8v4"></path><path d="M12 16h.01"></path>'),
    '🌿': get_svg('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"></path><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"></path>'),
    '🌸': get_svg('<circle cx="12" cy="12" r="3"></circle><path d="M12 16.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 1 1 12 7.5a4.5 4.5 0 1 1 4.5 4.5 4.5 4.5 0 1 1-4.5 4.5"></path>'),
    '🕵': get_svg('<path d="M12 2A4 4 0 0 0 8 6"></path><path d="M10.29 4.34c-1.3-.4-2.83.3-3.26 1.6-1 .85-2.26 1.1-3.5 1.07"></path><path d="M17.47 5.94c-1.24.03-2.5-.22-3.5-1.07-.43-1.3-1.96-2-3.26-1.6"></path><path d="M2 10a12 12 0 0 0 20 0H2z"></path><path d="M9 14h6"></path><path d="M8 12a4 4 0 0 0 8 0h-8z"></path>'),
    '🔁': get_svg('<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path>'),
    '💻': get_svg('<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>'),
    '🌍': get_svg('<circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path>'),
    '👍': get_svg('<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>'),
    '🚀': get_svg('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"></path><path d="m12 15-3-3a22 22 0 0 1 3.82-13.06c.09-.1.22-.1.35-.1.14 0 .27.01.4.03.35.05.69.2.98.44.38.3.64.71.74 1.18.3 1.34.62 4.48-.48 9.2A22 22 0 0 1 12 15z"></path>'),
    '📅': get_svg('<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line>'),
    '🟣': get_svg('<circle cx="12" cy="12" r="10"></circle>', fill='var(--primary)', stroke='var(--primary)'),
    '📷': get_svg('<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>'),
    '🆓': get_svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"></path>'),
    '✅': get_svg('<polyline points="20 6 9 17 4 12"></polyline>'),
    '💸': get_svg('<rect width="20" height="12" x="2" y="6" rx="2"></rect><circle cx="12" cy="12" r="2"></circle><path d="M6 12h.01M18 12h.01"></path>'),
    '⏱': get_svg('<circle cx="12" cy="13" r="8"></circle><polyline points="12 9 12 13 14 15"></polyline><line x1="12" y1="5" x2="12" y2="3"></line><line x1="2" y1="15" x2="4" y2="13"></line><line x1="22" y1="15" x2="20" y2="13"></line>'),
    '🏥': get_svg('<rect x="2" y="10" width="20" height="12" rx="2"></rect><path d="M12 10v12"></path><path d="M7 10v12"></path><path d="M17 10v12"></path><path d="M10 5h4"></path><path d="M12 3v4"></path><polygon points="12 2 14 7 10 7"></polygon>'),
    '📱': get_svg('<rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line>'),
    '🎪': get_svg('<path d="M2 20h20"></path><path d="M5 20l-2-7 9-9 9 9-2 7"></path><path d="M12 15v5"></path><path d="M9 20v-3a3 3 0 0 1 6 0v3"></path>'),
    '🧑': get_svg('<path d="M18 20a6 6 0 0 0-12 0"></path><circle cx="12" cy="10" r="4"></circle>'),
    '\u200d': '',
    '🎓': get_svg('<path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path>')
}

files = glob.glob('*.html') + glob.glob('js/*.js')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    for char, svg in emoji_map.items():
        if svg != "":
            content = content.replace(char, svg)
        elif char == '\u200d':
            content = content.replace(char, '') # remove zero width joiner
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Emojis replaced successfully.')
