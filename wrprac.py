from PIL import Image
import numpy as np
from wordcloud import WordCloud

text = ''

with open("warning_chat.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('너는', '').replace('오늘', '').replace('톡게시판', '').replace('합니다', '').replace('너도', '').replace('나는', '').replace('저기', '').replace('여러분', '').replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','').replace('삭제된 메시지입니다','')
# print(text)


wc = WordCloud(font_path='C:/Windows/Fonts/.TTF', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")


mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/.TTF', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
